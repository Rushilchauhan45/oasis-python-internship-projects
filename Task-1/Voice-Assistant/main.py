# Voice Assistant - Main Entry Point with GUI Option
# ==================================================

import sys
import os
from listener import listen
from speech_engine import speak
from commands import process_command

def run_console_assistant():
    """
    Run the voice assistant in console mode
    """
    print("🤖 Voice Assistant - Console Mode")
    print("=" * 40)
    speak("Hello! I am your voice assistant. How can I help you today?")
    
    while True:
        print("\n🎤 Listening...")
        # Listen for user command
        command = listen()
        
        if command:
            print(f"👤 You said: {command}")
            # Process the command
            result = process_command(command)
            
            # If result is False, it means exit was called
            if not result:
                break
        else:
            print("❌ No command detected. Please try again.")

def run_gui_assistant():
    """
    Run the voice assistant with GUI
    """
    try:
        from gui_main import VoiceAssistantGUI
        print("🚀 Starting Voice Assistant with GUI...")
        app = VoiceAssistantGUI()
        app.run()
    except ImportError as e:
        print(f"❌ Error: GUI modules not found - {e}")
        print("📝 Falling back to console mode...")
        run_console_assistant()
    except Exception as e:
        print(f"❌ Error starting GUI: {e}")
        print("📝 Falling back to console mode...")
        run_console_assistant()

def main():
    """
    Main function - Choose between GUI and console mode
    """
    print("🎯 Voice Assistant Launcher")
    print("=" * 30)
    print("1. GUI Mode (Recommended)")
    print("2. Console Mode")
    print("3. Auto-detect")
    
    try:
        choice = input("\n🔢 Enter your choice (1-3) or press Enter for auto: ").strip()
        
        if choice == "1":
            run_gui_assistant()
        elif choice == "2":
            run_console_assistant()
        else:  # Auto-detect or default
            # Try GUI first, fallback to console
            try:
                import tkinter
                run_gui_assistant()
            except ImportError:
                print("⚠️ Tkinter not available. Using console mode.")
                run_console_assistant()
                
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Legacy function for backward compatibility
def run_assistant():
    """Legacy function - redirects to console mode"""
    run_console_assistant()

if __name__ == "__main__":
    main()
