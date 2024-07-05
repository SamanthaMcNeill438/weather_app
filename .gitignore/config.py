API_KEY = 'b6385e81354e4ec6ed7e9b822f7167df'

def get_API_KEY():
    return API_KEY

def get_units():
    return "metric"

def get_params(city):
    params = {
        "q": city,
        "units": get_units(),  
        "appid": get_API_KEY()
    }