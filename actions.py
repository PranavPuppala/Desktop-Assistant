import textToSpeech
import speechToText
import webbrowser
import datetime

def action(input: str) -> str:
    user_data = input
    output = ""
    
    if "what are you" in user_data:
        output = "I am a simple desktop assistant"
        textToSpeech.text_to_speech(output)

    elif "hello" in user_data or "hi" in user_data:
        output = "Hello there! How may I help you?"
        textToSpeech.text_to_speech(output)

    elif "good morning" in user_data:
        output = "Good morning!! May I provide with any assistance today?"
        textToSpeech.text_to_speech(output)

    elif "google" in user_data:
        output = "opening google"
        textToSpeech.text_to_speech(output)
        webbrowser.open("https://www.google.com")

    elif "youtube" in user_data:
        output = "opening youtube"
        textToSpeech.text_to_speech(output)
        webbrowser.open("https://www.youtube.com")
    
    elif "shut down" in user_data or "shutdown" in user_data:
        output = "shutting down..."
        textToSpeech.text_to_speech(output)
        return output


    elif "current time" in user_data or "time now" in user_data:
        now = datetime.now()
        hour = now.strftime("%I")  # Hour in 12-hour format
        minute = now.strftime("%M")  # Minute
        am_pm = now.strftime("%p")  # AM or PM
        output = f"The time is currently {hour}:{minute}{am_pm}"
        textToSpeech.text_to_speech(output)

    else:
        output = "I cannot process this command."
        textToSpeech.text_to_speech(output)
    
    return output
