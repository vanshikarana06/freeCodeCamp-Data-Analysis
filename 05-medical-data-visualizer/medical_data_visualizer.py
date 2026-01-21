
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
df = pd.read_csv('medical_examination.csv')

# 2. Add overweight column
# BMI = weight (kg) / [height (m)]^2. If BMI > 25, value is 1, else 0.
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalize data
# 0 is good, 1 is bad. If value is 1 (normal) -> 0. If > 1 -> 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw Categorical Plot
def draw_cat_plot():
    # 5. Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and reformat data to split by cardio
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Draw the catplot
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig

    # 8. Return the figure
    fig.savefig('catplot.png')
    return fig

# 9. Draw Heat Map
def draw_heat_map():
    # 10. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 11. Calculate the correlation matrix
    corr = df_heat.corr()

    # 12. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 13. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 14. Plot the correlation matrix
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', square=True, center=0, vmin=-0.1, vmax=0.25, cbar_kws={'shrink': .5})

    # 15. Return the figure
    fig.savefig('heatmap.png')
    return fig