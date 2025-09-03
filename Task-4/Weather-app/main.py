#!/usr/bin/env python3
"""
Weather App - Main Application
==============================

A comprehensive GUI weather application that provides real-time weather
information using OpenWeatherMap API.

Author: Rushil Chauhan
Date: 03-09-25
Version: 1.0

Requirements:
- Python 3.6+
- tkinter (usually comes with Python)
- requests
- Pillow (PIL)

Setup Instructions:
1. Get free API key from openweathermap.org
2. Replace API_KEY in config.py
3. Install required packages: pip install requests pillow
4. Run: python main.py
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox

def check_dependencies():
    """Check if all required packages are installed"""
    missing_packages = []
    
    try:
        import requests
    except ImportError:
        missing_packages.append("requests")
    
    try:
        from PIL import Image, ImageTk
    except ImportError:
        missing_packages.append("Pillow")
    
    if missing_packages:
        error_msg = f"""Missing required packages: {', '.join(missing_packages)}

Please install them using:
pip install {' '.join(missing_packages)}

Then restart the application."""
        
        # Show error in GUI if possible, otherwise print
        try:
            root = tk.Tk()
            root.withdraw()  # Hide main window
            messagebox.showerror("Missing Dependencies", error_msg)
            root.destroy()
        except:
            print(error_msg)
        
        return False
    
    return True

def check_config():
    """Check if configuration is properly set up"""
    try:
        from config import API_KEY
        
        if not API_KEY or API_KEY == "your_api_key_here":
            error_msg = """API Key not configured!

Please follow these steps:
1. Visit: https://openweathermap.org/api
2. Sign up for a free account
3. Get your API key
4. Open config.py file
5. Replace 'your_api_key_here' with your actual API key
6. Save the file and restart the application

Example:
API_KEY = "your_actual_api_key_here" """
            
            # Show error in GUI
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Configuration Error", error_msg)
            root.destroy()
            return False
        
        return True
        
    except ImportError:
        print("Error: config.py file not found!")
        return False

def main():
    """Main application entry point"""
    print("Starting Weather App...")
    print("=" * 50)
    
    # Check dependencies
    print("Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    print("✓ All dependencies found")
    
    # Check configuration
    print("Checking configuration...")
    if not check_config():
        sys.exit(1)
    print("✓ Configuration valid")
    
    # Import and run application
    try:
        print("Loading application...")
        from gui_components import WeatherApp
        
        print("✓ Application loaded successfully")
        print("Starting GUI...")
        print("=" * 50)
        
        # Create and run app
        app = WeatherApp()
        app.run()
        
    except ImportError as e:
        error_msg = f"Error importing application modules: {e}"
        print(error_msg)
        messagebox.showerror("Import Error", error_msg)
        sys.exit(1)
        
    except Exception as e:
        error_msg = f"Unexpected error starting application: {e}"
        print(error_msg)
        messagebox.showerror("Application Error", error_msg)
        sys.exit(1)
    
    print("\nWeather App closed successfully!")

if __name__ == "__main__":
    main()