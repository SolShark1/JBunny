# main.py

import numpy as np
import pandas as pd
import requests
from flask import Flask
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Print a simple message
print("Hello, GitHub Codespaces!")

# Use NumPy to create an array
arr = np.array([1, 2, 3, 4, 5])
print("NumPy array:", arr)

# Use Pandas to create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print("Pandas DataFrame:\n", df)

# Use Requests to fetch data from an API
response = requests.get("https://api.github.com")
print("GitHub API status:", response.status_code)

# Use Flask to create a simple web app
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask!"

# Use Matplotlib to create a simple plot
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Simple Plot")
plt.show()

# Use scikit-learn to load a dataset
iris = load_iris()
print("Iris dataset keys:", iris.keys())

# Sample Flask app start (commented out to avoid blocking the script)
# if name == '__main__':
#     app.run(debug=True)
