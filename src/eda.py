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

#Correlation Analysis
def correlation_analysis(df):
    variables = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD']
    df_selected = df[variables]
    correlation_matrix = df_selected.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix: Solar Radiation, Temperature, and Wind Conditions')
    plt.show()
    # Pair plot for all selected variables
    sns.pairplot(df_selected, diag_kind='kde')
    plt.suptitle("Pair Plot: Solar Radiation, Temperature, and Wind Conditions", y=1.02)
    plt.show()
    # Scatter plots: Wind conditions vs Solar Irradiance
    wind_vars = ['WS', 'WSgust', 'WD']
    solar_vars = ['GHI', 'DNI', 'DHI']
    sns.pairplot(df, x_vars=wind_vars, y_vars=solar_vars, kind='scatter')
    plt.suptitle("Scatter Matrices: Wind Conditions vs Solar Irradiance", y=1.02)
    plt.show()







