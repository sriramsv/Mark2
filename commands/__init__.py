import re

class Command(object):
    """
    Stores a command that is executed by external events such as a voice command,
    a change of state or a notification.
    """

    # The name with which all commands begin. Can be a word or a regex.
    # Example: jenkins, alfred, robot. "Jenkins! Turn on the lights!"
    signal = "jarvis"

    def on_event(self, event, sender):
        """
        Handles events from the interpreter and other sources
        """
        # Do something here.

class RegexCommand(Command):

    prefixes = "(can you|could you)?(please)?"
    suffixes = "(please)?"
    def __init__(self, regex, polite=False):
        super(RegexCommand, self).__init__()
        if polite:
            final_regex = "{signal}{prefix} {command}{suffix}".format(
                signal = self.signal,
                command = regex,
                prefix = self.prefixes,
                suffix = self.suffixes,
            )
            self.regex = re.compile(final_regex)
        else:
            self.regex = re.compile(regex)

    def match(self, text):
        text=str(text)
        match1=self.regex.match(text)
        return match1

