# Winston configuration file
# Read the documentation to learn more about the settings below
from apscheduler.schedulers.background import BackgroundScheduler
import os
from utils import naturaltime,notify
import yaml
import multiprocessing
from blinker import signal
# from commands import date
COMMANDS=list()
voice_queue= multiprocessing.JoinableQueue()
results_queue= multiprocessing.Queue()
SCRIPT_PATH = os.path.dirname(__file__)
MESSAGE_FILE_DIR=os.path.join(SCRIPT_PATH,"sounds")
MESSAGE_FILE=os.path.join(MESSAGE_FILE_DIR,"message.mp3")
FAIL_FILE=os.path.join(MESSAGE_FILE_DIR,"recog-fail.mp3")
BRAIN_DIR=os.path.join(SCRIPT_PATH,"brain")
CONF_DIR=os.path.join(SCRIPT_PATH,"conf")
CONF_FILE=os.path.join(CONF_DIR,"config.yaml")
LANG_DIR=os.path.join(SCRIPT_PATH,"language")
LANG_FILE=os.path.join(LANG_DIR,"lm")
DIC_FILE=os.path.join(LANG_DIR,"dic")
'''object for parsedatetime module'''
nt=naturaltime.NaturalTime()
#init the dbus notify2 API
ny=notify.Notify()
broadcast= signal('Interpreter')
#dict containing all listeners the interpreter is hooked to
SCHEDULER = BackgroundScheduler()
listeners={}
activated=False
with open(CONF_FILE,'r') as conf_file:
    confs=yaml.load(conf_file)

keyword=confs["KEYWORD"]
keywords=keyword.split(',')
PUSHBULLET_ID=confs["PUSHBULLET_ID"]
PUSHBULLET_KEY=confs["PUSHBULLET_KEY"]
GOOGLE_API_KEY=confs["GOOGLE_API_KEY"]
DEVICE_NAME=confs["DEVICE_NAME"]
coordinates=confs["COORDINATES"]
WOLFRAM_KEY=confs["WOLFRAM_KEY"]






# Define your own commands and add them here

