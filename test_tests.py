import pytest
import unittest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
import main
import requests
import config

class MyTestCase(unittest.TestCase):

    def test_read_main(self):
        client = TestClient(app)
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}


    def test_link(self):
        API_KEY = config.get_API_KEY()
        units = config.get_units()
        city = "Belfast"  # Replace with the desired city
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "units": units,  
            "appid": API_KEY
        }

        response = requests.get(base_url, params=params)
        assert response.status_code == 200  # Check if the response was successful

        # weather_data = response.json()  # Use the response.json() method to parse the JSON response
        # Do something with the weather_data


    def test_get_weather_data(self):
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": 'Belfast',
            "units": config.get_units(),  
            "appid": config.get_API_KEY()
        }
        response = requests.get(base_url, params=params)
        assert response.status_code == 200
        # assert response.json()["main"]["humidity"] == 62

        assert 40 < response.json()["main"]["humidity"] < 80
        assert response.json()["main"]["temp_min"] < 80
        assert response.json()["main"]["temp_max"] < 80
        assert response.json()["main"]["temp"] < 80


# def test_get_weather_success(monkeypatch):
#     client = TestClient(app)
#     class MockResponse:
#         @staticmethod
#         def json():
#             return {
#                 "cod": "200",
#                 "main": {
#                     "temp_min": 15.0,
#                     "temp_max": 25.0,
#                     "humidity": 80
#                 }
#             }

#     def mock_get(*args, **kwargs):
#         return MockResponse()

#     monkeypatch.setattr("requests.get", mock_get)
#     response = client.get("/weather/London")
#     assert response.status_code == 200
#     assert response.json() == {
#         "min temp:": 15.0,
#         "max temp:": 25.0,
#         "avg temp:": 20.0,
#         "humidity:": 80
#     }

#     def test_get_data():
#         weather_data = {
#             "main": {
#                 "temp_min": 10.0,
#                 "temp_max": 20.0,
#                 "humidity": 70
#             }
#         }
#         expected_result = {
#             "min temp:": 10.0,
#             "max temp:": 20.0,
#             "avg temp:": 15.0,
#             "humidity:": 70
#         }
#         assert get_data(weather_data) == expected_result