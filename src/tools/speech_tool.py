import threading
import time
import pyttsx3


class SpeechManager:

    def __init__(self):

        self.rate = 170
        self.volume = 1.0

        self.engine = None
        self.thread = None

        self.lock = threading.Lock()

    # --------------------------------------------------
    # Settings
    # --------------------------------------------------
    def set_speed(self, rate):

        self.rate = rate

    def set_volume(self, volume):

        self.volume = volume

    # --------------------------------------------------
    # Internal Worker
    # --------------------------------------------------
    def _run(self, text):

        try:

            engine = pyttsx3.init()

            with self.lock:
                self.engine = engine

            engine.setProperty("rate", self.rate)
            engine.setProperty("volume", self.volume)

            engine.say(text)
            engine.runAndWait()

        except Exception as e:

            print("Speech Error:", e)

        finally:

            try:
                engine.stop()
            except:
                pass

            with self.lock:
                self.engine = None

    # --------------------------------------------------
    # Speak
    # --------------------------------------------------
    def speak(self, text):

        self.stop()

        time.sleep(0.15)

        self.thread = threading.Thread(
            target=self._run,
            args=(text,),
            daemon=True,
        )

        self.thread.start()

    # --------------------------------------------------
    # Stop Current Speech
    # --------------------------------------------------
    def stop(self):

        with self.lock:

            if self.engine:

                try:
                    self.engine.stop()

                except Exception:
                    pass

                self.engine = None


speech = SpeechManager()
