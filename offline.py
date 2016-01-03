import pygtk
pygtk.require('2.0')
import gtk
import os
import gobject
import pygst
pygst.require('0.10')
gobject.threads_init()
import gst,time,speech
from pubsub import pub
conf_dir = os.path.expanduser("~/jarvis")
lang_dir=os.path.join(conf_dir,"language")
language_file = os.path.join(lang_dir,'lm')
dictionary_file = os.path.join(lang_dir,'dic')
from notify.variable import *
import pynotify


class voice():
	def __init__(self):
	    self.init_gst()
	def init_gst(self):
	    """Initialize the speech components"""
	    self.pipeline = gst.parse_launch('gconfaudiosrc ! audioconvert ! audioresample '
	                                     + '! vader name=vad auto-threshold=true '
	                                     + '! pocketsphinx name=asr ! fakesink')
	    asr = self.pipeline.get_by_name('asr')
	    asr.connect('partial_result', self.asr_partial_result)
	    asr.connect('result', self.asr_result)
	    asr.set_property('configured', True)
	    asr.set_property('lm', language_file)
	    asr.set_property('dict', dictionary_file)
	    bus = self.pipeline.get_bus()
	    bus.add_signal_watch()
	    bus.connect('message::application', self.application_message)
	    asr.set_property('configured', True)
	    self.pipeline.set_state(gst.STATE_PAUSED)
	    # pynotify.init("Jarvis")
	    
	def application_message(self, bus, msg):
	    """Receive application messages from the bus."""
	    msgtype = msg.structure.get_name()
	    if msgtype == 'partial_result':
	        self.partial_result(msg.structure['hyp'], msg.structure['uttid'])
	    elif msgtype == 'result':
	        self.final_result(msg.structure['hyp'], msg.structure['uttid'])
	        self.pipeline.set_state(gst.STATE_PLAYING)

	def asr_partial_result(self, asr, text, uttid):
	    """Forward partial result signals on the bus to the main thread."""
	    struct = gst.Structure('partial_result')
	    struct.set_value('hyp', text)
	    struct.set_value('uttid', uttid)
	    asr.post_message(gst.message_new_application(asr, struct))

	def asr_result(self, asr, text, uttid):
	    """Forward result signals on the bus to the main thread."""
	    struct = gst.Structure('result')
	    struct.set_value('hyp', text)
	    struct.set_value('uttid', uttid)
	    asr.post_message(gst.message_new_application(asr, struct))
	    # print text
	    self.result=text.lower()
	    # self.notify("Recognized:{0}".format(self.result))
	    pub.sendMessage("Recognized", arg1=self.result)
	   

	def partial_result(self, hyp, uttid):
	    """Delete any previous selection, insert text and select it."""
	    # All this stuff appears as one single action
	    self.textbuf.begin_user_action()
	    self.textbuf.delete_selection(True, self.text.get_editable())
	    self.textbuf.insert_at_cursor(hyp)
	    ins = self.textbuf.get_insert()
	    iter = self.textbuf.get_iter_at_mark(ins)
	    iter.backward_chars(len(hyp))
	    self.textbuf.move_mark(ins, iter)
	    self.textbuf.end_user_action()

	def final_result(self, hyp, uttid):
	    """Insert the final result."""
	    # All this stuff appears as one single action
	    self.textbuf.begin_user_action()
	    self.textbuf.delete_selection(True, self.text.get_editable())
	    self.textbuf.insert_at_cursor(hyp)
	    self.textbuf.end_user_action()

	def listen(self):
		self.pipeline.set_state(gst.STATE_PLAYING)
		# self.notify("Offline Recognition started")
		
	def pause(self):
		self.pipeline.set_state(gst.STATE_PAUSED)
		# self.notify("Offline Recognition stopped")
		vader = self.pipeline.get_by_name('vad')
		return 0
        #vader.set_property('silent', True)

	def notify(self,title=None,body=None):
		n=pynotify.Notification(title,body)
		n.set_timeout(1000)
		n.show()
