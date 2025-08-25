
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",index_col='date',parse_dates=["date"])

# Clean data
df_clean = df[(df['value']>=df['value'].quantile(0.025))& (df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
   
    fig, ax = plt.subplots(figsize=(10,5))
    sns.lineplot(data=df, x='date', y='value',color='brown', ax=ax)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df_clean.copy()
    df_bar['year']=df_bar.index.year
    df_bar['month']=df_bar.index.month
    
    df_grouped = df_bar.groupby(['year','month'])['value'].mean().unstack()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_grouped.columns = months
    
    # Draw bar plot
    fig = df_grouped.plot(kind='bar',figsize=(10,7),legend='Months').figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.tight_layout()
    plt.show()

    





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_num'] = [d.month for d in df_box.date]

    # Sort data to ensure month order is correct
    df_box = df_box.sort_values(by='month_num')

    # Define consistent month order
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn with color palettes)
    fig, axes = plt.subplots(1, 2, figsize=(20, 7))

    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0], palette='Set2',hue='year')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1],
                order=months_order, palette='Set3', hue='month')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Adjust layout and save
    plt.tight_layout()
    plt.show()
    



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
