import subprocess
from get_answer import Fetcher


class Commander:
    def __init__(self):
        self.exit = ["quit", "goodbye", "exit", "bye"]
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "cancel", "negative", "don't", "wait"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("You haven't told your name is..")
            else:
                self.respond("My name is PyBot.")
        else:
            f = Fetcher("https://www.google.co.uk/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)

    def respond(self, response):
        subprocess.call('echo ' + response + ' | "C:\Program Files\Jampal\ptts.vbs"', shell=True)
