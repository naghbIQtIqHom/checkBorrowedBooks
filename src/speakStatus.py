# -*- coding: utf-8 -*-
from TextToSpeech import TextToSpeech

class speakStatus:
    def __init__(self):
        self.voice = TextToSpeech()

    def rentBooks(self, name, rents):
        numberOfBooks = len(rents.keys())
        msg = "%sで現在借りている本は全部で%d冊です。" % (name, numberOfBooks)
        self.voice.say(msg)
        i = 1
        for k,v in rents.items():
            msg = "{0}冊目、{1}は返却日{2}です。".format(i, k, v)
            self.voice.say(msg)
            i = i + 1

    def reserveBooks(self, name, reserves):
        numberOfBooks = len(reserves.keys())
        msg = "%sで予約している本は全部で%d冊です。" % (name, numberOfBooks)
        if numberOfBooks > 0:
            self.voice.say(msg)
            i = 1
            for k,v in reserves.items():
                msg = "{0}冊目{1}は{2}。".format(i, k, v)
                self.voice.say(msg)
                i = i + 1

    def endThatsit(self, name):
        msg = "{0}で借りている本は以上です。".format(name)
        self.voice.say(msg)
