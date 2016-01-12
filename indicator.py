import os
import signal
import appindicator
import gtk
import multiprocessing
APPINDICATOR_ID = 'Jarvisappindicator'
from Tkinter import *
# from gi.repository import GObject
from signal import SIGTERM
from config import voice_queue

window=False

class EntryClass():
    def __init__(self):
        self.top = Tk()
        self.top.title("Assistant")
        self.top.geometry('+860+10')
        self.entryVar = StringVar()
        self.entryVar.set("Enter Text Here")
        self.entry = Entry(self.top,width=20, textvariable=self.entryVar)
        self.entry.bind('<FocusIn>', (lambda event: self.entryVar.set('')))
        self.entry.bind('<FocusOut>', (lambda event: self.entryVar.set('Enter query here')))
        self.entry.pack(side = RIGHT)
        self.entry.bind('<Return>', (lambda event: self.get_entry()))
        self.top.protocol("WM_DELETE_WINDOW", self.quit)

    def run(self):
        try:
            self.top.mainloop()
        except KeyboardInterrupt:
            self.quit()
    def get_entry(self):
        voice_queue.put(self.entryVar.get().lower())

    def quit(self):
        window=False
        self.top.destroy()

# Gtk.main()
class Indicator(multiprocessing.Process):

    def __init__(self,mainp):
        self.mainp=mainp
        multiprocessing.Process.__init__(self)
        self.e=EntryClass()
        self.indicator = appindicator.Indicator(APPINDICATOR_ID,os.path.abspath("icons/ind.ico"),appindicator.CATEGORY_APPLICATION_STATUS)
        self.indicator.set_status(appindicator.STATUS_ACTIVE)
        self.indicator.set_menu(self.create_menu())

    def create_menu(self):
        menu = gtk.Menu()
        entry=gtk.MenuItem('Query')
        entry.connect('activate', self.enter)
        item_quit = gtk.MenuItem('Quit')
        item_quit.connect('activate', self.quit)
        menu.append(entry)
        menu.append(item_quit)
        menu.show_all()
        return menu

    def enter(self,source):

        self.e.run()
        window=True

    def main_quit(self):
        if window:
            self.e.quit()
        os.kill(self.pid,SIGTERM)
        # self.mainp.exit()

    def quit(self,source):
        self.main_quit()

    def run(self):
        # gtk.main()
        print "Indicator PID:", self.pid


