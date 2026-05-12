# Import plotting library
import matplotlib.pyplot as plt


# Initial gene expression dictionary (fixed)
gene_expression = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}
# Add new gene MYC (fixed value)
gene_expression["MYC"] = 11.6


# You can modify this line to test different genes
gene_of_interest = "TP53"


print("===== Task 1: Gene Expression Analysis =====")
print("Complete Gene Expression Data:", gene_expression)

# Plot bar chart
gene_names = list(gene_expression.keys())
expression_values = list(gene_expression.values())

plt.figure(figsize=(8, 4))
plt.bar(gene_names, expression_values, color='skyblue')
plt.title('Gene Expression Levels')
plt.xlabel('Gene Name')
plt.ylabel('Expression Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Check target gene
if gene_of_interest in gene_expression:
    print(f"\nExpression of {gene_of_interest} is {gene_expression[gene_of_interest]}")
else:
    print(f"\nError: {gene_of_interest} not found!")

# Calculate average expression
average = sum(expression_values) / len(expression_values)
print(f"Average Expression: {average:.2f}")