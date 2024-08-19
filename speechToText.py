import speech_recognition as sr # type: ignore

def speech_to_text():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recog.listen(source)
        try:
            voice_data = ""
            voice_data = recog.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError:
            print("Request Error")
