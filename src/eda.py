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