# ============================================
# ASSIGNMENT: Data Loading, Analysis, and Visualization
# ============================================

# 🎯 Objective:
# - Load and analyze a dataset using pandas
# - Visualize the data using matplotlib and seaborn

# ============================================
# Import Required Libraries
# ============================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Enable inline plotting (for Jupyter Notebook)
# %matplotlib inline   # Uncomment this if using a Jupyter Notebook


# ============================================
# Task 1: Load and Explore the Dataset
# ============================================

# Load the Iris dataset from sklearn
try:
    iris_data = load_iris()
    df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df['species'] = iris_data.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    print("✅ Dataset successfully loaded!\n")

except FileNotFoundError:
    print("❌ Error: Dataset file not found.")
except Exception as e:
    print(f"❌ An error occurred while loading the dataset: {e}")

# Display first few rows
print("🔹 First five rows of the dataset:")
print(df.head(), "\n")

# Display structure and info
print("🔹 Dataset Info:")
print(df.info(), "\n")

# Check for missing values
print("🔹 Missing Values:")
print(df.isnull().sum(), "\n")

# (For demonstration) — Fill or drop missing values if they existed
df = df.dropna()
print("✅ Data cleaned — no missing values remaining.\n")


# ============================================
# Task 2: Basic Data Analysis
# ============================================

# Compute basic statistics
print("🔹 Basic Statistical Summary:")
print(df.describe(), "\n")

# Group by 'species' and compute mean of numerical columns
grouped = df.groupby('species').mean()
print("🔹 Mean of each numerical column grouped by species:")
print(grouped, "\n")

# Findings / Observations
print("🔍 Observations:")
print("- Setosa generally has the smallest petal and sepal measurements.")
print("- Virginica tends to have the largest features.")
print("- Versicolor lies roughly between Setosa and Virginica in most metrics.\n")


# ============================================
# Task 3: Data Visualization
# ============================================

# Set Seaborn style for better visuals
sns.set(style="whitegrid")

# ---------- 1. Line Chart ----------
plt.figure(figsize=(8,5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length', color='teal')
plt.title('Line Chart: Sepal Length Trend')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

# ---------- 2. Bar Chart ----------
plt.figure(figsize=(8,5))
sns.barplot(x='species', y='petal length (cm)', data=df, palette='pastel')
plt.title('Bar Chart: Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# ---------- 3. Histogram ----------
plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=10, color='orchid', edgecolor='black')
plt.title('Histogram: Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# ---------- 4. Scatter Plot ----------
plt.figure(figsize=(8,5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, s=80)
plt.title('Scatter Plot: Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()


# ============================================
# Final Summary
# ============================================

print("✅ Assignment Completed Successfully!")
print("\n📊 Summary of Analysis:")
print("""
1. The dataset contains 150 samples across 3 species of Iris flowers.
2. Virginica species have the largest petal and sepal dimensions.
3. Setosa species are distinctively smaller in all measurements.
4. The relationship between petal and sepal length is positive — 
   as one increases, so does the other.
""")
