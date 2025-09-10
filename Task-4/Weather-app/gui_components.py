# Beautiful Weather App GUI - Simple & Working Version
# ===================================================

import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import io
import threading
from weather_api import weather_api
from config import *

class WeatherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """Setup beautiful window"""
        self.root.title("🌤️ Beautiful Weather App")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)
        
        # Center window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - WINDOW_WIDTH) // 2
        y = (screen_height - WINDOW_HEIGHT) // 2
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
    
    def create_widgets(self):
        """Create beautiful GUI widgets"""
        # Main container
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_frame)
        
        # Search section
        self.create_search_section(main_frame)
        
        # Weather display
        self.create_weather_display(main_frame)
        
        # Status bar
        self.create_status_bar()
    
    def create_header(self, parent):
        """Create beautiful header"""
        header_frame = tk.Frame(parent, bg="#2c3e50")
        header_frame.pack(fill="x", pady=(0, 30))
        
        # Title with emoji
        title_label = tk.Label(
            header_frame,
            text="🌤️ Beautiful Weather",
            font=("Segoe UI", 24, "bold"),
            fg="#3498db",
            bg="#2c3e50"
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="✨ Discover weather with style ✨",
            font=("Segoe UI", 12),
            fg="#ecf0f1",
            bg="#2c3e50"
        )
        subtitle_label.pack(pady=(5, 0))
    
    def create_search_section(self, parent):
        """Create search section"""
        search_frame = tk.Frame(parent, bg="#34495e", relief="flat", bd=0)
        search_frame.pack(fill="x", pady=(0, 20))
        
        # Search container
        search_container = tk.Frame(search_frame, bg="#34495e")
        search_container.pack(fill="x", padx=20, pady=15)
        
        # Search icon
        search_icon = tk.Label(
            search_container,
            text="🔍",
            font=("Segoe UI", 14),
            bg="#34495e",
            fg="#3498db"
        )
        search_icon.pack(side="left", padx=(0, 10))
        
        # Entry field
        self.city_var = tk.StringVar()
        self.city_entry = tk.Entry(
            search_container,
            textvariable=self.city_var,
            font=("Segoe UI", 12),
            relief="flat",
            bd=0,
            bg="#ecf0f1",
            fg="#2c3e50",
            insertbackground="#3498db"
        )
        self.city_entry.pack(side="left", fill="x", expand=True, padx=(0, 10), ipady=8)
        self.city_entry.bind("<Return>", lambda e: self.search_weather())
        
        # Search button
        self.search_button = tk.Button(
            search_container,
            text="Search",
            font=("Segoe UI", 12, "bold"),
            bg="#3498db",
            fg="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=8,
            command=self.search_weather,
            cursor="hand2"
        )
        self.search_button.pack(side="right")
        
        # Hover effects
        self.search_button.bind("<Enter>", lambda e: self.search_button.config(bg="#2980b9"))
        self.search_button.bind("<Leave>", lambda e: self.search_button.config(bg="#3498db"))
    
    def create_weather_display(self, parent):
        """Create weather display area"""
        self.weather_frame = tk.Frame(parent, bg="#ecf0f1", relief="flat", bd=0)
        self.weather_frame.pack(fill="both", expand=True)
        
        # Show welcome message initially
        self.show_welcome_message()
    
    def show_welcome_message(self):
        """Show welcome screen"""
        # Clear frame
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        welcome_container = tk.Frame(self.weather_frame, bg="#ecf0f1")
        welcome_container.pack(expand=True)
        
        # Weather emoji
        emoji_label = tk.Label(
            welcome_container,
            text="🌍",
            font=("Segoe UI", 60),
            bg="#ecf0f1"
        )
        emoji_label.pack(pady=30)
        
        # Welcome text
        welcome_label = tk.Label(
            welcome_container,
            text="Welcome to Beautiful Weather!\n\nEnter a city name above to get\nreal-time weather information",
            font=("Segoe UI", 14),
            fg="#2c3e50",
            bg="#ecf0f1",
            justify="center"
        )
        welcome_label.pack()
    
    def display_weather_data(self, data):
        """Display weather data beautifully"""
        # Clear frame
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        # Main content frame
        content_frame = tk.Frame(self.weather_frame, bg="#ecf0f1")
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Location header
        location_frame = tk.Frame(content_frame, bg="#ecf0f1")
        location_frame.pack(fill="x", pady=(0, 20))
        
        location_label = tk.Label(
            location_frame,
            text=f"📍 {data['city']}, {data['country']}",
            font=("Segoe UI", 16, "bold"),
            fg="#2c3e50",
            bg="#ecf0f1"
        )
        location_label.pack()
        
        # Main weather info
        main_info_frame = tk.Frame(content_frame, bg="#ecf0f1")
        main_info_frame.pack(fill="x", pady=(0, 20))
        
        # Temperature and icon
        temp_frame = tk.Frame(main_info_frame, bg="#ecf0f1")
        temp_frame.pack()
        
        # Weather icon
        self.load_weather_icon(temp_frame, data['icon'])
        
        # Temperature
        temp_label = tk.Label(
            temp_frame,
            text=f"{data['temperature']}°C",
            font=("Segoe UI", 36, "bold"),
            fg="#e74c3c",
            bg="#ecf0f1"
        )
        temp_label.pack(side="left", padx=20)
        
        # Description
        desc_label = tk.Label(
            main_info_frame,
            text=data['description'],
            font=("Segoe UI", 14, "bold"),
            fg="#34495e",
            bg="#ecf0f1"
        )
        desc_label.pack(pady=(10, 0))
        
        # Feels like
        feels_label = tk.Label(
            main_info_frame,
            text=f"Feels like {data['feels_like']}°C",
            font=("Segoe UI", 12),
            fg="#7f8c8d",
            bg="#ecf0f1"
        )
        feels_label.pack(pady=(5, 0))
        
        # Details grid
        self.create_details_grid(content_frame, data)
    
    def create_details_grid(self, parent, data):
        """Create details grid"""
        details_frame = tk.Frame(parent, bg="#ecf0f1")
        details_frame.pack(fill="x", pady=20)
        
        # Details data
        details = [
            ("💧", "Humidity", f"{data['humidity']}%", "#3498db"),
            ("🌬️", "Wind", f"{data['wind_speed']} m/s", "#2ecc71"),
            ("📊", "Pressure", f"{data['pressure']} hPa", "#f39c12"),
            ("☁️", "Clouds", f"{data['clouds']}%", "#9b59b6"),
            ("🌡️", "Min", f"{data['temp_min']}°C", "#3498db"),
            ("🌡️", "Max", f"{data['temp_max']}°C", "#e74c3c")
        ]
        
        # Create 2x3 grid
        for i, (icon, label_text, value_text, color) in enumerate(details):
            row = i // 2
            col = i % 2
            
            detail_card = tk.Frame(details_frame, bg="white", relief="flat", bd=1)
            detail_card.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            
            details_frame.grid_columnconfigure(col, weight=1)
            
            # Card content
            card_content = tk.Frame(detail_card, bg="white")
            card_content.pack(fill="both", expand=True, padx=10, pady=10)
            
            # Icon
            icon_label = tk.Label(
                card_content,
                text=icon,
                font=("Segoe UI", 16),
                bg="white"
            )
            icon_label.pack()
            
            # Label
            label = tk.Label(
                card_content,
                text=label_text,
                font=("Segoe UI", 10),
                fg="#7f8c8d",
                bg="white"
            )
            label.pack()
            
            # Value
            value = tk.Label(
                card_content,
                text=value_text,
                font=("Segoe UI", 12, "bold"),
                fg=color,
                bg="white"
            )
            value.pack()
    
    def load_weather_icon(self, parent, icon_code):
        """Load weather icon - simplified without threading"""
        try:
            # Just use emoji fallback for now to avoid threading issues
            self.display_fallback_icon(parent, icon_code)
            
        except Exception as e:
            print(f"Icon setup error: {e}")
            self.display_fallback_icon(parent, icon_code)
    
    def display_icon(self, parent, photo):
        """Display the downloaded icon"""
        icon_label = tk.Label(parent, image=photo, bg="#ecf0f1")
        icon_label.image = photo
        icon_label.pack(side="left")
    
    def display_fallback_icon(self, parent, icon_code):
        """Display fallback emoji icon"""
        emoji_map = {
            '01d': '☀️', '01n': '🌙', '02d': '⛅', '02n': '☁️',
            '03d': '☁️', '03n': '☁️', '04d': '☁️', '04n': '☁️',
            '09d': '🌧️', '09n': '🌧️', '10d': '🌦️', '10n': '🌧️',
            '11d': '⛈️', '11n': '⛈️', '13d': '❄️', '13n': '❄️',
            '50d': '🌫️', '50n': '🌫️'
        }
        emoji = emoji_map.get(icon_code, '🌤️')
        emoji_label = tk.Label(parent, text=emoji, font=("Segoe UI", 40), bg="#ecf0f1")
        emoji_label.pack(side="left")
    
    def search_weather(self):
        """Search for weather"""
        city = self.city_var.get().strip()
        
        if not city:
            messagebox.showwarning("Input Required", "Please enter a city name!")
            return
        
        # Show loading
        self.search_button.config(state="disabled", text="Loading...")
        self.show_loading()
        
        # Fetch weather data directly (no threading for now)
        try:
            success, result = weather_api.get_weather_data(city)
            
            # Handle result directly
            self.handle_weather_result(success, result)
            
        except Exception as e:
            self.search_button.config(state="normal", text="Search")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def handle_weather_result(self, success, result):
        """Handle weather result in main thread"""
        self.search_button.config(state="normal", text="Search")
        
        if success:
            self.display_weather_data(result)
            self.update_status(f"✅ Weather loaded for {result['city']}")
        else:
            self.show_error(result)
            messagebox.showerror("Error", result)
    
    def show_loading(self):
        """Show loading screen"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        loading_container = tk.Frame(self.weather_frame, bg="#ecf0f1")
        loading_container.pack(expand=True)
        
        loading_label = tk.Label(
            loading_container,
            text="🔄\n\nFetching weather data...\nPlease wait",
            font=("Segoe UI", 14),
            fg="#3498db",
            bg="#ecf0f1",
            justify="center"
        )
        loading_label.pack()
    
    def show_error(self, error_msg):
        """Show error message"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        error_container = tk.Frame(self.weather_frame, bg="#ecf0f1")
        error_container.pack(expand=True)
        
        error_label = tk.Label(
            error_container,
            text=f"❌\n\nError!\n\n{error_msg}",
            font=("Segoe UI", 14),
            fg="#e74c3c",
            bg="#ecf0f1",
            justify="center"
        )
        error_label.pack()
    
    def create_status_bar(self):
        """Create status bar"""
        self.status_var = tk.StringVar()
        self.status_var.set("🌟 Ready - Enter a city name to get weather information")
        
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief="flat",
            anchor="w",
            font=("Segoe UI", 10),
            bg="#34495e",
            fg="#ecf0f1",
            padx=10,
            pady=5
        )
        status_bar.pack(side="bottom", fill="x")
    
    def update_status(self, message):
        """Update status message"""
        self.status_var.set(message)
    
    def run(self):
        """Start the application"""
        # Validate API key
        valid, message = weather_api.validate_api_key()
        if not valid:
            messagebox.showerror("Configuration Error", 
                               f"{message}\n\nPlease get a free API key from:\nopenweathermap.org")
            return
        
        self.update_status("🌟 Ready - Enter a city name to get weather information")
        self.root.mainloop()


# Create app instance
app = WeatherApp()
