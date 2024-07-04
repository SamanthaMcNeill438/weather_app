#gets the min, max and avg temp and humidity for a user specified city

from typing import Union
from fastapi import FastAPI, HTTPException
import json
import requests

app = FastAPI()
API_KEY = 'b6385e81354e4ec6ed7e9b822f7167df'


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/weather/{city}")
async def get_weather(city: str):
    base_url = "api.openweathermap.org/data/2.5/forecast/daily?"
    params = {
        "q": city,
        #"units": "metric",  
        "cnt": 1,
        "appid": API_KEY
    }

    response = requests.get(base_url, params)
    print(response)

    weather_data = json.loads(response.text)
    print(weather_data)

    if weather_data["cod"] != "200": 
        HTTPException(status_code=weather_data, detail='An error occured')
        print("stopped working")
    return get_data(weather_data)
    

def get_data(weather_data):
    min_temp = weather_data["main"]["temp_min"]
    max_temp = weather_data["main"]["temp_max"]
    avg_temp = round(((min_temp + max_temp)/2),2)
    humidity = weather_data["main"]["humidity"]
    
    return {
        "min temp:": min_temp,
        "max temp:": max_temp,
        "avg temp:": avg_temp,
        "humidity:": humidity
    }

    
