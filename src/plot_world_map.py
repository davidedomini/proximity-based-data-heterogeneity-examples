import glob
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt

def get_data_by_country(data_path):
    files = glob.glob(f'{data_path}/*.csv')
    data = {
        'country': [],
        'Carbon intensity gCO₂eq/kWh (direct)': []
    }
    for file in files:
        df = pd.read_csv(file)
        country = df['Country'].iloc[0]
        if 'Bosnia' in country:
            country = 'Bosnia and Herz.'
        data['country'].append(country)
        data['Carbon intensity gCO₂eq/kWh (direct)'].append(df['Carbon intensity gCO₂eq/kWh (direct)'].mean())
    return pd.DataFrame(data)

def plot_map(data):
    world = gpd.read_file('data/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
    print(world['NAME'].sort_values().unique())
    merged = world.merge(data, how='left', left_on='NAME', right_on='country')
    merged = merged[merged['Carbon intensity gCO₂eq/kWh (direct)'].notnull()]
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    world.boundary.plot(ax=ax, linewidth=0.5, color='gray')  # bordi del mondo
    merged.plot(column='Carbon intensity gCO₂eq/kWh (direct)', ax=ax, legend=True, cmap='RdYlGn_r', edgecolor='black')
    ax.set_xlim([-15, 30])  # longitudes
    ax.set_ylim([35, 60])   # latitude
    plt.savefig('world_map.pdf', dpi=300)

if __name__ == '__main__':

    data_path = 'data/electricitymaps'
    data = get_data_by_country(data_path)
    plot_map(data)