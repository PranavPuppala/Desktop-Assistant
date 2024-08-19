import pyttsx3 # type: ignore

def text_to_speech(text: str):
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", "rate-70")
    engine.say(text)
    engine.runAndWait()
