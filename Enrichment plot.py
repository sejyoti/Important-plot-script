import matplotlib.pyplot as plt
import numpy as np

# Data
enrichment_fdr = [6.90E-07, 8.02E-14, 5.24E-07, 3.95E-05, 8.00E-07, 1.60E-05, 1.99E-05, 1.79E-05,
                  0.000180911847850784, 3.95E-05, 1.99E-05, 1.99E-05, 4.02E-06, 0.000180911847850784,
                  0.000208612837562355, 4.72E-05, 0.000180911847850784, 5.51E-06, 5.24E-07, 2.60E-05]

n_genes = [20, 56, 31, 22, 39, 31, 32, 41, 34, 41, 46, 47, 58, 40, 45, 57, 56, 83, 125, 283]

fold_enrichment = [3.89675213675214, 3.11740170940171, 2.97861327713383, 2.85761823361823, 2.53288888888889,
                   2.52835778175313, 2.43970568561873, 2.19526952436876, 2.1292967032967, 2.09912633352049,
                   2.06827613412229, 2.04761012900143, 2.01396496572734, 1.98983087834152, 1.89004145555044,
                   1.8424275079759, 1.76933610533611, 1.75883616081803, 1.65428156748911, 1.29993813913657]

pathways = ['DNA replication', 'Cell cycle', 'P53 signaling pathway', 'Fanconi anemia pathway',
            'Nucleocytoplasmic transport', 'Colorectal cancer', 'Small cell lung cancer', 'FoxO signaling pathway',
            'TNF signaling pathway', 'Yersinia infection', 'Cellular senescence', 'MicroRNAs in cancer',
            'Proteoglycans in cancer', 'Ubiquitin mediated proteolysis', 'Hepatocellular carcinoma',
            'Reg. of actin cytoskeleton', 'Human T-cell leukemia virus 1 infection', 'Human papillomavirus infection',
            'Pathways in cancer', 'Metabolic pathways']

# Create a color map for the number of genes
genes_color_map = plt.cm.get_cmap('Blues')

# Plotting
plt.figure(figsize=(8, 12))
plt.scatter(fold_enrichment, pathways, s=n_genes, c=n_genes, cmap='coolwarm', alpha=0.7, edgecolors='black')
plt.xlabel('Fold Enrichment')
plt.ylabel('Pathway')
plt.title('Enrichment Significant')
plt.colorbar(label='Number of Genes', orientation='vertical', cmap=genes_color_map)
plt.grid(True)
plt.yticks(pathways, fontsize=8)
plt.tight_layout()


