import multiprocessing
import signal
import sys
import threading
from enchant.tokenize import get_tokenizer
import os
from brain import Brain
from config import broadcast





class Interpreter(multiprocessing.Process,Brain):
    def __init__(self, scheduler=None,inq=None,outq=None):
        # multiprocessing.Process.__init__(self)
        super(Interpreter, self).__init__()
        self.tknzr = get_tokenizer("en_US")
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
                print list(self.tknzr(message))
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


