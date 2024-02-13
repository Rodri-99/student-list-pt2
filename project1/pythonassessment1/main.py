def get_weather(cities):
    weather = {}
    for city in cities:
        temperature = int(input(f"What is the current temperature in {city}? "))
        weather[city] = temperature
    return weather

def print_weather(weather):
    for city, temperature in weather.items():
        print(f"{city} has temperature {temperature}.")

def calc_avg_temp(weather):
    total_temp = sum(weather.values())
    avg_temp = total_temp / len(weather)
    return avg_temp

cities = []
num_cities = int(input("How many cities? "))
for _ in range(num_cities):
    city = input("Please enter a city name: ")
    cities.append(city)

all_weather = get_weather(cities)
print_weather(all_weather)

avg_temp = calc_avg_temp(all_weather)
print(f"Average temperature: {avg_temp}")