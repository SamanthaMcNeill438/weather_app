import pytest
import unittest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
import main
import requests
import config


client = TestClient(app)


# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}


# # @pytest.fixture
# # def weather_fixture():
# #     city = "Belfast"


# def test_get_weather(weather_fixture):
#     city = "Belfast"
#     response = client.get("/weather/{city}")
#     assert response.status_code == 200
#     {
#         # "min temp:": main.WeatherData.min_temp,
#         # "max temp:": main.WeatherData.max_temp,
#         # "avg temp:": main.WeatherData.avg_temp,
#         # "humidity:": main.WeatherData.humidity
#         "min temp:": main.data.min_temp,
#         "max temp:": main.data.max_temp,
#         "avg temp:": main.data.avg_temp,
#         "humidity:": main.data.humidity
#     }

# def test_weather_class():
#     data: object
#     data = main.WeatherData(10,20,44)
#     response = data.get_weather_data()
#     assert response == {
#             "min temp:": 10,
#             "max temp:": 20,
#             "avg temp:": 15.00,
#             "humidity:": 44 }
    

# def test_link():
#     API_KEY = config.get_API_KEY()
#     units = config.get_units()
#     city = "London"  # Replace with the desired city
#     base_url = "https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": city,
#         "units": units,  
#         "appid": API_KEY
#     }

#     response = requests.get(base_url, params=params)
#     assert response.status_code == 200  # Check if the response was successful

#     # weather_data = response.json()  # Use the response.json() method to parse the JSON response
#     # Do something with the weather_data


def test_get_weather():
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": 'Belfast',
        "units": config.get_units(),  
        "appid": config.get_API_KEY()
    }
    response = requests.get(base_url, params=params)
    assert response.status_code == 200
    assert response.json()["main"]["humidity"] == 62