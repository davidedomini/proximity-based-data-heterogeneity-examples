import glob
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt

def get_data(data_path):
    files = glob.glob(f'{data_path}/*.csv')
    data = {}
    for file in files:
        df = pd.read_csv(file)
        print(df)
        country = df['Country'].iloc[0]
        value = df['Carbon intensity gCO₂eq/kWh (direct)'].mean()
        data[country] = value
    return data

def plot_map(data):
   pass
    

if __name__ == '__main__':

    data_path = 'data/electricitymaps'
    data = get_data(data_path)
    plot_map(data)