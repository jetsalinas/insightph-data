import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def generate_bar_chart_poverty():
    poverty = pd.read_csv("finished/poverty-incidence-processed.csv")

    sns.set_style("darkgrid")
    f, ax = plt.subplots(figsize=(6, 30))
    sns.barplot(x="'2015'", y="'Location'", data=poverty, label="Poverty incidence per population", color="b")
    plt.tight_layout()
    plt.savefig("finished/poverty-incidence.png")

if __name__ == "__main__":
    generate_bar_chart_poverty()