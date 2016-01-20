__author__ = 'sriram'
from commands import RegexCommand
from utils import tts
import os
import alsaaudio

class VolumeControl(RegexCommand):

    def __init__(self):
        regex = "mute|volume (?P<swt>up|down)"
        super(VolumeControl, self).__init__(regex, False)

    def on_event(self, event, sender):
        m=self.match(event)
        if m:
            if m.group()=='mute':
                g = alsaaudio.Mixer()
                g.setvolume(0)
            elif m.group('swt')=='up':
                g=alsaaudio.Mixer()
                vol=int(g.getvolume()[0])
                if vol<100:
                    vol=vol+25
                    if vol<=100:
                        g.setvolume(vol)
            else:
                g=alsaaudio.Mixer()
                vol=int(g.getvolume()[0])
                if vol>0:
                    vol=vol-25
                    if vol>0:
                        g.setvolume(vol)
            return True