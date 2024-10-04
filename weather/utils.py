# weather/utils.py
import requests

def get_weather(city_name):
    api_key = 'be36de72a0f3fe9a9ee4b370b9c299b7'  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    return response.json()

