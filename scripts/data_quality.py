# scripts/data_quality.py

import pandas as pd

def check_missing_values(df):
    """
    Check for missing values in the DataFrame and return a summary.
    """
    missing_values = df.isnull().sum()
    missing_summary = missing_values[missing_values > 0]
    return missing_summary

def check_duplicates(df):
    """
    Check for duplicate rows in the DataFrame and return the count.
    """
    duplicates = df.duplicated().sum()
    return duplicates

def check_outliers(df):
    """
    Check for outliers or incorrect entries in the DataFrame.
    """
    outliers = {}
    # Iterate through each column
    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:  # Check only numerical columns
            # Calculate 1st and 99th percentiles
            lower_bound = df[column].quantile(0.01)
            upper_bound = df[column].quantile(0.99)
            
            # Identify outliers
            outlier_count = df[(df[column] < lower_bound) | (df[column] > upper_bound)].shape[0]
            if outlier_count > 0:
                outliers[column] = {
                    'lower_bound': lower_bound,
                    'upper_bound': upper_bound,
                    'outlier_count': outlier_count
                }
    return outliers

def validate_data_types(df):
    """
    Validate data types for each column.
    """
    data_types = df.dtypes
    return data_types

def calculate_summary_statistics(df):
    """
    Calculate summary statistics for numerical columns in the DataFrame.
    """
    summary_stats = df.describe()
    return summary_stats