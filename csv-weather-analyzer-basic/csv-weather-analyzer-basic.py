import csv
with open("weather-data.csv") as data_file:
    data  = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(f"{row}")
        if row[1] == "temp":
            continue
        temperatures.append(int(row[1]))
    print(temperatures)