import pyttsx3

engine = pyttsx3.init()


def speak(text, rate=170, volume=1.0):

    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)

    engine.say(text)
    engine.runAndWait()