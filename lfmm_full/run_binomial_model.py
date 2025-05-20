import pandas as pd
import argparse
import statsmodels.api as sm
from statsmodels.formula.api import glm
import pickle
# Set up argument parser
parser = argparse.ArgumentParser(description='Process Kendall tau correlations for a specific run.')
parser.add_argument('partition', type=str, help='The run identifier to process')

# Parse arguments
args = parser.parse_args()
partition = int(args.run)

env_variable = pd.read_csv('env.csv')

partition_0 = pd.read_csv(f'../baypass_terminal/individual_gfiles/partition_{partition}.txt',header=None) 

pickle_file_path = f'../baypass_terminal/individual_gfiles/column_names_partition_{partition}'
with open(pickle_file_path, 'rb') as file:
    data0 = pickle.load(file)

partition_0.columns = data0

minor_columns = partition_0.filter(like='minor')
major_columns = partition_0.filter(like='major')

# Properly calculate total allele counts by summing corresponding minor and major allele counts
total_allele_counts = minor_columns.values + major_columns.values

# Create a new DataFrame for total counts with proper column names
total_allele_counts_df = pd.DataFrame(total_allele_counts, columns=minor_columns.columns.str.replace('_minor', '_total'))

minor_alleles = minor_columns.T.reset_index(drop=True)
major_columns = major_columns.T.reset_index(drop=True)

# Total allele counts as the number of trials (total attempts)
total_alleles = total_allele_counts_df.T.reset_index(drop=True)

successes = minor_alleles.iloc[:,1]
failures = major_columns.iloc[:,1]

# Running binomial regression for each SNP separately
coefficients_df = {}

for i in range(minor_alleles.shape[1]):
    # Prepare response (successes, failures) and predictors (environmental variable)
    successes = minor_alleles.iloc[:,i]
    failures = major_columns.iloc[:,i]
    # Set up the binomial regression model
    X = sm.add_constant(env_variable_scaled)  # Adding constant for intercept
    y = pd.concat([successes,failures],axis=1)
    # Fit the modelb
    model = sm.GLM(y, X, family=sm.families.Binomial())
    result = model.fit()

    # Extract slope (coefficient for environmental variable) and p-value
    slope = result.params[1]  # Coefficient for the environmental variable
    p_value = result.pvalues[1]  # P-value for the environmental variable
    
    # Append the results to the DataFrame
    coefficients_df[i] = [slope, p_value]

coefficients_df = pd.DataFrame(coefficients_df).T

coefficients_df.columns = ['slope', 'pvalue']

coefficients_df.to_csv(f'results/partition{partition}.csv',index=None)