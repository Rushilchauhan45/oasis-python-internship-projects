# 🌤️ GUI Weather App

A comprehensive desktop weather application built with Python and Tkinter that provides real-time weather information using the OpenWeatherMap API.

## ✨ Features

- **Modern GUI Interface** - Clean, intuitive design with modern styling
- **Real-time Weather Data** - Current weather conditions from OpenWeatherMap
- **Comprehensive Information** - Temperature, humidity, wind, pressure, and more
- **Weather Icons** - Visual weather representation with dynamic icons
- **Error Handling** - Robust error handling for network and API issues
- **Loading Indicators** - User-friendly loading states during API calls
- **Input Validation** - Smart validation for city names and user input
- **Responsive Design** - Clean layout that works on different screen sizes

## 🛠️ Technology Stack

- **Python 3.6+** - Core programming language
- **Tkinter** - GUI framework (built-in with Python)
- **Requests** - HTTP requests for API calls
- **Pillow (PIL)** - Image processing for weather icons
- **OpenWeatherMap API** - Weather data source

## 📦 Installation

### 1. Clone or Download Project
```bash
# Download all project files to a folder named 'weather-app'
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get API Key
1. Visit [OpenWeatherMap API](https://openweathermap.org/api)
2. Sign up for a free account
3. Get your API key from the dashboard

### 4. Configure API Key
1. Open `config.py` file
2. Replace `"your_api_key_here"` with your actual API key:
```python
API_KEY = "your_actual_api_key_here"
```

### 5. Run Application
```bash
python main.py
```

## 🚀 Usage

1. **Launch Application** - Run `python main.py`
2. **Enter City Name** - Type any city name in the input field
3. **Search Weather** - Click "Search" button or press Enter
4. **View Results** - Weather information will be displayed with icons
5. **Search Again** - Enter a new city name to get different weather data

## 📁 Project Structure

```
weather-app/
│
├── main.py                 # Main application entry point
├── config.py              # Configuration & API settings  
├── weather_api.py         # Weather API functions
├── gui_components.py      # GUI interface class
├── requirements.txt       # Required libraries
├── README.md             # Project documentation
│
└── assets/               # Assets folder
    └── icons/           # Weather icons (we'll download these)