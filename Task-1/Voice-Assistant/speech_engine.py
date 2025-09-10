import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text: str):
    """Convert text to speech"""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
