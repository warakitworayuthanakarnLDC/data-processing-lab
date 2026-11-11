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

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

print("All Cities in germany")
German_cities = []
for city in cities:
    if city["country"] == "Germany" :
        German_cities.append(city)

for city in German_cities:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C")
Spanish_city_over_12C = []

for city in cities:
    if city["country"] == "Spain" and float(city["temperature"]) > 12 :
        Spanish_city_over_12C.append(city)

for city in Spanish_city_over_12C:
    print(city)

print()
# Count the number of unique countries
print("Unique Countries")

countrylist = []
for country in cities:
    if country["country"] not in countrylist:
        countrylist.append(country["country"])
no=1
for country in countrylist:
    print(f"{no}. {country}")
    no+=1

print()
# Print the average temperature for all the cities in Germany
print("average temperature for all the cities in Germany")

gc_temp=[]
for city in German_cities:
    gc_temp.append(float(city["temperature"]))

print( ( sum(gc_temp) / len(gc_temp) ) )

print()
# Print the max temperature for all the cities in Italy

ic_temp = []
for city in cities:
    if city["country"] == "Italy" :
        ic_temp.append(float(city["temperature"]))
print("Max temp of all cities in italy")
print(max(ic_temp))
