import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # First line of best fit (All data)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'r', label='Best Fit Line 1')

    # Second line of best fit (From year 2000)
    new_df = df[df['Year'] >= 2000]
    res_recent = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series([i for i in range(2000, 2051)])
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    plt.plot(x_recent, y_recent, 'green', label='Best Fit Line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save and return for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()