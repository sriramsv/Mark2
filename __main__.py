#! /usr/bin/python
from interpreter import *
import pygst
pygst.require('0.10')
import signal
import gobject
import config,sys
from indicator import Indicator
from audio import OnlineRecognizer
from listener import Recognizer,main_loop
scheduler = config.SCHEDULER
interpreter = Interpreter(scheduler=config.SCHEDULER,inq=config.voice_queue,outq=config.results_queue)

class StartProgram(object):
    def __init__(self):
        scheduler.start()
        self.listener=OnlineRecognizer()
        # self.ind=Indicator(self)
    def exit(self):
        print 'shutting down'
        # self.listener.end()
        print 'killed speech recognition'
        scheduler.shutdown()
        interpreter.end()
        # self.ind.quit()
        print 'scheduler stopped'
        print 'interpreter shutdown'
        sys.exit(0)

    def all_start(self):
        interpreter.start()
        # self.ind.start()

    def switch(self,r,text):
        print text.lower()
        r.pause()
        if self.listener.online_recognition():
            r.listen()

if __name__ == "__main__":
    try:
        s=StartProgram()
        s.all_start()
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        r=Recognizer(config.LANG_FILE,config.DIC_FILE)
        r.connect('finished',s.switch)
        r.listen()
        print "starting"
        main_loop.run()
    except KeyboardInterrupt:
        r.pause()
        s.exit()
