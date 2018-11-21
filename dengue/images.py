import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def generate_heatmap_dengue():
    dengue_long = pd.read_csv("denguecases.csv")
    dengue_long = dengue_long.loc[dengue_long.Year == 2016]
    dengue_long.Month = pd.to_datetime(dengue_long.Month, format='%b', errors='coerce').dt.month
    dengue = dengue_long.pivot("Month", "Region", "Dengue_Cases")
    months = ['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']
    dengue.index = pd.Series([months[i-1] for i in dengue.index])
    dengue.sort_index()
    print(dengue.head())


    f, ax = plt.subplots(figsize=(18, 12))
    sns.heatmap(dengue, annot=True, linewidths=.5, ax=ax)
    plt.title("Dengue cases per 100,000 population in the Philippines (2016)")
    plt.xlabel("Region")
    plt.ylabel("Month")
    plt.savefig("finished/dengue.png")

if __name__ == "__main__":
    generate_heatmap_dengue()