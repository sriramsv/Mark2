__author__ = 'sriram'
import notify2
import time
class Notify():
    def __init__(self):
        notify2.init("Jarvis")
    def show(self,message):
        n=notify2.Notification(message)
        n.show()
        time.sleep(2)
        n.close()
