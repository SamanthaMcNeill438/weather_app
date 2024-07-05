class WeatherData:
    #city: str
    min_temp = 0
    max_temp = 0
    avg_temp = 0
    humidity = 0

    def __init__(self, min_temp, max_temp, humidity):
        #self.city = city
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.avg_temp = round(((min_temp + max_temp)/2),2)
        self.humidity = humidity
    

    def get_weather_data(self):
        #     """
        # Extracts the weather data from the API response.

        # Args:
        #     weather_data (dict): The API response data.

        # Returns:
        #     dict: A dictionary with keys "min temp:", "max temp:", "avg temp:", and "humidity:".

        # Example:
        #     >>> weather_data = {"main": {"temp_min": 10, "temp_max": 20, "humidity": 60}}
        #     >>> get_data(weather_data)
        #     {"min temp:": 10, "max temp:": 20, "avg temp:": 15.0, "humidity:": 60}
        # """
        return {
            "min temp:": self.min_temp,
            "max temp:": self.max_temp,
            "avg temp:": self.avg_temp,
            "humidity:": self.humidity
        }


    