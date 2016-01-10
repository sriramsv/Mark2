from utils.tts import speak, spell_integer
from datetime import datetime
from random import choice
import re
from config import broadcast




@broadcast.connect
def on_event(sender,**kw):
    """
    Reads the date or the time
    """
    reg=re.match(r'date',kw['text'],re.DOTALL)
    if reg:
        intro = ('The date is','Today is',)
        date = datetime.now().strftime("%B %d,%yyyy")
        readable_date = "{0} {1}".format(choice(intro), date)
        speak(readable_date)


    reg=re.match(r'time',kw['text'],re.DOTALL)
    if reg:
        time=datetime.now()
        now=time.strftime("%-I:%M %P")


        intro = (
            'The time is',
            'It is',
            'It currently is',
            'The current time is',
        )
        readable_time = "{0} {1}".format(choice(intro),now)
        speak(readable_time)