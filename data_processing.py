import csv, os #Imports csv parsing and operating system 

__location__ = os.path.realpath( #local variable location set to os.path.realpath
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        if isinstance(table, Table):
            self.table = list(table.table)
        else:
            self.table = list(table)

    def filter(self, condition):
        filtered_rows = [row for row in self.table if condition(row)]
        return Table(self.table_name, filtered_rows)

    def aggregate(self, arg1, arg2):
        if callable(arg1):
            aggregation_function, aggregation_key = arg1, arg2
        else:
            aggregation_key, aggregation_function = arg1, arg2

        values = []
        for item in self.table:
            val = item[aggregation_key]
            if isinstance(val, str):
                try:
                    val = float(val)
                except ValueError:
                    pass
            values.append(val)
        return aggregation_function(values)

    def __str__(self):
        return self.table_name + ':' + str(self.table)

    def __repr__(self):
        return self.table_name + ':' + str(self.table)

    def __len__(self):
        return len(self.table)

    def __iter__(self):
        return iter(self.table)

    def __getitem__(self, item):
        return self.table[item]


class DataLoader:
    def __init__(self, base_path=None):
        self.base_path = base_path if base_path is not None else __location__

    def load_csv(self, filename):
        file_path = filename if os.path.isabs(filename) else os.path.join(self.base_path, filename) if self.base_path else filename
        data = []
        with open(file_path, mode='r', encoding='utf-8') as f:
            rows = csv.DictReader(f)
            for r in rows:
                data.append(dict(r))
        table_name = os.path.splitext(os.path.basename(filename))[0]
        return Table(table_name, data)


def filter_items(condition, dict_list):
    if isinstance(dict_list, Table):
        return dict_list.filter(condition).table
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    if isinstance(dict_list, Table):
        return dict_list.aggregate(aggregation_key, aggregation_function)
    values = []
    for item in dict_list:
        val = item[aggregation_key]
        if isinstance(val, str):
            try:
                val = float(val)
            except ValueError:
                pass
        values.append(val)
    return aggregation_function(values)


loader = DataLoader()
cities = loader.load_csv('Cities.csv')

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = cities.aggregate('temperature', lambda temps: sum(temps)/len(temps))
print(temps)
print()

# Print all cities in Germany

print("All Cities in germany")
German_cities = cities.filter(lambda city: city["country"] == "Germany")

for city in German_cities:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C")
Spanish_city_over_12C = cities.filter(
    lambda city: city["country"] == "Spain" and float(city["temperature"]) > 12
)

for city in Spanish_city_over_12C:
    print(city)

print()
# Count the number of unique countries
print("Unique Countries")

countrylist = cities.aggregate('country', lambda countries: list(dict.fromkeys(countries)))
no=1
for country in countrylist:
    print(f"{no}. {country}")
    no+=1

print()
# Print the average temperature for all the cities in Germany
print("average temperature for all the cities in Germany")

gc_temp = German_cities.aggregate('temperature', lambda temps: sum(temps)/len(temps))
print(gc_temp)

print()
# Print the max temperature for all the cities in Italy

ic_temp = cities.filter(lambda city: city["country"] == "Italy").aggregate('temperature', max)
print("Max temp of all cities in italy")
print(ic_temp)
