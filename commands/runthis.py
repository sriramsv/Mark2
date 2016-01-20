__author__ = 'sriram'
from commands import RegexCommand
from utils import tts
import os
from multiprocessing import Process
from config import SCHEDULER,nt,ny
import subprocess
from easygui import enterbox

class RunThis(RegexCommand):

    def __init__(self):
        regex = "(run|execute)( (this)? (at|on|in)? (?P<time>.*))?"
        super(RunThis, self).__init__(regex, False)

    def on_event(self, event, sender):
        m=self.match(event)
        if m:
            if m.group("time"):
                self.when=m.group("time")
                self.when_epoch=nt.parse_natural_time(self.when)
                tts.speak("sir, please enter the full command you wish to execute?")
                self.what=enterbox("command to run at {}".format(self.when_epoch))
                print self.when_epoch
                try:
                    self.remainder=SCHEDULER.add_job(self.runat,'date',run_date=self.when_epoch)

                except ValueError:
                    tts.speak("Could not schedule this run")
            else:
                tts.speak("sir, please enter the full command you wish to execute?")
                self.what=enterbox("command to run")
                comm="gnome-terminal --tab -e {0}".format(self.what)
                self.command(comm)
            return True


    def runat(self):
        tts.speak("Sir,running your specified command")
        self.command(comm)
    def command(self,comm):
        term=subprocess.Popen("gnome-terminal")
        term.wait()
        term.communicate(comm)
    def cancel_run(self):
        self.remainder.remove()