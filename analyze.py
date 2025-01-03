import pandas as pd

# Load the dataset
df = pd.read_csv("data.csv")

# Display the first few rows
print("Dataset:")
print(df.head())

# Calculate the average age
avg_age = df['Age'].mean()
print("\nAverage Age:", avg_age)

# Calculate the total salary
total_salary = df['Salary'].sum()
print("Total Salary:", total_salary)
