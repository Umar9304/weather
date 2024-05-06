import requests

API_KEY = "Bd5e378503939ddaee76f12ad7a97608"


def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    response = requests.get(url)

    data = response.json()

    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]["description"]
        temperature = main["temp"] - 273.15
        return f"In {city}, the weather is {weather} with a temperature of {temperature:.2f}°C."

    else:
        return f"Error: City not found."


city = input("Enter a city name: ")

weather_info = get_weather(city)

print(weather_info)
