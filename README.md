# Task 1: Exploring and Visualizing the Iris Dataset

## Overview

This project is part of the **DevelopersHub Corporation AI/ML Engineering Internship Tasks**.

The objective of this task is to perform:

* Data loading
* Data inspection
* Exploratory Data Analysis (EDA)
* Data visualization

using the classic **Iris Dataset** with Python libraries such as:

* Pandas
* Matplotlib
* Seaborn

---

# Objective

The main goal of this project is to:

* Understand the structure of the Iris dataset
* Explore relationships between features
* Visualize data distributions
* Detect potential outliers
* Build strong foundational skills in data analysis and visualization

---

# Dataset Information

The Iris dataset contains measurements of iris flowers from three different species:

* Setosa
* Versicolor
* Virginica

### Features

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width
* Species

Dataset Source:

* Built-in dataset available in Seaborn
* Optional local CSV fallback (`iris.csv`)

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

# Project Structure

```bash
project-folder/
│
├── task1_iris_visualization.py
├── iris.csv                # Optional local dataset
├── task1_pairplot.png
├── task1_histograms.png
├── task1_boxplots.png
└── README.md
```

---

# Features Implemented

## 1. Dataset Loading

* Loads dataset directly from Seaborn
* Includes fallback loading from local CSV file

## 2. Data Inspection

* Dataset shape
* Column names
* First 5 rows
* Data types and missing values
* Descriptive statistics

## 3. Data Visualization

### Pairplot

Shows pairwise relationships between all numerical features.

### Histograms

Displays distributions of:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### Boxplots

Used for:

* Outlier detection
* Feature comparison across species

---

# Output Visualizations

The script automatically saves:

* `task1_pairplot.png`
* `task1_histograms.png`
* `task1_boxplots.png`

---

# How to Run

## Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

## Run the Script

```bash
python task1_iris_visualization.py
```

---

# Key Insights

* Petal features provide strong separation between species.
* Setosa species is easily distinguishable from others.
* Some minor outliers are visible in sepal width measurements.
* Feature distributions vary significantly between species.

---

# Learning Outcomes

Through this project, the following skills were practiced:

* Data loading using Pandas
* Exploratory Data Analysis (EDA)
* Statistical summaries
* Data visualization with Seaborn and Matplotlib
* Outlier detection
* Writing clean and professional Python code

---

# Author
prepared by :Ubaid Ullah

Prepared for:
**DevelopersHub Corporation – AI/ML Engineering Internship**

Developed using Python and modern data science libraries.
