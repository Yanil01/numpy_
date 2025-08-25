import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('medical_examination.csv')

BMI = df['weight']/((df['height']/100)**2) # BMI = weight(kg) / height(m)^2
df['overweight'] = (BMI > 25).astype(int) # 0 if BMI <= 25 else 1

df['cholesterol'] = (df['cholesterol'] > 1).astype(int) # 0 if cholesterol == 1 else 1
df['gluc'] = (df['gluc'] > 1).astype(int) # 0 if gluc == 1 else 1

def draw_cat_plot():
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
    
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig
    
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]  # Clean the data
    
    corr = df_heat.corr() # Calculate the correlation matrix
    
    mask = np.triu(np.ones_like(corr, dtype=bool)) # Generate a mask for the upper triangle
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

    fig.savefig('heatmap.png')
    return fig