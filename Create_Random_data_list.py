from faker import Faker
import csv

fake = Faker()

data = []

for _ in range(1000000):
    row = [
        fake.first_name(),
        fake.last_name(),
        fake.random_int(min = 18, max = 30),
        fake.job(),
        fake.currency_code(),
        fake.random_int(min = 100, max = 1000000),
        fake.city()
    ]
    data.append(row)

filename = "data.csv"
with open(filename, "w", newline="") as file:
    writer = csv.writer(file, delimiter = ';')
    writer.writerow(["first_name", "last_name", "Age", "Job", "currence", "money", "city"])  # Запись заголовка колонок
    writer.writerows(data)  # Запись данных
