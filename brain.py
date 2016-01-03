import rivescript,re,os
from utils.tts import speak

from config import ny,BRAIN_DIR
class Brain():
    def __init__(self):
        self.bot = rivescript.RiveScript()
        self.bot.load_directory(BRAIN_DIR)
        self.bot.sort_replies()
        super(Brain, self).__init__("", False)

    def answer(self, event, sender):
        reply=self.bot.reply("localuser", event)
        speak(str(reply))
        ny.show(reply)
        return True