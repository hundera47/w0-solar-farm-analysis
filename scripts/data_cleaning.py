# scripts/data_cleaning.py

def handle_missing_values(df):
    """
    Handle missing values in the dataset.
    """
    # Check for missing values
    missing_values = df.isnull().sum()

    # Option 1: Drop columns or rows with a significant number of missing values
    df_cleaned = df.dropna(axis=1, thresh=0.5*len(df))  # Drop columns with more than 50% missing
    df_cleaned = df_cleaned.dropna(axis=0)  # Drop rows with any missing values

    # Option 2: Fill missing values with mean or median
    # df_cleaned = df.fillna(df.mean())
    print('sucessfully cleaned')
    return df_cleaned
