# scripts/eda.py


from scipy import stats 
import seaborn as sns
import matplotlib.pyplot as plt

def plot_time_series(df, columns, title_prefix):
    """
    Plot time series graphs for specified columns.
    
    Parameters:
    df (DataFrame): The data to plot.
    columns (list): List of column names to plot.
    title_prefix (str): The prefix for the title of the plots.
    """
    for column in columns:
        plt.figure(figsize=(10, 6))
        plt.plot(df['Timestamp'], df[column], label=column)
        plt.xlabel('Time')
        plt.ylabel(f'{column} (W/m²)' if 'W/m²' in column else column)
        plt.title(f'{title_prefix} {column} Over Time')
        plt.legend()
        plt.grid(True)
        plt.show()

#***********************************************
# 4.2 Correlation Analysis
# scripts/eda.py (add this to the existing file)

def plot_correlation_heatmap(df, title):
    """
    Plot a heatmap of the correlation matrix.
    
    Parameters:
    df (DataFrame): The data to calculate the correlation matrix.
    title (str): The title of the heatmap.
    """
    plt.figure(figsize=(12, 8))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(f'Correlation Matrix: {title}')
    plt.show()

#**********************************************************
# scripts/eda.py (add this to the existing file)

def plot_scatter(df, x_col, y_col, title):
    """
    Plot a scatter plot to visualize the relationship between two variables.
    
    Parameters:
    df (DataFrame): The data to plot.
    x_col (str): The column name for the x-axis variable.
    y_col (str): The column name for the y-axis variable.
    title (str): The title of the scatter plot.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col], alpha=0.5)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'{title}: {x_col} vs {y_col}')
    plt.grid(True)
    plt.show()

#**************************************************************
# scripts/eda.py (add this to the existing file)

def plot_histogram(df, column, bins=50, title=''):
    """
    Plot a histogram to visualize the distribution of a variable.
    
    Parameters:
    df (DataFrame): The data to plot.
    column (str): The column name to plot the histogram for.
    bins (int): Number of bins in the histogram.
    title (str): The title of the histogram.
    """
    plt.figure(figsize=(10, 6))
    df[column].hist(bins=bins)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'{title}: Histogram of {column}')
    plt.grid(True)
    plt.show()
#***********************************************************
# scripts/eda.py (add this to the existing file)

def plot_bubble_chart(df, x_col, y_col, size_col, title):
    """
    Plot a bubble chart to visualize relationships between three variables.
    
    Parameters:
    df (DataFrame): The data to plot.
    x_col (str): The column name for the x-axis variable.
    y_col (str): The column name for the y-axis variable.
    size_col (str): The column name for the bubble size variable.
    title (str): The title of the bubble chart.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col], s=df[size_col]*10, alpha=0.5)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'{title}: {x_col} vs {y_col} (Size: {size_col})')
    plt.grid(True)
    plt.show()


#*******************************
