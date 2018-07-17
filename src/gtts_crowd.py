"""
create mp3 of crowd of voices by generating text of a language, then using text
to speech api to make the mp3s that are then layered.

TODO markov chains for more realistic word sequences.

:author: Derek S. Prijatelj
"""

import csv
from os import listdir
from os.path import isfile
from random import randint
import numpy as np
from gtts import gTTS
from pydub import AudioSegment

def get_word_list(lang='en'):
    """ Loads word list for specified language. """
    if lang.lower() == 'en':
        with open('data/english_words.txt', encoding='utf-8') as csvfile:
            content = csv.reader(csvfile, delimiter=' ')

            word_list = []
            probs = []
            for row in content:
                word_list.append(row[0].lower())
                probs.append(float(row[1]))

            probs = np.asarray(probs, dtype=np.float32)
            probs = probs / np.sum(probs)
    elif lang.lower() == 'de':
        with open('data/german_words.txt', encoding='utf-8') as csvfile:
            content = csv.reader(csvfile, delimiter=' ')

            word_list = []
            probs = []
            for row in content:
                word_list.append(row[2].lower())
                probs.append(float(row[1]))

            probs = np.asarray(probs, dtype=np.float32)
            probs = probs / np.sum(probs)
    elif lang.lower() == 'ja':
        with open('data/japanese_words.txt', encoding='utf-8') as csvfile:
            content = csv.reader(csvfile, delimiter=' ')

            word_list = []
            probs = []
            for row in content:
                word_list.append(row[2].lower())
                probs.append(float(row[1]))

            probs = np.asarray(probs, dtype=np.float32)
            probs = probs / np.sum(probs)

    return word_list, probs

def generate_speech(word_list, word_probs, str_len, gender=None, lang='en'):
    utterance = ' '.join(np.random.choice(word_list, str_len, p=word_probs))
    if lang == 'de':
        language = ['de']
    if lang == 'ja':
        language = ['ja']
    else:
        language = ['en-us', 'en-uk', 'en-au']
    return gTTS(utterance, lang=language[randint(0, len(language)-1)])

def generate_random_tts(num_people, lang='en'):
    """ Generates the files to be spoken in the crowd. """
    word_list, probs = get_word_list(lang=lang)
    return [generate_speech(word_list,
        probs,
        int(np.random.normal(24, 4)),
        lang=lang) for x in range(0,num_people)]

def save_tts(tts_list, output_dir, lang='en'):
    for i, tts in enumerate(tts_list):
        tts.save(output_dir + '/' + lang + '/speaker_' + str(i) + '.mp3')

def load_mp3(mp3_dir):
    mp3s = []
    for filename in [x for x in listdir(mp3_dir) if '.mp3' in x]:
        mp3s.append(AudioSegment.from_mp3(mp3_dir + '/' + filename))

    return mp3s

def load_wav(wav_dir):
    wavs = []
    for filename in [x for x in listdir(wav_dir) if '.wav' in x]:
        wavs.append(AudioSegment.from_file(
            os.path.join(wav_dir,filename),
            format='wav')
         )
    return wavs

def create_crowd(mp3_list):
    lengths = [len(x) for x in mp3_list]

    mp3_list = [mp3 for _, mp3 in sorted(zip(lengths, mp3_list), reverse=True,
        key=lambda pair: pair[0])]

    #crowd = AudioSegment.silent(duration=20000)
    #for i, mp3 in enumerate(mp3_list):
        #crowd = crowd.append(mp3, min(len(crowd) - i * 4000, len(mp3)))
        #if i * 4000 >= len(crowd):
        #    break
        #crowd = crowd.overlay(mp3, i * 4000)
    #    crowd = crowd.overlay(mp3)

    crowd = mp3_list[0]
    for i, mp3 in enumerate(mp3_list[1:]):
        crowd = crowd.append(mp3, min(len(mp3),len(crowd)))
    return crowd

def crowd_compile(sound_dir, output_filepath):
    crowd_sound = create_crowd(load_wav(sound_dir))
    crowd_sound.export(output_filepath, format='wav')

def main():
    lang = 'ja'
    speaker_dir = 'results/speakers'
    speaker_num = 30

    save_tts(generate_random_tts(speaker_num, lang), speaker_dir, lang=lang)
    crowd_sound = create_crowd(load_mp3(speaker_dir + '/' + lang))

    crowd_sound.export('results/crowds/' + lang + '/' + lang + '_' \
        + str(speaker_num) + '_overlay.mp3',
        format='mp3')

if __name__ == '__main__':
    main()
