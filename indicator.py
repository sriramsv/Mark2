import os
import signal
import appindicator
import gtk
import multiprocessing
APPINDICATOR_ID = 'Jarvisappindicator'


class Indicator(multiprocessing.Process):
    def __init__(self,mainp):
        multiprocessing.Process.__init__(self)
        self.main=mainp
        self.indicator = appindicator.Indicator(APPINDICATOR_ID,os.path.abspath("icons/ind.ico"),appindicator.CATEGORY_APPLICATION_STATUS)
        self.indicator.set_status(appindicator.STATUS_ACTIVE)
        self.indicator.set_menu(self.create_menu())


    def create_menu(self):
        menu = gtk.Menu()
        self.item_listen = gtk.ToggleButton(label="Listening", use_underline=True)
        self.item_listen.connect('activate', self.listen)
        menu.append(self.item_listen)
        item_quit = gtk.MenuItem('Quit')
        item_quit.connect('activate', self.quit)
        menu.append(item_quit)
        menu.show_all()
        return menu

    def listen(self,source):
        if self.item_listen.get_label()=="Start Listening":
            self.item_listen.set_label("Stop Listening")
        elif self.item_listen.get_label()=="Stop Listening":
            self.item_listen.set_label("Start Listening")


    def quit(self,source):
        gtk.main_quit()

    def run(self):
        print "Indicator PID:", self.pid
        gtk.main()

