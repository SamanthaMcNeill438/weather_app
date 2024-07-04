from fastapi import FastAPI, HTTPException
import requests
import json

app = FastAPI()

@app.get("/weather/{city}/{day}")
async def get_weather(city: str, day: int):
    api_key = "89ca44b042a300df0768d9ef96e6af9e"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    if data["cod"] != "200":
        raise HTTPException(status_code=404, detail="City not found")
    forecasts = data["list"]
    min_temp = []
    max_temp = []
    humidity = []
    for forecast in forecasts:
        if forecast["dt_txt"].split(" ")[0] == day:
            min_temp.append(forecast["main"]["temp_min"])
            max_temp.append(forecast["main"]["temp_max"])
            humidity.append(forecast["main"]["humidity"])
    min_avg = sum(min_temp) / len(min_temp)
    max_avg = sum(max_temp) / len(max_temp)
    return {
        "city": city,
        "day": day,
        "min_temp": min(min_temp),
        "max_temp": max(max_temp),
        "avg_temp": (min_avg + max_avg) / 2,
        "humidity": sum(humidity) / len(humidity)
    }