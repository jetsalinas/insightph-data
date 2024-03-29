import csv

def preprocess_file():
    data_names = ["Poverty Incidence among Population", "Magnitude of Poor Population"]
    data_poverty_incidence = []
    data_mangnitude_poor = []
    header = None

    with open("poverty-incidence-per-region-psa.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = csv_reader.__next__()

        for i in range(len(header)):
            header[i] = "'{}'".format(header[i])

        for row in csv_reader:
            if row[0] == data_names[0]:
                data_poverty_incidence.append(list(row))
            elif row[0] == data_names[1]:
                data_mangnitude_poor.append(list(row))

    with open("finished/poverty-incidence-processed.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        for row in data_poverty_incidence:
            csv_writer.writerow(row)
    
    with open("finished/magnitude-poor-processed.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        for row in data_mangnitude_poor:
            csv_writer.writerow(row)

if __name__ == "__main__":
    preprocess_file()