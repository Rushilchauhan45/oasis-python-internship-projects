# Weather App Configuration File



API_KEY = "your_api_key_here"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
ICON_BASE_URL = "http://openweathermap.org/img/wn/"

# App Settings
APP_TITLE = "Weather App"
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 600
UNITS = "metric"  

COLORS = {
    "primary": "#2E86AB",
    "secondary": "#A23B72", 
    "background": "#F18F01",
    "text": "#FFFFFF",
    "accent": "#C73E1D",
    "light_bg": "#E8F4FD",
    "dark_text": "#2C3E50"
}


FONTS = {
    "title": ("Arial", 18, "bold"),
    "heading": ("Arial", 14, "bold"), 
    "normal": ("Arial", 12),
    "small": ("Arial", 10)
}


HTTP_SUCCESS = 200
HTTP_NOT_FOUND = 404
HTTP_UNAUTHORIZED = 401