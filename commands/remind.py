from commands import RegexCommand
from utils import tts
from utils import naturaltime
from config import SCHEDULER,nt,ny


class Reminder(RegexCommand):

    def __init__(self):
        regex = "remind me (to) (?P<reminder_text>.*?) (at|on|in) (?P<remind_time>.*)?"
        super(Reminder, self).__init__(regex, False)

    def on_event(self, event, sender):
        m=self.match(event)
        if m:
            self.what=m.group("reminder_text")
            self.when=m.group("remind_time")
            self.when_epoch=nt.parse_natural_time(self.when)
            print self.when_epoch
            try:
                self.remainder=SCHEDULER.add_job(self.remind,'date',run_date=self.when_epoch)

            except ValueError:
                tts.text_to_speech("Could not schedule this remainder")

    def remind(self):
        count=0
        time=nt.to_natural_day_and_time(self.when_epoch)
        ny.show(self.what,time)
        while count!=2:
            tts.text_to_speech("Sir,reminding you to {}".format(self.what))
            time.sleep(2)
            count+=1
    def cancel_remainder(self):
        self.remainder.remove()

