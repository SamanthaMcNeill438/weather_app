from typing import Union
from fastapi import FastAPI, HTTPException
import json
import requests

app = FastAPI()
API_KEY = 'b6385e81354e4ec6ed7e9b822f7167df'
#base_url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/weather/{city}")
async def get_weather(city: str):
    #base_url = 'https://api.openweathermap.org/data/2.5/weather?q=Belfast&appid=b6385e81354e4ec6ed7e9b822f7167df'
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "units": "metric",  
        "appid": API_KEY

    }
    
    #response = requests.get(base_url)
    response = requests.get(base_url, params)
    print(response)

    weather_data = json.loads(response.text)
    print(weather_data)

    if weather_data["cod"] != "200": 
        #raise HTTPException(status_code=404, detail="City not found")
        print("stopped working")
    return get_data(weather_data)
    # #forecasts = weather_data["list"]
    # min_temp = []
    # max_temp = []
    # avg_temp = []
    # humidity = []
    # print(forecasts)
    # for forecast in forecasts:
    #     print(forecast["main"]["temp_min"])
    #     if weather_data.txt != " ":
    #         min_temp.append(forecast["main"]["temp_min"])
    #         max_temp.append(forecast["main"]["temp_max"])
    #         avg_temp.append(((min_temp+max_temp)/2, 2))
    #         humidity.append(forecast["main"]["humidity"])
    #         #return_details(min_temp,max_temp,avg_temp,humidity)
    # return {
    #     "min temp:": min_temp,
    #     "max temp:": max_temp,
    #     "avg temp:": avg_temp,
    #     "humidity:": humidity
    # }
    

def get_data(weather_data):
    min_temp = weather_data["main"]["temp_min"]
    max_temp = weather_data["main"]["temp_max"]
    avg_temp = ((min_temp + max_temp)/2)
    humidity = weather_data["main"]["humidity"]
    
    return {
        "min temp:": min_temp,
        "max temp:": max_temp,
        "avg temp:": avg_temp,
        "humidity:": humidity
    }

    
