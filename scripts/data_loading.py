# scripts/data_loading.py

import pandas as pd

def load_data(filepath):
    print(3.1)
    """
    Load CSV data from the given file path and return a pandas DataFrame.
    """
    try:
        df = pd.read_csv(filepath, parse_dates=['Timestamp'])
        return df
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def initial_exploration(df):
    """
    Perform initial exploration on the DataFrame.
    """
    print("First 5 rows of the data:\n", df.head())
    print("\nData Info:\n", df.info())
    print("\nData Description:\n", df.describe())
