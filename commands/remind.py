
from utils import tts
from config import nt,ny,broadcast,SCHEDULER
import re,time,multiprocessing,threading,signal,os


class Remind(object):
    def __init__(self,sender=None,message=None):
        # super(Remind, self).__init__()
        self.regex = "remind me (to) (?P<reminder_text>.*?) (at|on|in) (?P<remind_time>.*)?"
        self.sender=sender
        self.remainder=" "
        self.message=message
        # self.on_event()
        # self.stop=threading.Event()

    def rem(self):
        print self.what
        count=0
        time2=nt.to_natural_day_and_time(self.when_epoch)
        ny.show(self.what)
        while count<2:
            tts.speak("Sir,reminding you to {}".format(self.what))
            time.sleep(2)
            count+=1

    def on_event(self,message):
        self.message=message
        print self.message
        m=re.match(self.regex,self.message['text'],re.DOTALL)
        if m:
            self.what=m.group("reminder_text")
            self.when=m.group("remind_time")
            self.when_epoch=nt.parse_natural_time(self.when)
            print self.when_epoch
            try:
                self.remainder=SCHEDULER.add_job(self.rem,'date',name='test',next_run_time=self.when_epoch)
                print self.remainder
                return self.remainder
            except ValueError:
                tts.speak("Could not schedule this remainder")
                print "error"

    def cancel_remainder(self):
        self.remainder.remove()





@broadcast.connect
def startrem(sender,**kw):
    r=Remind()
    r.on_event(kw)
    # while 1:
    #     time.sleep(1)
print "Exiting"


