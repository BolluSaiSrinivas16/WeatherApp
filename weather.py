import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        temp = main["temp"]
        feels_like = main["feels_like"]
        humidity = main["humidity"]
        description = data["weather"][0]["description"]
        
        print(f"\nWeather in {city}:\n")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"🤗 Feels Like: {feels_like}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️ Description: {description.capitalize()}")
    else:
        print("\n⚠️ City not found. Please try again.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
