import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 404:
            print("City not found. Please check the city name.")
            return

        if response.status_code != 200:
            print("Unable to get weather information.")
            return

        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n========== WEATHER INFORMATION ==========")
        print(f"City          : {city_name}, {country}")
        print(f"Temperature   : {temperature} °C")
        print(f"Feels Like    : {feels_like} °C")
        print(f"Weather       : {description.title()}")
        print(f"Humidity      : {humidity}%")
        print(f"Wind Speed    : {wind_speed} m/s")
        print("=========================================")

    except requests.exceptions.ConnectionError:
        print("Internet connection error.")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except Exception as error:
        print("An unexpected error occurred:", error)


print("========================================")
print("          BASIC WEATHER APP")
print("========================================")

while True:
    city = input("\nEnter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        continue

    get_weather(city)

    again = input("\nCheck another city? (y/n): ").lower()

    if again != "y":
        print("\nThank you for using the Weather App!")
        break