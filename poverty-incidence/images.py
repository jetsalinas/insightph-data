import seaborn as sns
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

def generate_bar_chart_poverty():
    poverty = pd.read_csv("finished/poverty-incidence-processed.csv")

    sns.set_style("darkgrid")
    f, ax = plt.subplots(figsize=(6, 30))
    sns.barplot(x="'2015'", y="'Location'", data=poverty, label="Poverty incidence per population", color="b")
    plt.tight_layout()
    plt.savefig("finished/poverty-incidence.png")

def generate_cloropleth_poverty(year):
    # load datasets
    poverty = pd.read_csv("finished/poverty-incidence-processed.csv")
    phl_url = "../geo/ph-provinces.geojson"
    philippines = gpd.read_file(phl_url)

    # preprocess data
    poverty_provinces = pd.DataFrame()
    poverty_incidence_provinces = []
    geometry_provinces = []
    name_query = []
    for index, row in poverty.iterrows():
        if row["'Location'"] in philippines.PROVINCE.tolist():
            poverty_query = poverty.loc[poverty["'Location'"] == row["'Location'"]]["'{}'".format(year)].iloc[0]
            poverty_incidence_provinces.append(poverty_query)
            geometry_query = philippines.loc[philippines.PROVINCE == row["'Location'"]]["geometry"].iloc[0]
            geometry_provinces.append(geometry_query)
            name_query.append(row["'Location'"])
    poverty_provinces["name"] = pd.Series(name_query)
    poverty_provinces["poverty_incidence"] = pd.Series(poverty_incidence_provinces)
    poverty_provinces["geometry"] = pd.Series(geometry_provinces)
    
    # print(set(philippines.PROVINCE.tolist()) - set(poverty_provinces["name"].tolist()) )
    # Not shown: {'Eastern Samar', 'Shariff Kabunsuan', 'Dinagat Islands'}
    
    # plot and save image
    map_plot = gpd.GeoDataFrame(poverty_provinces)
    ax = map_plot.plot(figsize=(10, 10), alpha=0.5, cmap="Oranges", column="poverty_incidence", legend=True, vmin=0, vmax=80)
    plt.title("Poverty incidence in the Philippines per province({})".format(year))
    plt.axis("off")
    plt.savefig("finished/geo/poverty-{}.png".format(year))
    plt.close()

if __name__ == "__main__":
    generate_bar_chart_poverty()
    generate_cloropleth_poverty(2006)
    generate_cloropleth_poverty(2009)
    generate_cloropleth_poverty(2012)
    generate_cloropleth_poverty(2015)