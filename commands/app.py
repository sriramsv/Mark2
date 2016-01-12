#!/usr/bin/python
import re
import os,subprocess
import sys
from utils.tts import speak
from config import broadcast


@broadcast.connect
def on_event(sender,**kw):
    regex="(open|launch)? (?P<app_name>.*?)"
    m=re.match(regex,kw['text'],re.DOTALL)
    if m:
        app_name=m.group('app_name')
        print app_name


