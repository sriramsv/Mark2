import multiprocessing
import signal
import sys
import threading

import os
from brain import Brain
from config import broadcast


# import smokesignal


class Interpreter(multiprocessing.Process,Brain):
    def __init__(self, scheduler=None,inq=None,outq=None):
        # multiprocessing.Process.__init__(self)
        super(Interpreter, self).__init__()
        print "I:",self.name
        self.scheduler = scheduler
        self.inq=inq
        self.outq=outq
        self.daemon = True
        self.stop=threading.Event()

    def run(self):
        print "starting Interpreter"
        print "Interpreter Process:", self.pid
        try:
            while not self.stop.isSet():
                message = self.inq.get()
                print "Got New Word from- Queue:",message
                broadcast.send(text=message)

        except KeyboardInterrupt:
            if not self.inq.empty():
                self.inq.task_done()
            sys.exit()


    def end(self):
        self.stop.set()
        os.kill(self.pid,signal.SIGSTOP)

    def keyword_extract(self,message):
        message.split()


# @broadcast.connect
# def date_event(sender,**kw):
#     """
#     Reads the date or the time
#     """
#     print "Hello",kw
#     # intro = (
#     #     'The date is',
#     #     'Today is',
#     # )
#     # date = datetime.now().strftime("%B %d")
#     # readable_date = "{0} {1}".format(choice(intro), date)
#     # speak(readable_date)