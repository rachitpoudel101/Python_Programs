import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def fetch_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == "200":  # Successful response
        print("Weather Forecast for", data["city"]["name"])
        forecasts = data["list"]
        for forecast in forecasts:
            date_time = datetime.strptime(forecast["dt_txt"], "%Y-%m-%d %H:%M:%S")
            temperature = forecast["main"]["temp"]
            weather_desc = forecast["weather"][0]["description"]
            print(f"Date/Time: {date_time}, Weather: {weather_desc}, Temperature: {temperature}°C")
    else:
        print("Error fetching weather data. Please check the city name and try again.")

def plot_temperature_trend(data):
    timestamps = []
    temperatures = []
    forecasts = data["list"]
    for forecast in forecasts:
        timestamps.append(datetime.strptime(forecast["dt_txt"], "%Y-%m-%d %H:%M:%S"))
        temperatures.append(forecast["main"]["temp"])
    
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temperatures, marker='o', linestyle='-')
    plt.title('Temperature Trend')
    plt.xlabel('Date/Time')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    city = input("Enter city name: ")
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    weather_data = fetch_weather(city, api_key)
    display_weather(weather_data)
    plot_temperature_trend(weather_data)

if __name__ == "__main__":
    main()
