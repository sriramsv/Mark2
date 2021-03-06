import random
import sys

import speech_recognition as sr
from config import GOOGLE_API_KEY, voice_queue
from utils.tts import speak


class OnlineRecognizer():
    def __init__(self):
        self.r = sr.Recognizer()
        self.r.energy_threshold = 3000
        self.r.pause_threshold = 0.5
        # subprocess.call("pulseaudio --kill>/dev/null",shell=True)
        # subprocess.call("jack_control start>/dev/null",shell=True)
        self.randomresp=['I am listening','yes sir', 'At your service']
    # def pause(self):
    #     os.kill(self.pid,signal.SIGSTOP)
    # def resume(self):
    #     os.kill(self.pid, signal.SIGCONT)
    # def end(self):
    #     print "ending recognition server"
    #     print 'stopping recognition'

    def online_recognition(self):
        r=self.r
        speak(random.choice(self.randomresp))
        try:
            with sr.Microphone() as source:
                audi1 = r.adjust_for_ambient_noise(source)
                print "----------Listening-------"
                audi1 = r.listen(source)
                print "----------Recognizing-------"
                try:
                    data=r.recognize_google(audi1,key=GOOGLE_API_KEY,language="en-US",show_all=False)
                    voice_queue.put(data.lower())
                    return True
                except IndexError:
                    # the API key didn't work
                    speak("I am sorry sir, could not connect to the internet")
                    print("No internet connection")
                except KeyError:
                    speak("I am afraid,your API key is invalid")
                    print("Invalid API key or quota maxed out")
                except LookupError:
                    print("Could not understand audio")
                except sr.UnknownValueError:
                    pass

        except KeyboardInterrupt:
            sys.exit(0)
