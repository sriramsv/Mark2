import re
import multiprocessing
import os
import sys,signal,threading
from brain import Brain
from config import ny,COMMANDS


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
                next_task = self.inq.get()
                print "Got New Word from Queue:",next_task
                for command in COMMANDS:
                     command.on_event(next_task,self)


        except KeyboardInterrupt:
            if not self.inq.empty():
                self.inq.task_done()
            sys.exit()

    def end(self):
        self.stop.set()
        os.kill(self.pid,signal.SIGSTOP)

