"""
A simple program that generates a mp3 audio file of multiple voices speaking
filler english over one another to simulate the noise from a background crowd of
voices speaking. This is to be able to speak in any language, so that any langauge of crowd background noise may be generated.

:author: Derek S. Prijatelj
"""

import pyttsx3
from gtts import gTTS

engine = pyttsx3.init()
voices = engine.getProperty('voices')
english_voices = [v for v in voices if any('en' in x for x in v.languages)]

def simple_crowd():
    def other_speak(name, location, length):
        print('word', name, location, length)
        if location > 10:
            engine.setProperty('voice', voices[8])

    engine.connect('started-word', other_speak)
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()

def add_say(name, location, length):
    if location > 10:
        engine.say('Yo, I just added this phrase boyo!')
        engine.runAndWait()

def onEnd(name, completed):
    if not completed:

def main():
    #engine.connect('started-word', add_say)



if __name__ == '__main__':
    main()
