import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
import main

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_get_weather():
    city = "Belfast"
    response = client.get("/weather/{city}")
    assert response.status_code == 200
    {
        # "min temp:": main.WeatherData.min_temp,
        # "max temp:": main.WeatherData.max_temp,
        # "avg temp:": main.WeatherData.avg_temp,
        # "humidity:": main.WeatherData.humidity
        "min temp:": main.data.min_temp,
        "max temp:": main.data.max_temp,
        "avg temp:": main.data.avg_temp,
        "humidity:": main.data.humidity
    }

def test_weather_class():
    data: object
    data = main.WeatherData(10,20,44)
    response = data.get_weather_data()
    assert response == {
            "min temp:": 10,
            "max temp:": 20,
            "avg temp:": 15.00,
            "humidity:": 44
        }
    
test_weather_class()
