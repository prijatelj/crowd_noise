Crowd Noise Generation
==
Background crowd noise generator from a provided corpora of text and text to speech (TTS) API(s).

Hackathon Version:
1. randomly concatentates words from a list of words with respective frequencies.
2. creates individual utterances/speakers as .mp3 files
3. loads the mp3 files from one directory and overlays/appends them randomly to create a background crowd noise.

libraries used:
- pydub
- gtts

Related Work
--
- Babble Noise : https://mynoise.net/NoiseMachines/babbleNoiseGenerator.php


Conference Paper Version ToDo:
==
+ Improve Audio Qualities
    - research the libraries for use in audio synthesizing, signal processing, and text-to-speech
    - Include more text-to-speech voices
    - Make them more natural sounding (if not done in above tasks)
+ Improve NLG
    - Apply Markov Chain for more realistic word phrases
    - Allow use of explicit dialogue
+ Analysis:
    - gather datasets of crowd noise
    - perform signal analysis to compare our generated crowd noise to actual recorded crowd noise
    - spectrum analysis

bonus:
- make GUI for custom crowd noise generation (this exists to some extent so we must surpass it)

Libraries to use possibly:
- pydub?
- audioop?
- scipy.signal
- Text-to-Speech:
    + gtts (google text-to-speech Api)
    + pyttsx/pyttsx3
    + IBM Watson TTS (potential pay)
    + Amazon Polly (requires AWS account and potentail pay)
    + Festival : https://en.wikipedia.org/wiki/Festival_Speech_Synthesis_System
        - Festvox
        - Flite
    + WaveNet (google's thing for tts in tensorflow)
    + Deep-Voice (https://arxiv.org/abs/1702.07825)

Links of Use
--
- Audio in python:
    + https://github.com/faroit/awesome-python-scientific-audio
    + https://wiki.python.org/moin/Audio/
    + https://wiki.python.org/moin/PythonInMusic
- TTS:
    + https://deepmind.com/blog/wavenet-generative-model-raw-audio/
        - https://github.com/tensorflow/magenta/tree/master/magenta/models/nsynth
    + https://github.com/israelg99/deepvoice
    + https://github.com/festvox
