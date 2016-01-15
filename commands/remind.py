
from utils import naturaltime,tts
from config import SCHEDULER,nt,ny,broadcast
import re,time

class Remind(object):
    def __init__(self,sender=None,message=None):
        self.regex = "remind me (to) (?P<reminder_text>.*?) (at|on|in) (?P<remind_time>.*)?"
        self.sender=sender
        self.remainder=" "
        self.message=message
        # self.on_event()

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
                self.remainder=SCHEDULER.add_job(self.rem,'date',name='test',run_date=self.when_epoch)
                print self.remainder
            except ValueError:
                tts.speak("Could not schedule this remainder")
                print "error"

    def rem(self):
        print self.what
        count=0
        time=nt.to_natural_day_and_time(self.when_epoch)
        # ny.show(self.what,time)
        while count!=2:
            tts.speak("Sir,reminding you to {}".format(self.what))
            time.sleep(2)
            count+=1

    def cancel_remainder(self):
        self.remainder.remove()




