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
