import glob
import matplotlib
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt

def get_data(data_path, selected_countries):
    files = glob.glob(f'{data_path}/*.csv')
    dataframes = []
    for file in files:
        df = pd.read_csv(file)
        country = df['Country'].iloc[0]
        if country in selected_countries:
            dataframes.append(df)
    return dataframes

def plot_boxplot(data):
    plt.figure(figsize=(10, 6))
    # sns.set_theme(style="whitegrid")
    # sns.set_context("talk", font_scale=1.4)
    sns.boxplot(x= 'Country', y='Carbon intensity gCO₂eq/kWh (direct)', data=data, palette='colorblind', hue='Country', legend=False)
    plt.xticks(rotation=45)
    plt.ylabel('gCO₂eq/kWh')
    plt.title('Carbon intensity')
    plt.tight_layout()
    plt.savefig('boxplot.pdf', dpi=300, bbox_inches='tight')

if __name__ == '__main__':
    matplotlib.rcParams.update({'axes.titlesize': 25})
    matplotlib.rcParams.update({'axes.labelsize': 25})
    matplotlib.rcParams.update({'xtick.labelsize': 25})
    matplotlib.rcParams.update({'ytick.labelsize': 25})
    data_path = 'data/electricitymaps'
    selected_countries = ['Italy', 'Germany', 'France', 'Austria', 'Belgium', 'Poland']
    data = get_data(data_path, selected_countries)
    data = pd.concat(data)
    plot_boxplot(data)