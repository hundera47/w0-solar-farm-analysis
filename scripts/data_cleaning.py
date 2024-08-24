import pandas as pd
from scipy import stats

# scripts/data_cleaning.py

def handle_missing_values(df):
#               3.1 Handle Missing Values

    # Check for missing values
    missing_values = df.isnull().sum()

    # Option 1: Drop columns or rows with a significant number of missing values
    df_cleaned = df.dropna(axis=1, thresh=0.5*len(df))  # Drop columns with more than 50% missing
    df_cleaned = df_cleaned.dropna(axis=0)  # Drop rows with any missing values

    # Option 2: Fill missing values with mean or median
    # df_cleaned = df.fillna(df.mean())
    print('sucessfully cleaned')
    return df_cleaned
#**************************************************************
# scripts/data_cleaning.py
#       3.2 Outlier Treatment

def treat_outliers(df):
    """
    Treat outliers in the dataset using Z-score analysis.
    """
    z_scores = stats.zscore(df.select_dtypes(include=['float64', 'int64']))
    abs_z_scores = abs(z_scores)
    filtered_entries = (abs_z_scores < 3).all(axis=1)  # Keep only data within 3 standard deviations
    df_outliers_removed = df[filtered_entries]
    print('outliers removed!')
    return df_outliers_removed

#*****************************************************************
# scripts/data_cleaning.py
#          3.3 Final Data Preparation

def final_data_preparation(df):
    """
    Perform final cleaning and preparation of the dataset.
    """
    # Convert Timestamp to datetime using .loc[] to avoid SettingWithCopyWarning
    if 'Timestamp' in df.columns:
        df.loc[:, 'Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Drop 'Comments' column if it exists
    if 'Comments' in df.columns:
        df = df.drop(columns=['Comments'])

    return df
