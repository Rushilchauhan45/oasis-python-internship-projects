# Voice Assistant Commands - Enhanced with GUI Support
# =====================================================

import datetime
import webbrowser
import pyjokes
from speech_engine import speak
from listener import listen

# Global variable to store GUI reference for chat logging
gui_app = None

def set_gui_reference(app):
    """Set reference to GUI app for chat logging"""
    global gui_app
    gui_app = app

def add_response_to_chat(response):
    """Add assistant response to GUI chat if available"""
    if gui_app:
        try:
            gui_app.root.after(0, lambda: gui_app.add_chat_message("🤖 Assistant", response))
        except:
            pass  # Ignore if GUI not available

def process_command(command: str):
    """
    Process user commands and return responses
    Enhanced with GUI chat integration
    """
    command = command.lower().strip()
    
    if "hello" in command or "hi" in command:
        response = "Hello! How can I help you today? 😊"
        speak(response)
        add_response_to_chat(response)
    
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {now} ⏰"
        speak(f"The time is {now}")
        add_response_to_chat(response)
    
    elif "date" in command or "today" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        response = f"Today is {today} 📅"
        speak(f"Today is {today}")
        add_response_to_chat(response)
    
    elif "open google" in command or "google" in command:
        webbrowser.open("https://www.google.com")
        response = "Opening Google in your browser 🌐"
        speak("Opening Google")
        add_response_to_chat(response)
    
    elif "search" in command:
        # Extract search query from command
        if "for" in command:
            query = command.split("for", 1)[1].strip()
        elif "search" in command:
            query = command.replace("search", "").strip()
        else:
            speak("What do you want to search?")
            add_response_to_chat("What would you like to search for? 🔍")
            query = listen()
        
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            response = f"Searching for '{query}' on Google 🔍"
            speak(f"Here are the search results for {query}")
            add_response_to_chat(response)
        else:
            response = "I didn't catch that. Please try again."
            speak(response)
            add_response_to_chat(response)
    
    elif "joke" in command or "funny" in command:
        try:
            joke = pyjokes.get_joke()
            response = f"Here's a joke for you: {joke} 😄"
            speak(joke)
            add_response_to_chat(response)
        except:
            response = "Why don't programmers like nature? It has too many bugs! 😂"
            speak(response)
            add_response_to_chat(response)
    
    elif "weather" in command:
        response = "I can't check weather yet, but you can use the weather app in Task-4! 🌤️"
        speak("I can't check weather yet, but you can use the weather app!")
        add_response_to_chat(response)
    
    elif "what can you do" in command or "help" in command or "commands" in command:
        response = """I can help you with:
        • Greetings and conversations
        • Tell you the current time and date
        • Open Google and search the web
        • Tell programming jokes
        • Basic voice interactions
        
        Just speak naturally! 🗣️"""
        speak("I can tell you the time, date, open Google, search the web, tell jokes, and have conversations with you!")
        add_response_to_chat(response)
    
    elif "thank you" in command or "thanks" in command:
        response = "You're welcome! Happy to help! 😊"
        speak("You're welcome!")
        add_response_to_chat(response)
    
    elif "how are you" in command:
        response = "I'm doing great! Thanks for asking. How are you? 😊"
        speak("I'm doing great! Thanks for asking. How are you?")
        add_response_to_chat(response)
    
    elif "your name" in command or "who are you" in command:
        response = "I'm your AI Voice Assistant! I'm here to help with various tasks. 🤖"
        speak("I'm your AI Voice Assistant! I'm here to help you.")
        add_response_to_chat(response)
    
    elif "exit" in command or "quit" in command or "stop" in command or "bye" in command:
        response = "Goodbye! Have a wonderful day! 👋"
        speak("Goodbye! Have a nice day.")
        add_response_to_chat(response)
        return False
    
    else:
        response = f"I heard '{command}' but I'm not sure what to do with that. Try asking for help! 🤔"
        speak("Sorry, I can't do that yet. Try asking what I can do!")
        add_response_to_chat(response)
    
    return True

# Available commands list for reference
AVAILABLE_COMMANDS = [
    "Hello/Hi - Greet the assistant",
    "What time is it? - Get current time", 
    "What's the date/today? - Get current date",
    "Open Google - Open Google in browser",
    "Search for [query] - Search on Google",
    "Tell me a joke - Get a programming joke",
    "What can you do/Help - List available commands",
    "Thank you - Polite response",
    "How are you? - Casual conversation",
    "What's your name? - Learn about the assistant",
    "Exit/Quit/Stop/Bye - Close the assistant"
]
