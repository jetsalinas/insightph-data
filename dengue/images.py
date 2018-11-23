import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas as gpd

def generate_heatmap_dengue(year):
    mpl.style.use("seaborn")

    dengue_long = pd.read_csv("denguecases.csv")
    dengue_long = dengue_long.loc[dengue_long.Year == year]
    dengue_long.Month = pd.to_datetime(dengue_long.Month, format='%b', errors='coerce').dt.month
    dengue = dengue_long.pivot("Month", "Region", "Dengue_Cases")

    # order dataframe by months
    months = ['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']
    dengue.index = pd.Series([months[i-1] for i in dengue.index])

    # order dataframes by region
    cols = dengue.columns.tolist()
    regions = ['CAR', 'CARAGA', 'NCR', 'Region I', 'Region II', 'Region III', 'Region IV-A', 'Region IV-B', 'Region V', 'Region VI', 'Region VII', 'Region VIII', 'Region IX', 'Region X', 'Region XI', 'Region XII', 'ARMM']
    dengue = dengue[regions]

    f, ax = plt.subplots(figsize=(18, 12))
    sns.heatmap(dengue, vmin=0, vmax=80, annot=True, linewidths=.5, ax=ax)
    plt.title("Dengue cases per 100,000 population in the Philippines ({})".format(year))
    plt.xlabel("Region")
    plt.ylabel("Month")
    plt.savefig("finished/heatmap/dengue-{}.png".format(year))
    plt.close()

def generate_cloropleth_dengue(year):
    mpl.style.use("seaborn")
    
    dengue = pd.read_csv("denguecases.csv")

    dengue = pd.read_csv("denguecases.csv")
    dengue = dengue.loc[dengue.Year == year]

    phl_url = "../geo/ph-regions.geojson"
    philippines = gpd.read_file(phl_url)
    
    regions = ['CAR', 'CARAGA', 'NCR', 'Region I', 'Region II', 'Region III', 'Region IV-A', 'Region IV-B', 'Region V', 'Region VI', 'Region VII', 'Region VIII', 'Region IX', 'Region X', 'Region XI', 'Region XII', 'ARMM']
    geometry_data = []
    for index, row in dengue.iterrows():
        geometry_query = philippines.loc[philippines.NAME == row.Region.upper()].geometry.iloc[0]
        geometry_data.append(geometry_query)
    dengue["geometry"] = pd.Series(geometry_data, index=dengue.index)
    
    map_plot = gpd.GeoDataFrame(pd.DataFrame().append(dengue))

    months = ['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']

    for i in range(len(months)):
        map_plot_month = gpd.GeoDataFrame(map_plot.loc[map_plot.Month == months[i]])
        ax = map_plot_month.plot(figsize=(10, 10), alpha=0.5, cmap="gist_heat", column="Dengue_Cases", legend=True, vmin=0, vmax=80)
        plt.title("Dengue cases per 100,000 population in the Philippines ({} {})".format(months[i], year))
        plt.axis("off")
        plt.savefig("finished/geo/dengue-{}-{}.png".format(year, i))
        plt.close()

if __name__ == "__main__":
    for i in range(2008, 2017):
        generate_heatmap_dengue(i)
        generate_cloropleth_dengue(i)
        print("Finished {} iteration(s)".format(i))