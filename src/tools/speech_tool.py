import pyttsx3
import threading


def _speak(text, rate, volume):

    engine = pyttsx3.init()

    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)

    engine.say(text)
    engine.runAndWait()


def speak(text, rate=170, volume=1.0):

    threading.Thread(
        target=_speak,
        args=(text, rate, volume),
        daemon=True,
    ).start()