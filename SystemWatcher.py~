
import datetime
import dbus
import gobject,time
from dbus.mainloop.glib import DBusGMainLoop
from utils.tts import speak

from config import nt
suspend_time=0;
awake_time=0;


def GetTime(seck):
    diff=[]
    sec = datetime.timedelta(seconds=int(seck))
    d = datetime.datetime(1,1,1,1,1) + sec


    if (d.year-1)>0:
        diff.append("{} years".format(d.year-1))
    if (d.month-1)>0:
        diff.append("{} months".format(d.month-1))
    if (d.day-1)>0:
        diff.append("{} days".format(d.day-1))
    if (d.hour-1)>0:
        diff.append("{} hours".format(d.hour-1))
    if (d.minute-1)>0:
        diff.append("{} minutes".format(d.minute-1))
    if (d.second)>0:
        diff.append("{} seconds".format(d.second))
    return  ', '.join(diff)


def handle_sleep(*args):
    global suspend_time,awake_time
    if str(args[0])=='1':
        speak("See you soon,sir!")
        suspend_time=time.time()
        dtime=GetTime(awake_time-suspend_time)
        print dtime
        speak("sir!,you were logged in for {}".format(dtime))
    elif str(args[0])=='0':
        awake_time=time.time()
        dtime=GetTime(awake_time-suspend_time)
        print dtime
        speak("sir!, welcome back, you are back after {}".format(dtime))

DBusGMainLoop(set_as_default=True)     # integrate into gobject main loop
bus = dbus.SystemBus()                 # connect to system wide dbus
bus.add_signal_receiver(               # define the signal to listen to
    handle_sleep,                      # callback function
    'PrepareForSleep',                 # signal name
    'org.freedesktop.login1.Manager',  # interface
    'org.freedesktop.login1'           # bus name
)

loop = gobject.MainLoop()
loop.run()

