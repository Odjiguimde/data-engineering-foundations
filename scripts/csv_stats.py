import csv
from statistics import mean


def read_ages_from_csv(file_name):
    """Read ages from CSV file."""
    ages = []

    with open(file_name, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            ages.append(int(row["age"]))

    return ages


def compute_statistics(values):
    """Compute min, max and average."""
    return min(values), max(values), mean(values)


def main():
    file_name = "data.csv"

    ages = read_ages_from_csv(file_name)
    minimum, maximum, average = compute_statistics(ages)

    print("Statistiques sur les âges")
    print("Min :", minimum)
    print("Max :", maximum)
    print("Moyenne :", average)


main()
