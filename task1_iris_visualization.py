
"""
Task 1: Exploring and Visualizing the Iris Dataset
-------------------------------------------------
Objective:
Explore, analyze, and visualize the Iris dataset using pandas,
matplotlib, and seaborn.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# Load Dataset
# -------------------------------
iris = sns.load_dataset("iris")

# -------------------------------
# Basic Dataset Inspection
# -------------------------------
print("\nDataset Shape:")
print(iris.shape)

print("\nColumn Names:")
print(iris.columns)

print("\nFirst 5 Rows:")
print(iris.head())

print("\nDataset Info:")
print(iris.info())

print("\nSummary Statistics:")
print(iris.describe())

# -------------------------------
# Scatter Plot
# -------------------------------
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=iris,
    x="sepal_length",
    y="petal_length",
    hue="species"
)
plt.title("Sepal Length vs Petal Length")
plt.savefig("scatter_plot.png")
plt.close()

# -------------------------------
# Histograms
# -------------------------------
iris.hist(figsize=(10, 8))
plt.suptitle("Feature Distributions")
plt.savefig("histograms.png")
plt.close()

# -------------------------------
# Boxplots
# -------------------------------
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris)
plt.title("Boxplot for Detecting Outliers")
plt.savefig("boxplot.png")
plt.show()

print("\nVisualizations saved successfully.")
