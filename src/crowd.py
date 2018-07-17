import espeak
import nlg
from random import randint
import gtts_crowd

if __name__ == '__main__':
    sentences = nlg.markov_chain_text(100,'/home/magic/Downloads/moby.txt', num_sentences=50, lang='en')
    fullText = ''
    sentenceNumber = 0
    for sentence in sentences:
        pitchA = randint(60,140)
        espeak.espeak(sentence,'/home/magic/crowdnoise/crowd_noise/data/voice-output/individuals/sample'+str(sentenceNumber),name='sample'+str(sentenceNumber),
        pitch=(pitchA,randint(pitchA,pitchA+50)),formant=None,echo=None,tone=(600,170,1200,135,2000,110),
        flutter=randint(1,15),roughness=randint(0,5),voicing=randint(25,250),consonants=(randint(75,125),randint(75,125)),breath=None, 
        breathw=None, speed=randint(90,110), language='en', gender='male')
        sentenceNumber = sentenceNumber + 1
    gtts_crowd.crowd_compile('/home/magic/crowdnoise/crowd_noise/data/voice-output/individuals/','/home/magic/crowdnoise/crowd_noise/data/voice-output/crowd.wav')
