from pushbullet import Pushbullet
import requests
import json
import websocket
import time
import logging
import os
import threading
from config import PUSHBULLET_KEY,MESSAGE_FILE,PUSHBULLET_ID,ny,DEVICE_NAME


api_key=PUSHBULLET_KEY





class Pushlistener(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, name="PbThread")
        self.api_key=api_key
        self.pb = Pushbullet(self.api_key)
        self.ws = websocket.WebSocket()
        self.ws.connect("wss://stream.pushbullet.com/websocket/{0}".format(self.api_key))
        self.last_time=0
        self.data=''
        self.setDaemon(True)
        self.interpreters=[]
        self.devices=[x.nickname.encode('UTF-8') for x in self.pb.devices]
        if DEVICE_NAME not in self.devices:
            self.pb.new_device('DEVICE_NAME')

    def run(self):
        while(1):
            self.result=json.loads(self.ws.recv())
            self.res_type=self.result.get("type")
            if self.res_type!='nop':
                self.context_matcher()

		

    def context_matcher(self):
        if self.result.get("type")=='tickle':
            if self.result.get('subtype')=='push':
                pushes = self.pb.get_pushes()
                latest=pushes[1][0]
                if latest.get('target_device_iden')==PUSHBULLET_ID:
                    self.body=latest['body']
                    os.system('mpg321 {0} 2>/dev/null'.format(MESSAGE_FILE))
                    self.notify({'text':self.body})
                    ny.show(self.body)

    def register(self, interpreter):
        """
        Register interpreters to be notified of new input
        """
        if not interpreter in self.interpreters:
            self.interpreters.append(interpreter)

    def unregister(self, interpreter):
        """
        Unregisters an interpreter
        """
        if interpreter in self.interpreters:
            self.interpreters.remove(interpreter)

    def notify(self, event):
        """
        Notify all interpreters of a received input
        """
        for interpreter in self.interpreters:
            interpreter.on_event(event, self)

    def send(self,device,msg):
        for dev in self.pb.devices:
            print dev.nickname
            if dev.nickname==device:
                dev.push_note(msg,None)


