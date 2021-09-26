# -*- coding: utf-8 -*-
import pyttsx3

# mac でしゃべらせる。
class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty("voice", "com.apple.speech.synthesis.voice.kyoko.premium")
        self.engine.setProperty("rate", 400)

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
