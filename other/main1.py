from typing import Union
from fastapi import FastAPI, HTTPException
# import exceptions
import json
import requests

app = FastAPI()
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.get("/")
def read_root():

    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):

#     return {"item_id": item_id, "q": q}


@app.get("/weather/{city}")
async def get_weather(city: str):

    API_KEY = "89ca44b042a300df0768d9ef96e6af9e"
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(weather_url)
    data = json.loads(response.text)
    if data["cod"] != "200": 
        raise HTTPException(status_code=404, detail="City not found")
    forecasts = data["list"]
    min_temp = []
    max_temp = []
    avg_temp = []
    humidity = []
    print(forecasts)
    for forecast in forecasts:
        if data.txt != " ":
            min_temp.append(forecast["main"]["temp_min"])
            max_temp.append(forecast["main"]["temp_max"])
            avg_temp.append(((min_temp+max_temp)/2, 2))
            humidity.append(forecast["main"]["humidity"])

    # forecasts = data["list"]
    # min_temp = forecasts["main"]["temp_min"]
    # max_temp = forecasts["main"]["temp_max"]
    # avg_temp = ((min_temp+max_temp)/2, 2)
    # humidity = forecasts["main"]["humidity"]

    avg_temp = ((min_temp+max_temp)/2, 2)

    return{
        "min temp:": min_temp,
        "max temp:": max_temp,
        "avg temp:": avg_temp,
        "humidity:": humidity
    }



