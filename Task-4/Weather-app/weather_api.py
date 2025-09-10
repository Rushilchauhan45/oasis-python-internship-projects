# Weather API Handler


import requests
import json
from config import API_KEY, BASE_URL, UNITS, HTTP_SUCCESS, HTTP_NOT_FOUND, HTTP_UNAUTHORIZED

class WeatherAPI:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.units = UNITS
    
    def get_weather_data(self, city_name):
        """
        Fetch weather data for a given city
        Returns: tuple (success, data/error_message)
        """
        try:
            
            params = {
                'q': city_name,
                'appid': self.api_key,
                'units': self.units
            }
            
            
            response = requests.get(self.base_url, params=params, timeout=10)
            
            
            if response.status_code == HTTP_SUCCESS:
                data = response.json()
                return True, self.parse_weather_data(data)
            
            elif response.status_code == HTTP_NOT_FOUND:
                return False, "City not found! Please check the city name."
            
            elif response.status_code == HTTP_UNAUTHORIZED:
                return False, "Invalid API key! Please check your configuration."
            
            else:
                return False, f"API Error: {response.status_code}"
                
        except requests.exceptions.ConnectionError:
            return False, "No internet connection! Please check your network."
        
        except requests.exceptions.Timeout:
            return False, "Request timeout! Please try again."
        
        except requests.exceptions.RequestException as e:
            return False, f"Request error: {str(e)}"
        
        except json.JSONDecodeError:
            return False, "Invalid response from weather service."
        
        except Exception as e:
            return False, f"Unexpected error: {str(e)}"
    
    def parse_weather_data(self, raw_data):
        """
        Parse raw API response into readable format
        """
        try:
            parsed_data = {
                
                'city': raw_data['name'],
                'country': raw_data['sys']['country'],
                
                
                'temperature': round(raw_data['main']['temp']),
                'feels_like': round(raw_data['main']['feels_like']),
                'temp_min': round(raw_data['main']['temp_min']),
                'temp_max': round(raw_data['main']['temp_max']),
                
                
                'condition': raw_data['weather'][0]['main'],
                'description': raw_data['weather'][0]['description'].title(),
                'icon': raw_data['weather'][0]['icon'],
                
                
                'humidity': raw_data['main']['humidity'],
                'pressure': raw_data['main']['pressure'],
                'wind_speed': round(raw_data.get('wind', {}).get('speed', 0), 1),
                'wind_direction': raw_data.get('wind', {}).get('deg', 0),
                'clouds': raw_data.get('clouds', {}).get('all', 0),
                'visibility': raw_data.get('visibility', 0) / 1000,  
                
                
                'timezone': raw_data.get('timezone', 0),
                'sunrise': raw_data['sys']['sunrise'],
                'sunset': raw_data['sys']['sunset']
            }
            
            return parsed_data
            
        except KeyError as e:
            raise Exception(f"Missing data in API response: {e}")
        except Exception as e:
            raise Exception(f"Error parsing weather data: {e}")
    
    def get_weather_icon_url(self, icon_code):
        """
        Generate weather icon URL from icon code
        """
        return f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    
    def validate_api_key(self):
        """
        Check if API key is valid by making a test request
        """
        if not self.api_key or self.api_key == "your_api_key_here":
            return False, "Please set your API key in config.py"
        
        try:
            test_params = {
                'q': 'London',
                'appid': self.api_key,
                'units': self.units
            }
            
            response = requests.get(self.base_url, params=test_params, timeout=5)
            
            if response.status_code == HTTP_UNAUTHORIZED:
                return False, "Invalid API key!"
            
            return True, "API key is valid"
            
        except Exception:
            return False, "Unable to validate API key"


weather_api = WeatherAPI()