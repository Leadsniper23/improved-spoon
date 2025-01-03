import pandas as pd
import numpy as np
import requests

# Example: Create a DataFrame using pandas
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Example: Create a NumPy array
array = np.array([1, 2, 3, 4, 5])
print("\nNumPy Array:")
print(array)

# Example: Make a request using requests
response = requests.get('https://api.github.com')
print("\nGitHub API Response:")
print(response.json())
