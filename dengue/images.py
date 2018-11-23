import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def generate_heatmap_dengue(year):
    dengue_long = pd.read_csv("denguecases.csv")
    dengue_long = dengue_long.loc[dengue_long.Year == year]
    dengue_long.Month = pd.to_datetime(dengue_long.Month, format='%b', errors='coerce').dt.month
    dengue = dengue_long.pivot("Month", "Region", "Dengue_Cases")

    # order dataframe by months
    months = ['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']
    dengue.index = pd.Series([months[i-1] for i in dengue.index])

    # order dataframes by region
    cols = dengue.columns.tolist()
    regions = ['CAR', 'CARAGA', 'NCR', 'Region.I', 'Region.II', 'Region.III', 'Region.IV.A', 'Region.IV.B', 'Region.V', 'Region.VI', 'Region.VII', 'Region.VIII', 'Region.IX', 'Region.X', 'Region.XI', 'Region.XII', 'ARMM']
    dengue= dengue[regions]

    print(dengue.max())

    f, ax = plt.subplots(figsize=(18, 12))
    sns.heatmap(dengue, vmin=0, vmax=75, annot=True, linewidths=.5, ax=ax)
    plt.title("Dengue cases per 100,000 population in the Philippines ({})".format(year))
    plt.xlabel("Region")
    plt.ylabel("Month")
    plt.savefig("finished/dengue-{}.png".format(year))

if __name__ == "__main__":
    for i in range(2008, 2017):
        generate_heatmap_dengue(i)