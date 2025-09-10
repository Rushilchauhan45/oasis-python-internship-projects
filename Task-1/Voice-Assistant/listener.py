import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    """Listen to microphone and convert speech to text"""
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"👉 You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""
    except sr.RequestError:
        print("⚠️ Network error")
        return ""
