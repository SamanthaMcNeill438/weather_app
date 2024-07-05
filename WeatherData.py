import WeatherDAL

class WeatherData:
    city : str
    min_temp : float
    max_temp : float
    avg_temp : float
    humidity : float

    def __init__(self, city, min_temp, max_temp, humidity):
        self.city = city
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.avg_temp = self.calc_average()
        self.humidity = humidity

    def __init__(self, city):
        self.city = city


    def calc_average(self):
        return round(((self.min_temp + self.max_temp)/2),2)
        
    
    def get_avg_temp(self):
        return self.avg_temp


    def check_if_exists(self, city, current_data):
        pre_result = self.search()
        
        if current_data == pre_result:
            return pre_result
        else:
            self.update(city, current_data)
            return current_data  
    

    # returns record
    def search(self):
        data = WeatherDAL(self.city)
        return data.search(self.city)
    

    def update_data(self, current_data):
        min_temp = current_data[min_temp]
        max_temp = current_data[max_temp]
        avg_temp = current_data[avg_temp]
        humidity = current_data[humidity]

        data = WeatherDAL(self.city, min_temp, max_temp, avg_temp, humidity)
        data.update_weather_data()