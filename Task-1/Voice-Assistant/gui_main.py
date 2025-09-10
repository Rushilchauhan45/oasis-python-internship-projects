# Voice Assistant GUI - Advanced 3D-like Interface
# ================================================

import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
from datetime import datetime
import math
import os

# Import voice assistant modules
from listener import listen
from speech_engine import speak
from commands import process_command, set_gui_reference

class VoiceAssistantGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.create_variables()
        self.create_widgets()
        self.is_listening = False
        self.is_running = False
        self.animation_running = False
        
        # Set GUI reference for commands module
        set_gui_reference(self)
        
    def setup_window(self):
        """Setup the main window with modern styling"""
        self.root.title("🎤 AI Voice Assistant - 3D Interface")
        self.root.geometry("900x700")
        self.root.configure(bg="#0f0f23")
        self.root.resizable(False, False)
        
        # Center window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 900) // 2
        y = (screen_height - 700) // 2
        self.root.geometry(f"900x700+{x}+{y}")
        
        # Modern style configuration
        style = ttk.Style()
        style.theme_use('clam')
        
    def create_variables(self):
        """Create tkinter variables"""
        self.status_var = tk.StringVar(value="🤖 Ready to assist you!")
        self.command_var = tk.StringVar()
        self.response_var = tk.StringVar(value="Hi! I'm your AI Voice Assistant. Click 'Start' to begin!")
        
    def create_widgets(self):
        """Create all GUI widgets with 3D-like effects"""
        # Main container with gradient effect
        self.create_gradient_background()
        
        # Header section
        self.create_header()
        
        # Main control panel
        self.create_control_panel()
        
        # Chat/Log area
        self.create_chat_area()
        
        # Status bar
        self.create_status_bar()
        
        # Start animations
        self.start_animations()
    
    def create_gradient_background(self):
        """Create gradient background effect"""
        self.bg_canvas = tk.Canvas(self.root, width=900, height=700, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        
        # Create gradient from dark blue to purple
        for i in range(700):
            ratio = i / 700
            # Dark blue to purple gradient
            r = int(15 + (60 - 15) * ratio)    # 15 to 60
            g = int(15 + (20 - 15) * ratio)    # 15 to 20  
            b = int(35 + (100 - 35) * ratio)   # 35 to 100
            
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.bg_canvas.create_line(0, i, 900, i, fill=color, width=1)
    
    def create_header(self):
        """Create header with animated title"""
        header_frame = tk.Frame(self.bg_canvas, bg="#1a1a3a", relief="flat", bd=0)
        header_frame.place(x=50, y=30, width=800, height=120)
        
        # Add 3D shadow effect
        shadow_frame = tk.Frame(self.bg_canvas, bg="#000011", relief="flat", bd=0)
        shadow_frame.place(x=53, y=33, width=800, height=120)
        header_frame.lift()
        
        # Animated AI emoji
        self.ai_emoji = tk.Label(
            header_frame,
            text="🤖",
            font=("Segoe UI Emoji", 40),
            bg="#1a1a3a",
            fg="#00ff88"
        )
        self.ai_emoji.pack(pady=10)
        
        # Title
        title_label = tk.Label(
            header_frame,
            text="AI VOICE ASSISTANT",
            font=("Segoe UI", 20, "bold"),
            bg="#1a1a3a",
            fg="#00ff88"
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="✨ Advanced 3D Interface with Voice Recognition ✨",
            font=("Segoe UI", 12),
            bg="#1a1a3a",
            fg="#88ccff"
        )
        subtitle_label.pack()
    
    def create_control_panel(self):
        """Create main control panel with 3D buttons"""
        control_frame = tk.Frame(self.bg_canvas, bg="#1e1e3e", relief="flat", bd=0)
        control_frame.place(x=50, y=170, width=800, height=180)
        
        # Shadow for 3D effect
        shadow_frame = tk.Frame(self.bg_canvas, bg="#000015", relief="flat", bd=0)
        shadow_frame.place(x=53, y=173, width=800, height=180)
        control_frame.lift()
        
        # Voice visualizer area
        self.voice_viz_frame = tk.Frame(control_frame, bg="#2a2a4a", relief="flat", bd=0)
        self.voice_viz_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        
        # Create voice visualizer
        self.create_voice_visualizer()
        
        # Control buttons frame
        buttons_frame = tk.Frame(control_frame, bg="#1e1e3e")
        buttons_frame.pack(side="right", padx=20, pady=20)
        
        # Start/Stop button
        self.start_button = tk.Button(
            buttons_frame,
            text="🎤 START",
            font=("Segoe UI", 14, "bold"),
            bg="#00cc66",
            fg="white",
            relief="flat",
            bd=0,
            padx=30,
            pady=15,
            command=self.toggle_assistant,
            cursor="hand2"
        )
        self.start_button.pack(pady=10)
        
        # Listen button
        self.listen_button = tk.Button(
            buttons_frame,
            text="👂 LISTEN",
            font=("Segoe UI", 12, "bold"),
            bg="#0066cc",
            fg="white",
            relief="flat",
            bd=0,
            padx=25,
            pady=10,
            command=self.manual_listen,
            cursor="hand2",
            state="disabled"
        )
        self.listen_button.pack(pady=5)
        
        # Settings button
        settings_button = tk.Button(
            buttons_frame,
            text="⚙️ SETTINGS",
            font=("Segoe UI", 10, "bold"),
            bg="#666699",
            fg="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=8,
            command=self.show_settings,
            cursor="hand2"
        )
        settings_button.pack(pady=5)
        
        # Add hover effects
        self.add_button_effects()
    
    def create_voice_visualizer(self):
        """Create animated voice visualizer"""
        viz_label = tk.Label(
            self.voice_viz_frame,
            text="🔊 Voice Visualizer",
            font=("Segoe UI", 12, "bold"),
            bg="#2a2a4a",
            fg="#88ccff"
        )
        viz_label.pack(pady=5)
        
        # Canvas for wave animation
        self.viz_canvas = tk.Canvas(
            self.voice_viz_frame,
            width=400,
            height=100,
            bg="#1a1a2e",
            highlightthickness=0
        )
        self.viz_canvas.pack(pady=10)
        
        # Status indicator
        self.status_indicator = tk.Label(
            self.voice_viz_frame,
            text="⚫ Idle",
            font=("Segoe UI", 10),
            bg="#2a2a4a",
            fg="#cccccc"
        )
        self.status_indicator.pack()
    
    def create_chat_area(self):
        """Create chat/log area"""
        chat_frame = tk.Frame(self.bg_canvas, bg="#1e1e3e", relief="flat", bd=0)
        chat_frame.place(x=50, y=370, width=800, height=250)
        
        # Shadow
        shadow_frame = tk.Frame(self.bg_canvas, bg="#000015", relief="flat", bd=0)
        shadow_frame.place(x=53, y=373, width=800, height=250)
        chat_frame.lift()
        
        # Chat header
        chat_header = tk.Label(
            chat_frame,
            text="💬 CONVERSATION LOG",
            font=("Segoe UI", 12, "bold"),
            bg="#1e1e3e",
            fg="#00ff88"
        )
        chat_header.pack(pady=(10, 5))
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            width=90,
            height=12,
            font=("Consolas", 10),
            bg="#0f0f1a",
            fg="#88ccff",
            insertbackground="#00ff88",
            relief="flat",
            bd=0,
            wrap=tk.WORD
        )
        self.chat_display.pack(padx=20, pady=(0, 20), fill="both", expand=True)
        
        # Add welcome message
        self.add_chat_message("🤖 System", "Voice Assistant initialized successfully!")
        self.add_chat_message("💡 Tip", "Click 'START' to begin voice interaction")
    
    def create_status_bar(self):
        """Create status bar"""
        status_frame = tk.Frame(self.bg_canvas, bg="#0a0a1a", relief="flat", bd=0)
        status_frame.place(x=0, y=650, width=900, height=50)
        
        # Status text
        status_label = tk.Label(
            status_frame,
            textvariable=self.status_var,
            font=("Segoe UI", 10),
            bg="#0a0a1a",
            fg="#88ccff",
            anchor="w"
        )
        status_label.pack(side="left", padx=20, pady=15)
        
        # Time display
        self.time_label = tk.Label(
            status_frame,
            text="",
            font=("Segoe UI", 10),
            bg="#0a0a1a",
            fg="#00ff88"
        )
        self.time_label.pack(side="right", padx=20, pady=15)
    
    def add_button_effects(self):
        """Add hover effects to buttons"""
        def on_enter_start(e):
            self.start_button.config(bg="#00ff66")
        def on_leave_start(e):
            color = "#cc3333" if self.is_running else "#00cc66"
            self.start_button.config(bg=color)
            
        def on_enter_listen(e):
            if self.listen_button["state"] != "disabled":
                self.listen_button.config(bg="#0088ff")
        def on_leave_listen(e):
            if self.listen_button["state"] != "disabled":
                self.listen_button.config(bg="#0066cc")
        
        self.start_button.bind("<Enter>", on_enter_start)
        self.start_button.bind("<Leave>", on_leave_start)
        self.listen_button.bind("<Enter>", on_enter_listen)
        self.listen_button.bind("<Leave>", on_leave_listen)
    
    def start_animations(self):
        """Start background animations"""
        self.animation_running = True
        self.animate_ai_emoji()
        self.animate_voice_waves()
        self.update_time()
    
    def animate_ai_emoji(self):
        """Animate the AI emoji"""
        if not self.animation_running:
            return
            
        try:
            emojis = ["🤖", "🎤", "🔊", "💫"] if getattr(self, 'is_listening', False) else ["🤖", "😴", "🤖", "💤"]
            current_emoji = self.ai_emoji.cget("text")
            
            try:
                current_index = emojis.index(current_emoji)
                next_index = (current_index + 1) % len(emojis)
            except ValueError:
                next_index = 0
            
            self.ai_emoji.config(text=emojis[next_index])
            
            # Different speeds for different states
            delay = 500 if getattr(self, 'is_listening', False) else 2000
            self.root.after(delay, self.animate_ai_emoji)
        except Exception as e:
            print(f"Animation error: {e}")
            # Restart animation after delay
            self.root.after(2000, self.animate_ai_emoji)
    
    def animate_voice_waves(self):
        """Animate voice visualization waves"""
        if not self.animation_running:
            return
            
        try:
            self.viz_canvas.delete("all")
            
            if getattr(self, 'is_listening', False):
                # Draw animated waves
                width = 400
                height = 100
                center_y = height // 2
                
                for i in range(0, width, 20):
                    # Create wave effect
                    wave_height = math.sin((i + time.time() * 100) * 0.1) * 20
                    
                    self.viz_canvas.create_line(
                        i, center_y,
                        i, center_y + wave_height,
                        fill="#00ff88",
                        width=3
                    )
                    
                    self.viz_canvas.create_line(
                        i + 10, center_y,
                        i + 10, center_y - wave_height * 0.5,
                        fill="#0088ff",
                        width=2
                    )
            else:
                # Draw static line
                self.viz_canvas.create_line(
                    0, 50, 400, 50,
                    fill="#333355",
                    width=2
                )
            
            self.root.after(50, self.animate_voice_waves)
        except Exception as e:
            print(f"Wave animation error: {e}")
            # Restart animation after delay
            self.root.after(100, self.animate_voice_waves)
    
    def update_time(self):
        """Update time display"""
        if not self.animation_running:
            return
            
        try:
            current_time = datetime.now().strftime("%H:%M:%S | %d %B %Y")
            self.time_label.config(text=current_time)
            self.root.after(1000, self.update_time)
        except Exception as e:
            print(f"Time update error: {e}")
            self.root.after(1000, self.update_time)
    
    def toggle_assistant(self):
        """Toggle assistant on/off"""
        if not self.is_running:
            self.start_assistant()
        else:
            self.stop_assistant()
    
    def start_assistant(self):
        """Start the voice assistant"""
        self.is_running = True
        self.start_button.config(text="🛑 STOP", bg="#cc3333")
        self.listen_button.config(state="normal")
        self.status_var.set("🟢 Assistant is active and ready!")
        
        # Add to chat
        self.add_chat_message("🤖 System", "Voice Assistant started successfully!")
        
        # Start listening in background
        threading.Thread(target=self.background_listener, daemon=True).start()
    
    def stop_assistant(self):
        """Stop the voice assistant"""
        self.is_running = False
        self.is_listening = False
        self.start_button.config(text="🎤 START", bg="#00cc66")
        self.listen_button.config(state="disabled")
        self.status_var.set("🔴 Assistant stopped")
        self.status_indicator.config(text="⚫ Idle")
        
        # Add to chat
        self.add_chat_message("🤖 System", "Voice Assistant stopped")
    
    def background_listener(self):
        """Background listening loop"""
        speak("Voice Assistant is now active!")
        
        while self.is_running:
            try:
                self.is_listening = True
                self.root.after(0, lambda: self.status_indicator.config(text="🔴 Listening..."))
                self.root.after(0, lambda: self.status_var.set("🎤 Listening for commands..."))
                
                # Listen for command
                command = listen()
                
                self.is_listening = False
                self.root.after(0, lambda: self.status_indicator.config(text="🟡 Processing..."))
                
                if command:
                    # Add command to chat
                    self.root.after(0, lambda: self.add_chat_message("👤 You", command))
                    self.root.after(0, lambda: self.status_var.set(f"🗣️ Processing: {command}"))
                    
                    # Process command
                    result = process_command(command)
                    
                    if not result:  # Exit command
                        self.root.after(0, self.stop_assistant)
                        break
                        
                    self.root.after(0, lambda: self.status_indicator.config(text="✅ Ready"))
                    
                else:
                    self.root.after(0, lambda: self.status_indicator.config(text="❌ No input"))
                    time.sleep(1)
                    
            except Exception as e:
                self.root.after(0, lambda: self.add_chat_message("❌ Error", f"An error occurred: {str(e)}"))
                time.sleep(2)
        
        self.is_listening = False
        self.root.after(0, lambda: self.status_indicator.config(text="⚫ Idle"))
    
    def manual_listen(self):
        """Manual listen button"""
        if not self.is_listening and self.is_running:
            threading.Thread(target=self.single_listen, daemon=True).start()
    
    def single_listen(self):
        """Single listen operation"""
        try:
            self.is_listening = True
            self.root.after(0, lambda: self.status_indicator.config(text="🔴 Listening..."))
            self.root.after(0, lambda: self.status_var.set("🎤 Listening for your command..."))
            
            command = listen()
            
            self.is_listening = False
            
            if command:
                self.root.after(0, lambda: self.add_chat_message("👤 You", command))
                self.root.after(0, lambda: self.status_var.set(f"🗣️ Processing: {command}"))
                
                result = process_command(command)
                
                if not result:  # Exit command
                    self.root.after(0, self.stop_assistant)
                else:
                    self.root.after(0, lambda: self.status_var.set("✅ Command processed successfully"))
            else:
                self.root.after(0, lambda: self.status_var.set("❌ No command detected"))
                
            self.root.after(0, lambda: self.status_indicator.config(text="✅ Ready"))
            
        except Exception as e:
            self.root.after(0, lambda: self.add_chat_message("❌ Error", f"Error: {str(e)}"))
            self.is_listening = False
            self.root.after(0, lambda: self.status_indicator.config(text="❌ Error"))
    
    def add_chat_message(self, sender, message):
        """Add message to chat display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {sender}: {message}\n"
        
        self.chat_display.insert(tk.END, formatted_message)
        self.chat_display.see(tk.END)
    
    def show_settings(self):
        """Show settings dialog"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("⚙️ Voice Assistant Settings")
        settings_window.geometry("400x300")
        settings_window.configure(bg="#1a1a3a")
        settings_window.resizable(False, False)
        
        # Center the settings window
        x = self.root.winfo_x() + 250
        y = self.root.winfo_y() + 200
        settings_window.geometry(f"400x300+{x}+{y}")
        
        # Settings content
        title_label = tk.Label(
            settings_window,
            text="🛠️ Voice Assistant Settings",
            font=("Segoe UI", 14, "bold"),
            bg="#1a1a3a",
            fg="#00ff88"
        )
        title_label.pack(pady=20)
        
        # Available commands
        commands_label = tk.Label(
            settings_window,
            text="📋 Available Commands:",
            font=("Segoe UI", 12, "bold"),
            bg="#1a1a3a",
            fg="#88ccff"
        )
        commands_label.pack(pady=(10, 5))
        
        commands_text = """
        • "Hello" - Greet the assistant
        • "What time is it?" - Get current time
        • "What's the date?" - Get current date  
        • "Open Google" - Open Google in browser
        • "Search for [query]" - Search on Google
        • "Tell me a joke" - Get a programming joke
        • "Exit" or "Quit" - Close the assistant
        """
        
        commands_display = tk.Label(
            settings_window,
            text=commands_text,
            font=("Segoe UI", 9),
            bg="#1a1a3a",
            fg="#cccccc",
            justify="left"
        )
        commands_display.pack(pady=10)
        
        # Close button
        close_button = tk.Button(
            settings_window,
            text="✅ Close",
            font=("Segoe UI", 10, "bold"),
            bg="#00cc66",
            fg="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=8,
            command=settings_window.destroy,
            cursor="hand2"
        )
        close_button.pack(pady=20)
    
    def run(self):
        """Start the GUI application"""
        try:
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.root.mainloop()
        except KeyboardInterrupt:
            self.on_closing()
    
    def on_closing(self):
        """Handle window closing"""
        self.animation_running = False
        self.is_running = False
        self.is_listening = False
        
        try:
            speak("Goodbye! Voice Assistant is shutting down.")
        except:
            pass
            
        self.root.quit()
        self.root.destroy()

# Create and run the GUI application
if __name__ == "__main__":
    try:
        app = VoiceAssistantGUI()
        app.run()
    except Exception as e:
        print(f"Error starting Voice Assistant GUI: {e}")
