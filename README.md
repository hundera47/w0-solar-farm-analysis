                                    Solar Farm Data Analysis Project
                                           Project Overview
This project is focused on understanding, exploring, and analyzing solar farm data from Benin, Sierra Leone, and Togo. The goal is to evaluate key environmental measurements and provide strategic recommendations for MoonLight Energy Solutions. The analysis will help identify high-potential regions for solar installation that align with the company's sustainability goals.

Table of Contents
    1 Project Overview
    2 Folder Structure
    3 Setup Instructions
    4 Steps and Sub-Steps Completed
    

Setup Instructions
   1 Clone the Repository:
        git clone https://github.com/your-username/solar-farm-analysis.git
        cd solar-farm-analysis

    2 Create and Activate a Virtual Environment:
        python3 -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    3 Install the Required Packages:
        pip install -r requirements.txt

    4 Run the Jupyter Notebooks:
         Navigate to the notebooks folder and open the respective notebook for each country to run the analysis.

************************************************************************************************

Steps and Sub-Steps Completed

1. Git and GitHub Setup
Environment Setup: Configured a Python environment with a virtual environment (venv).
Version Control: Set up a GitHub repository, created branches, and committed changes.
CI/CD: Added a basic CI/CD pipeline using GitHub Actions.

2. Data Understanding and Quality Check
Data Loading: Created reusable functions to load data for each country.
Data Quality Check:
Checked for missing values, outliers, and data types.
Identified outliers using Z-score analysis.

3. Summary Statistics
Statistical Analysis:
Calculated mean, median, standard deviation, and other summary statistics.
Interpreted results to understand data distribution.

4. Exploratory Data Analysis (EDA)
Time Series Analysis: Plotted time series graphs to identify trends and anomalies.
Correlation Analysis: Created heatmaps to visualize correlations between variables.
Wind Analysis: Used polar plots to analyze wind speed and direction.
Temperature and Humidity Analysis: Explored relationships between temperature and humidity.
Histograms: Visualized the distribution of key variables.
Z-Score Analysis: Identified significant deviations in key variables.
Bubble Charts: Explored complex relationships between multiple variables.

5. Data Cleaning (to be done)
Handle Missing Values: Decide on strategies for handling missing values.
Outlier Treatment: Apply methods to filter out outliers based on Z-scores or IQR.
Final Data Preparation: Ensure the dataset is clean and ready for further analysis.