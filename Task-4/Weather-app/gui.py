# GUI Components for Weather App
# =============================

import tkinter as tk
from tkinter import ttk, messagebox, font
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
        self.weather_data = None
        
    def setup_window(self):
        """Configure main window properties"""
        self.root.title(APP_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=COLORS["background"])
        self.root.resizable(False, False)
        
        # Center window on screen
        self.center_window()
        
        # Set window icon (optional)
        try:
            self.root.iconbitmap('assets/icon.ico')
        except:
            pass  # Icon not found, continue without it
    
    def center_window(self):
        """Center window on the screen"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width - WINDOW_WIDTH) // 2
        y = (screen_height - WINDOW_HEIGHT) // 2
        
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
    
    def create_widgets(self):
        """Create and setup all GUI widgets"""
        
        # Main container frame
        main_frame = tk.Frame(self.root, bg=COLORS["background"])
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title header
        self.create_header(main_frame)
        
        # Search section
        self.create_search_section(main_frame)
        
        # Weather display section
        self.create_weather_display(main_frame)
        
        # Status bar
        self.create_status_bar()
    
    def create_header(self, parent):
        """Create app header section"""
        header_frame = tk.Frame(parent, bg=COLORS["background"])
        header_frame.pack(fill="x", pady=(0, 20))
        
        title_label = tk.Label(
            header_frame,
            text="🌤️ Weather App",
            font=FONTS["title"],
            fg=COLORS["text"],
            bg=COLORS["background"]
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Get real-time weather information",
            font=FONTS["small"],
            fg=COLORS["text"],
            bg=COLORS["background"]
        )
        subtitle_label.pack()
    
    def create_search_section(self, parent):
        """Create search input section"""
        search_frame = tk.Frame(parent, bg=COLORS["background"])
        search_frame.pack(fill="x", pady=(0, 20))
        
        # City input label
        input_label = tk.Label(
            search_frame,
            text="Enter City Name:",
            font=FONTS["normal"],
            fg=COLORS["text"],
            bg=COLORS["background"]
        )
        input_label.pack(anchor="w")
        
        # Input frame
        input_frame = tk.Frame(search_frame, bg=COLORS["background"])
        input_frame.pack(fill="x", pady=(5, 0))
        
        # City input field
        self.city_var = tk.StringVar()
        self.city_entry = tk.Entry(
            input_frame,
            textvariable=self.city_var,
            font=FONTS["normal"],
            width=25,
            relief="flat",
            bd=5
        )
        self.city_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        # Bind Enter key to search
        self.city_entry.bind("<Return>", lambda event: self.search_weather())
        
        # Search button
        self.search_button = tk.Button(
            input_frame,
            text="🔍 Search",
            font=FONTS["normal"],
            bg=COLORS["primary"],
            fg=COLORS["text"],
            relief="flat",
            padx=20,
            command=self.search_weather,
            cursor="hand2"
        )
        self.search_button.pack(side="right")
        
        # Loading label (initially hidden)
        self.loading_label = tk.Label(
            search_frame,
            text="🔄 Loading weather data...",
            font=FONTS["small"],
            fg=COLORS["accent"],
            bg=COLORS["background"]
        )
    
    def create_weather_display(self, parent):
        """Create weather information display section"""
        # Main weather frame
        self.weather_frame = tk.Frame(parent, bg=COLORS["light_bg"], relief="raised", bd=2)
        self.weather_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        # Initially show welcome message
        self.show_welcome_message()
    
    def show_welcome_message(self):
        """Display welcome message when app starts"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        welcome_frame = tk.Frame(self.weather_frame, bg=COLORS["light_bg"])
        welcome_frame.pack(expand=True)
        
        welcome_label = tk.Label(
            welcome_frame,
            text="🌍\nWelcome to Weather App!\n\nEnter a city name above to get\nreal-time weather information",
            font=FONTS["normal"],
            fg=COLORS["dark_text"],
            bg=COLORS["light_bg"],
            justify="center"
        )
        welcome_label.pack(expand=True)
    
    def display_weather_data(self, data):
        """Display weather data in the weather frame"""
        # Clear existing widgets
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        # Main weather info frame
        main_info_frame = tk.Frame(self.weather_frame, bg=COLORS["light_bg"])
        main_info_frame.pack(fill="x", padx=20, pady=20)
        
        # Location info
        location_label = tk.Label(
            main_info_frame,
            text=f"📍 {data['city']}, {data['country']}",
            font=FONTS["heading"],
            fg=COLORS["dark_text"],
            bg=COLORS["light_bg"]
        )
        location_label.pack()
        
        # Weather icon and temperature frame
        temp_frame = tk.Frame(main_info_frame, bg=COLORS["light_bg"])
        temp_frame.pack(pady=10)
        
        # Weather icon (we'll load this)
        self.load_weather_icon(temp_frame, data['icon'])
        
        # Temperature
        temp_label = tk.Label(
            temp_frame,
            text=f"{data['temperature']}°C",
            font=("Arial", 36, "bold"),
            fg=COLORS["primary"],
            bg=COLORS["light_bg"]
        )
        temp_label.pack(side="left", padx=10)
        
        # Weather description
        desc_label = tk.Label(
            main_info_frame,
            text=data['description'],
            font=FONTS["heading"],
            fg=COLORS["dark_text"],
            bg=COLORS["light_bg"]
        )
        desc_label.pack()
        
        # Feels like temperature
        feels_label = tk.Label(
            main_info_frame,
            text=f"Feels like {data['feels_like']}°C",
            font=FONTS["normal"],
            fg=COLORS["dark_text"],
            bg=COLORS["light_bg"]
        )
        feels_label.pack(pady=(5, 15))
        
        # Additional details frame
        details_frame = tk.Frame(self.weather_frame, bg=COLORS["light_bg"])
        details_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Create details grid
        self.create_details_grid(details_frame, data)
    
    def create_details_grid(self, parent, data):
        """Create grid of additional weather details"""
        # Details data
        details = [
            ("💧 Humidity", f"{data['humidity']}%"),
            ("🌬️ Wind Speed", f"{data['wind_speed']} m/s"),
            ("📊 Pressure", f"{data['pressure']} hPa"),
            ("☁️ Cloudiness", f"{data['clouds']}%"),
            ("🌡️ Min Temp", f"{data['temp_min']}°C"),
            ("🌡️ Max Temp", f"{data['temp_max']}°C")
        ]
        
        # Create 2x3 grid
        for i, (label_text, value_text) in enumerate(details):
            row = i // 2
            col = i % 2
            
            detail_frame = tk.Frame(parent, bg=COLORS["light_bg"])
            detail_frame.grid(row=row, column=col, padx=10, pady=5, sticky="ew")
            
            # Configure grid weights
            parent.grid_columnconfigure(col, weight=1)
            
            label = tk.Label(
                detail_frame,
                text=label_text,
                font=FONTS["small"],
                fg=COLORS["dark_text"],
                bg=COLORS["light_bg"],
                anchor="w"
            )
            label.pack(anchor="w")
            
            value = tk.Label(
                detail_frame,
                text=value_text,
                font=FONTS["normal"],
                fg=COLORS["primary"],
                bg=COLORS["light_bg"],
                anchor="w"
            )
            value.pack(anchor="w")
    
    def load_weather_icon(self, parent, icon_code):
        """Load and display weather icon"""
        try:
            # Get icon URL
            icon_url = weather_api.get_weather_icon_url(icon_code)
            
            # Download icon in separate thread
            def download_icon():
                try:
                    response = requests.get(icon_url, timeout=5)
                    response.raise_for_status()
                    
                    # Load image
                    image = Image.open(io.BytesIO(response.content))
                    image = image.resize((80, 80), Image.Resampling.LANCZOS)
                    
                    # Convert to PhotoImage
                    photo = ImageTk.PhotoImage(image)
                    
                    # Update GUI in main thread
                    self.root.after(0, lambda: self.display_icon(parent, photo))
                    
                except Exception as e:
                    print(f"Error loading weather icon: {e}")
            
            # Start download thread
            threading.Thread(target=download_icon, daemon=True).start()
            
        except Exception as e:
            print(f"Error setting up icon download: {e}")
    
    def display_icon(self, parent, photo):
        """Display the loaded weather icon"""
        icon_label = tk.Label(
            parent,
            image=photo,
            bg=COLORS["light_bg"]
        )
        icon_label.image = photo  # Keep a reference
        icon_label.pack(side="left")
    
    def search_weather(self):
        """Handle weather search request"""
        city = self.city_var.get().strip()
        
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name!")
            return
        
        # Show loading state
        self.show_loading()
        
        # Perform search in separate thread
        def fetch_weather():
            success, result = weather_api.get_weather_data(city)
            
            # Update GUI in main thread
            self.root.after(0, lambda: self.handle_weather_result(success, result))
        
        # Start search thread
        threading.Thread(target=fetch_weather, daemon=True).start()
    
    def show_loading(self):
        """Show loading indicator"""
        self.search_button.config(state="disabled", text="🔄 Loading...")
        self.loading_label.pack(pady=(5, 0))
        
        # Clear weather display and show loading message
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        loading_frame = tk.Frame(self.weather_frame, bg=COLORS["light_bg"])
        loading_frame.pack(expand=True)
        
        loading_msg = tk.Label(
            loading_frame,
            text="🔄\nFetching weather data...\nPlease wait",
            font=FONTS["normal"],
            fg=COLORS["primary"],
            bg=COLORS["light_bg"],
            justify="center"
        )
        loading_msg.pack(expand=True)
    
    def handle_weather_result(self, success, result):
        """Handle the weather API result"""
        # Hide loading state
        self.search_button.config(state="normal", text="🔍 Search")
        self.loading_label.pack_forget()
        
        if success:
            # Display weather data
            self.display_weather_data(result)
            self.update_status(f"Weather data loaded for {result['city']}")
        else:
            # Show error message
            self.show_error_message(result)
            messagebox.showerror("Weather Error", result)
    
    def show_error_message(self, error_msg):
        """Display error message in weather frame"""
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        error_frame = tk.Frame(self.weather_frame, bg=COLORS["light_bg"])
        error_frame.pack(expand=True)
        
        error_label = tk.Label(
            error_frame,
            text=f"❌\nError!\n\n{error_msg}",
            font=FONTS["normal"],
            fg=COLORS["accent"],
            bg=COLORS["light_bg"],
            justify="center"
        )
        error_label.pack(expand=True)
    
    def create_status_bar(self):
        """Create status bar at bottom"""
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief="sunken",
            anchor="w",
            font=FONTS["small"],
            bg=COLORS["light_bg"],
            fg=COLORS["dark_text"]
        )
        status_bar.pack(side="bottom", fill="x")
    
    def update_status(self, message):
        """Update status bar message"""
        self.status_var.set(message)
    
    def run(self):
        """Start the application"""
        
        valid, message = weather_api.validate_api_key()
        if not valid:
            messagebox.showerror("Configuration Error", 
                               f"{message}\n\nPlease get a free API key from:\nopenweathermap.org")
            return
        
        self.update_status("Ready - Enter a city name to get weather data")
        self.root.mainloop()


app = WeatherApp()