import requests
from dotenv import load_dotenv
import os 
from dataclasses import dataclass

load_dotenv()
API_KEY = os.getenv('API_KEY')

@dataclass
class Weather:
      main:str
      description:str
      icon:str
      temp:float
      humidity:int
      pressure:int
      

def get_lat_lon(city_name, state_code, country_code,API_KEY):
    
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY}').json()
    data=response[0]
    lat,lon=data.get('lat'),data.get('lon')
    return lat,lon
    

def get_current_weather(lat,lon,API_KEY):
        
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric').json()
        data=Weather(
              main=response.get('weather')[0].get('main'),
              description=response.get('weather')[0].get('description'),
              icon=response.get('weather')[0].get('icon'),
              temp=response.get('main').get('temp'),
              humidity=response.get('main').get('humidity'),
              pressure=response.get('main').get('pressure')
                        
        )
        return data

def main(city_name,state_name,country_name):
    lat,lon=get_lat_lon(city_name,state_name,country_name,API_KEY)
    weather=get_current_weather(lat,lon,API_KEY)
    return weather

if __name__=="__main__":
      lat,lon=get_lat_lon("Los Angeles","CA","US",API_KEY)
      print(get_current_weather(lat,lon,API_KEY))
      
