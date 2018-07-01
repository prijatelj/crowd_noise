
"""

eSpeak Unit Tester

@author Matthew "SpudManTwo" Kaufman

"""

import os

#Get eSpeak Code Path

workingDirectory = os.path.dirname(os.path.realpath(''))

srcDirectory = os.path.join(workingDirectory,'src')

espeakFile = os.path.join(srcDirectory,'espeak.py')

#Load Code

import importlib.util

spec = importlib.util.spec_from_file_location("espeak", espeakFile)

src = importlib.util.module_from_spec(spec)

spec.loader.exec_module(src)

#from espeakFile import espeak

if __name__ == '__main__':

    #Regular Espeak Test

    print('Testing Regular espeak call')

    src.espeak('All hail glow cloud. All hail glow cloud. All hail glow cloud.', '/home/magic/crowdnoise/crowd_noise/data/voice-output/regular')

    #random_espeak Test

    print('Testing random_espeak')

    src.random_espeak('All hail glow cloud. All hail glow cloud. All hail glow cloud.', '/home/magic/crowdnoise/crowd_noise/data/voice-output/random')
