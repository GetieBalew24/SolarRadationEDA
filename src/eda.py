# EDA analysis for solar radiation data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load data 
def load_data(filepath):
    return pd.read_csv(filepath, parse_dates=['Timestamp'])

# Summary Statistics
# Summary Statistics
def summary_statistics(df):
    return df.describe()

# Data Quality Check:
def data_quality_check(df):
    missing_values = df.isnull().sum() 
    negative_values = df[['GHI', 'DNI', 'DHI']][(df['GHI'] < 0) | (df['DNI'] < 0) | (df['DHI'] < 0)] 
    return missing_values, negative_values 


# Time Series Analysis

def time_series_analysis(df):
    plt.figure(figsize=(15, 8))
    plt.plot(df['Timestamp'], df['GHI'], label='GHI')
    plt.plot(df['Timestamp'], df['DNI'], label='DNI')
    plt.plot(df['Timestamp'], df['DHI'], label='DHI')
    plt.plot(df['Timestamp'], df['Tamb'], label='Tamb')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title('Time Series Analysis')
    plt.show()






