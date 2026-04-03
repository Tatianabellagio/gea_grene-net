# gea_grene-net

Code and analyses for gene-environment association (GEA) studies using the [GrENE-Net](http://grene-net.org/) *Arabidopsis thaliana* outdoor evolution experiment. Multiple GEA methods are compared and integrated to identify loci underlying local adaptation to climate.

## Publication

Wu X, Bellagio T, Peng Y, Czech L, Lin M et al. (2025). *Rapid adaptation and extinction across climates in synchronized outdoor evolution experiments of Arabidopsis thaliana.* bioRxiv. [doi: 10.1101/2025.05.28.654549](https://www.biorxiv.org/content/10.1101/2025.05.28.654549v1)

---

## Overview

The analyses link genomic variation in *A. thaliana* populations to climatic variables across GrENE-Net experimental sites, using several complementary GEA methods:

- **LFMM** — latent factor mixed model
- **Binomial regression** — allele frequency change regressed on climate
- **Kendall tau** — rank correlation with climate variables
- **GWAS** — genome-wide association
- **Weighted-Z analysis (WZA)** — gene-level aggregation of association signals
- **Genomic offset** — predictions of maladaptation under climate change
- **Demographic analysis** — controlling for population structure

---

## Repository structure

```
preproc_scripts/                          # Preprocessing and data preparation
gwas/                                     # GWAS-based association analyses
lfmm/                                     # LFMM GEA
binomial_regression/                      # Binomial regression GEA
kendall_tau/                              # Kendall tau climate correlations
climate_distance/                         # Climate distance calculations
demography_analysis/                      # Demographic history analyses
manhattan_plot_GEA_annotated/             # Annotated Manhattan plots
signficant_intersection_GEA_models/       # Intersection of significant hits across methods
key_files/                                # Key input/output files
ARCHIVE/                                  # Archived intermediate analyses
```

---

## Tools & dependencies

- R (`lfmm`, `vegan`, `ggplot2`)
- Python 3, Jupyter
- [bcftools](https://samtools.github.io/bcftools/), [PLINK](https://www.cog-genomics.org/plink/)
