import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('QVI_transaction_data.csv')

# Step 1: Data Overview
print("Data Overview:")
print(data.info())  # Basic information about the dataset

# Step 2: Check for Missing Values
print("\nMissing Values:")
print(data.isnull().sum())  # Count the missing values in each column

# Step 3: Data Summary Statistics
print("\nSummary Statistics:")
print(data.describe())  # Summary statistics for numeric columns

# Step 4: Data Visualization (using Matplotlib)
# Box Plot for 'TXN_ID', 'PROD_QTY', and 'TOT_SALES'
plt.figure(figsize=(4, 4))
plt.boxplot([data['TXN_ID'], data['PROD_QTY'], data['TOT_SALES']], labels=['TXN_ID', 'PROD_QTY', 'TOT_SALES'])
plt.xlabel('Columns')
plt.ylabel('Values')
plt.title('Box Plot')
plt.grid(True)
plt.show()

# Histogram for 'TOT_SALES'
plt.figure(figsize=(8, 5))
plt.hist(data['TOT_SALES'], bins=20, color='skyblue', edgecolor='black', density=True)
plt.xlabel('TOT_SALES')
plt.ylabel('Density')
plt.title('Histogram')
plt.grid(True)
plt.show()

# Scatter Plot for 'PROD_QTY' vs. 'TOT_SALES' with the specified range
plt.figure(figsize=(8, 5))
plt.scatter(data['PROD_QTY'], data['TOT_SALES'], color='orange', alpha=0.7)
plt.xlabel('PROD_QTY')
plt.ylabel('TOT_SALES')
plt.title('Scatter Plot')
plt.grid(True)

# Set the range for the x-axis and y-axis
plt.xlim(0, 8)
plt.ylim(0, 50)

plt.show()

