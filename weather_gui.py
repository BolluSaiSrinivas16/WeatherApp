import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv

# Load the API key
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        result_text.set(
            f"🌡️ Temperature: {temp}°C\n"
            f"🤗 Feels Like: {feels_like}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"☁️ Description: {description.capitalize()}"
        )
    else:
        result_text.set("⚠️ City not found. Please try again.")

# Setup GUI window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

# Input field
city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=20)

# Button
get_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_button.pack()

# Result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), justify="left", padx=10, pady=10)
result_label.pack(pady=10)

# Start app
root.mainloop()
