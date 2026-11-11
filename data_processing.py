import csv, os #Imports csv parsing and operating system 

__location__ = os.path.realpath( #local variable location set to os.path.realpath
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)


def filter_items(condition, dict_list):
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
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


# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = aggregate("temperature", lambda temps: sum(temps)/len(temps), cities)
print(temps)
print()

# Print all cities in Germany

print("All Cities in germany")
German_cities = filter_items(lambda city: city["country"] == "Germany", cities)

for city in German_cities:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C")
Spanish_city_over_12C = filter_items(
    lambda city: city["country"] == "Spain" and float(city["temperature"]) > 12,
    cities
)

for city in Spanish_city_over_12C:
    print(city)

print()
# Count the number of unique countries
print("Unique Countries")

countrylist = aggregate("country", lambda countries: list(dict.fromkeys(countries)), cities)
no=1
for country in countrylist:
    print(f"{no}. {country}")
    no+=1

print()
# Print the average temperature for all the cities in Germany
print("average temperature for all the cities in Germany")

gc_temp = aggregate("temperature", lambda temps: sum(temps)/len(temps), German_cities)
print(gc_temp)

print()
# Print the max temperature for all the cities in Italy

ic_temp = aggregate("temperature", max, filter_items(lambda city: city["country"] == "Italy", cities))
print("Max temp of all cities in italy")
print(ic_temp)
