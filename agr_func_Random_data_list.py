import csv

import pandas as pd

sd = pd.DataFrame()


class ReadCSVFile:

    def __init__(self, f_name):
        self.f_name = f_name

    def open_file(self):
        with open(self.f_name, 'r') as file:
            csv_reader = csv.reader(file, delimiter=';')
            next(csv_reader)
            rows = list(csv_reader)

        data_list = []

        for row in rows:
            data_list.append(row)
        return data_list

    def max_val_age(self):
        list_rows = self.open_file()
        list_for_max = [int(sublist[2]) for sublist in list_rows]
        max_val_age = max(list_for_max)
        return max_val_age

    def min_val_age(self):
        list_rows = self.open_file()
        list_for_max = [int(sublist[2]) for sublist in list_rows]
        min_val_age = min(list_for_max)
        return min_val_age

    def avg_val_age(self):
        list_rows = self.open_file()
        list_for_max = [int(sublist[2]) for sublist in list_rows]
        avg_val_age = sum(list_for_max) / len(list_for_max)
        return avg_val_age

    def for_pipline(self):
        data_list = pd.self.open_file()
        return data_list.dropna()




csv_file = ReadCSVFile('data.csv')
# read_csv = csv_file.open_file()

max_val = csv_file.max_val_age()
min_val = csv_file.min_val_age()
avg_val = csv_file.avg_val_age()

# print(csv_file.open_file())
print(max_val)
print(min_val)
print(avg_val)

# ['Kathryn;Atkins;21;Social worker;CLP;964983;Princeton']
