import pandas as pd
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

# Load data from Excel file
gene_data = pd.read_excel("Gene names.xlsx")  # Replace with the actual file path

# Extract gene names based on groups
control_genes = set(gene_data[gene_data["Control"] == 1]["Control"])
treatment_genes = set(gene_data[gene_data["Treatment"] == 1]["Treatment"])

# Create Venn diagram
venn = venn2([control_genes, treatment_genes], ("Control", "Treatment"))

# Add labels to the diagram
venn.get_label_by_id('10').set_text(len(control_genes))
venn.get_label_by_id('01').set_text(len(treatment_genes))
venn.get_label_by_id('11').set_text(len(control_genes & treatment_genes))

# Display the diagram
plt.title("Gene Venn Diagram")
plt.show()

