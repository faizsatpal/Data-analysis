import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Dataset: Iris Dataset
from sklearn.datasets import load_iris

data = load_iris(as_frame=True).frame

# Task 1: Load and Explore the Dataset
try:
    # Display the first few rows of the dataset
    print("First few rows of the dataset:")
    print(data.head())

    # Explore the structure of the dataset
    print("\nDataset Info:")
    print(data.info())

    # Check for missing values
    print("\nMissing Values:")
    print(data.isnull().sum())

    # Clean the dataset (example: filling missing values with the mean)
    data.fillna(data.mean(), inplace=True)
    print("\nMissing values after cleaning:")
    print(data.isnull().sum())

except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
try:
    # Compute basic statistics
    print("\nBasic Statistics:")
    print(data.describe())

    # Grouping and computing mean (example: grouping by target)
    group_column = 'target'  # Target is the species column in the Iris dataset
    numeric_column = 'sepal length (cm)'  # Example numerical column

    if group_column in data.columns and numeric_column in data.columns:
        grouped_data = data.groupby(group_column)[numeric_column].mean()
        print("\nMean of numerical column grouped by categorical column:")
        print(grouped_data)
    else:
        print("Specified columns for grouping are not in the dataset.")

except Exception as e:
    print(f"An error occurred during analysis: {e}")

# Task 3: Data Visualization
try:
    # Line chart (example: cumulative mean of a numerical column)
    if numeric_column in data.columns:
        cumulative_mean = data[numeric_column].expanding().mean()
        plt.figure(figsize=(10, 6))
        plt.plot(cumulative_mean, label='Cumulative Mean')
        plt.title('Line Chart of Cumulative Mean')
        plt.xlabel('Index')
        plt.ylabel('Cumulative Mean')
        plt.legend()
        plt.show()

    # Bar chart (example: mean sepal length by species)
    if group_column in data.columns and numeric_column in data.columns:
        grouped_data.plot(kind='bar', figsize=(10, 6))
        plt.title('Bar Chart of Average Sepal Length by Species')
        plt.xlabel('Species')
        plt.ylabel(f'Average {numeric_column}')
        plt.show()

    # Histogram (example: distribution of sepal length)
    if numeric_column in data.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[numeric_column], kde=True, bins=20)
        plt.title('Histogram of Sepal Length')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Frequency')
        plt.show()

    # Scatter plot (example: sepal length vs sepal width)
    if 'sepal length (cm)' in data.columns and 'sepal width (cm)' in data.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=data['sepal length (cm)'], y=data['sepal width (cm)'], hue=data['target'])
        plt.title('Scatter Plot of Sepal Length vs Sepal Width')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Sepal Width (cm)')
        plt.legend(title='Species')
        plt.show()

except Exception as e:
    print(f"An error occurred during visualization: {e}")
