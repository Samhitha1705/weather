import requests

API_KEY = "76b0443d5e257a282e1eaae876528cf7"

CITY = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    print("\nWeather Report")
    print("----------------------")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["main"])
    print("Humidity:", data["main"]["humidity"], "%")

    # ✅ ADD THIS HERE (LOGGING PART)
    with open("weather_log.txt", "a") as f:
        f.write(f"{data['name']} | {data['main']['temp']}°C | {data['weather'][0]['main']} | {data['main']['humidity']}%\n")

else:
    print("Error:", data["message"])



