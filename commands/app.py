#!/usr/bin/python
import re
import os,subprocess
import sys,speech
import easygui as g
from commands import RegexCommand
from utils import tts

class OpenApp(RegexCommand):
    def __init__(self):
        """
        Build the basic regex command
        """
        regex = 'open (?P<app_name>.*)'
        super(OpenApp, self).__init__(regex,False)

    def on_event(self, event, sender):
        m=self.match(event)
        if m:
            app_name=m.group('app_name')
            index=open('/usr/share/applications/bamf-2.index','r')
            f=index.readlines()
            app_paths=[]
            app_names=[]
            for line in f:
                match=re.search(app_name,line,re.DOTALL)
                if match!=None:
                    path=line.split('\t')
                    path1=[x for x in path if x!='']
                    command=path1[1]
                    app=path1[0].strip('.desktop')
                    if '%U' in command:
                        command=command.strip('%U')
                    if '%u' in command:
                        command=command.strip('%u')
                    app_names.append(app)
                    app_paths.append(command)


            if len(app_names)==1:
        		# speech.say("opening {0}".format(app_names[0]))
                comm=app_paths[0]+'&'+'2>/dev/null'
                self.call(comm)
            elif len(app_names)>1:
                command=g.choicebox("choose from these apps","",app_names)
                if command!=None:
                    index=app_names.index(command)
                    comm=app_paths[index]+'&'+'2>/dev/null'
                    self.call(comm)

            else:
                tts.speak("No app found")
            return True
        else:
            return False
    def call(self,app):
	    subprocess.call(app,shell=False)
