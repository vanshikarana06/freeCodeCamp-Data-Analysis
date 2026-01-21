import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# 1. Import and Clean Data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
# Filter out the top 2.5% and bottom 2.5% outliers
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
    ]


def draw_line_plot():
    df_line = df.copy()
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_line.index, df_line['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Group and pivot for the bar chart
    df_pivot = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot = df_pivot[months]

    fig = df_pivot.plot(kind='bar', figsize=(15, 10), xlabel='Years', ylabel='Average Page Views').get_figure()
    plt.legend(title='Months')

    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    fig, axes = plt.subplots(1, 2, figsize=(20, 10))

    # Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0]).set(
        title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views'
    )

    # Month-wise Box Plot
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=month_order).set(
        title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views'
    )

    fig.savefig('box_plot.png')
    return fig