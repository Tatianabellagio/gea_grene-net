import os

# List of required input files
required_files = [
    '../key_files/generation_1_sample_names.txt',
    '../key_files/bioclimvars_sites_era5_year_2018.csv',
    '../key_files/allele_freq_maf05_mincount05_firstgensamples.csv',
    '../key_files/delta_p_maf05_mincount05_firstgensamples.csv',
    '../key_files/var_pos_grenenet.csv',
    '../key_files/blocks_snpsid_dict.pkl'
]

# Function to verify if a file exists and has content
def verify_file(file_path):
    if os.path.exists(file_path):
        if os.path.getsize(file_path) > 0:
            return True, 'File exists and has content.'
        else:
            return False, 'File exists but is empty.'
    else:
        return False, 'File does not exist.'

# Verify each file
for file in required_files:
    exists, message = verify_file(file)
    print(f'{file}: {message}') 