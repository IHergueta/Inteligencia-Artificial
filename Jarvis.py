import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
#pip install pipwin
#pipwin install PyAudio

engine= pyttsx3.init()

def speak(audio):

    voices = engine.getProperty('voices') #cambiar voz
    engine.setProperty('voice', voices[1].id) # 0 hombre , 1 mujer
    engine.say(audio)
    engine.runAndWait()

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Eschuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconociendo..")
        query = r.recognize_google(audio, language='en-in')
        print(query)


    except Exception as e:
        print(e)
        speak("Repite")

    return speak(query)
escuchar()
