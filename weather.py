import requests
import os

API_KEY = "76b0443d5e257a282e1eaae876528cf7"

CITY = os.getenv("CITY", "Bangalore")

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print("\nWeather Report")
print("----------------------")

if data["cod"] == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["main"])
    print("Humidity:", data["main"]["humidity"], "%")
else:
    print("Error:", data["message"])


