import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

strains = '/home/sejyoti/Downloads/plastic_heatmap.csv'

# Load the data into a DataFrame
df = pd.read_csv(strains)

# Get the sample list from the first column
sample_list = df.iloc[:, 0].tolist()

# Define the subsets
subset_1 = df.iloc[:, 1].tolist()
subset_a = df.iloc[:, 2].tolist()
subset_2 = df.iloc[:, 3].tolist()
subset_b = df.iloc[:, 4].tolist()
subset_3 = df.iloc[:, 5].tolist()
subset_c = df.iloc[:, 6].tolist()
subset_4 = df.iloc[:, 7].tolist()
subset_d = df.iloc[:, 8].tolist()
subset_5 = df.iloc[:, 9].tolist()
subset_e = df.iloc[:, 10].tolist()

# Create a dictionary to store the presence or absence information
matrix_data = {
    'Inlet Site': [subset_a[subset_1.index(item)] if item in subset_1 else 0 for item in sample_list],
    'Outlet Site': [subset_b[subset_2.index(item)] if item in subset_2 else 0 for item in sample_list],
    'Station1': [subset_c[subset_3.index(item)] if item in subset_3 else 0 for item in sample_list],
    'Station2': [subset_d[subset_4.index(item)] if item in subset_4 else 0 for item in sample_list],
    'Station3': [subset_e[subset_5.index(item)] if item in subset_5 else 0 for item in sample_list]
}

# Create the matrix DataFrame
matrix = pd.DataFrame(matrix_data, index=sample_list)

# Save the matrix as CSV
matrix.to_csv("Test_HM_Genes_For_Heatmap.csv")

# Create the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(matrix, cmap="Blues", annot=False, cbar=True)

# Add labels and title
plt.title('Bioremediating Microbes', fontname='Arial', fontsize=12, fontweight='bold')
plt.xlabel('Sample', fontname='Arial', fontsize=12, fontweight='bold')
plt.ylabel('Genes', fontname='Arial', fontsize=12, fontweight='bold')

plt.xticks(fontname='Arial', fontsize=12)
plt

