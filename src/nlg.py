"""
All NLG methods and an interface to select between them.

:author: Derek S. Prijatelj
"""

import csv
import random
import numpy as np
import pandas as pd
import markovify

def frequency(sentence_length, frequencies=None, lang='en', filepath=None):
    """
    Basic word frequency NLG method.
    :param sentence_length: Length of the sentence
    :param lang: Language of the sentence produced
    :param frequencies: mapping of word to frequency, otherwise data file used.
    """
    return

def markov_chain(sentence_length, n=2, lang='en'):
    """
    Markov Chain NLG method of sentence generation.

    Selects the first word using frequency distribution.
    Then uses N-grams (N defaults to 2) to determine next state(s).
    Creates to specified length, then stops. Ensures that proper N-Gram length
    is used based on sentence length.
    """

    # static N-Gram method,
    # growing N-Gram method, where the other N-Gram freqs are used as space in
    # the sentence length provides. 1 word slected from word freqs, then next
    # based on  bigrams, then trigrams, etc... If a gram doesn't exist, then
    # bigrams is defaulted to.

    # perhaps google ngram corpus as well?

    return

def markov_chain_ngram(max_length, n=5, num_sentences=1, lang='en'):
    # TODO test and fix
    assert max_length >= n

    # load ngram chains
    ngram_chain = [load_ngram_chain(N, lang) for N in range(2,6)]

    print('loaded ngram chain')

    # generate sentences
    sentences = []

    # growing method, uses all ngram data
    for i in range(0,num_sentences):
        key = random.choice(list(ngram_chain[0].keys()))
        sentence = key.capitalize()

        words = sentence.split(' ')
        while len(words) < max_length:
            ngram_df = ngram_chain[len(words)-1][key]

            print(
                np.random.choice(
                    np.asarray(ngram_df['word']),
                    1,
                    np.asarray(ngram_df['freq'])
                )[0]
            )

            sentence += ' ' + \
                np.random.choice(
                    np.asarray(ngram_df['word']),
                    1,
                    np.asarray(ngram_df['freq'])
                )[0]

            words = sentence.split(' ')

            if len(words) <= n:
                key = sentence
            else:
                key = ' '.join(words[-n:len(words)])

            while key not in ngram_chain[len(words)-1]:
                key = key[key.find(' ') + 1:]
        sentences.append(sentence)
    return sentences

def markov_chain_static_n(length, n, size, lang='en'):
    assert max_length >= n

    # load ngram chains
    ngram_chain = load_ngram_chain(n, lang)

    print('loaded ngram chain')

    # generate sentences
    sentences = []

    for i in range(0,num_sentences):
        key = random.choice(list(ngram_chain.keys()))
        sentence = key

        words = sentence.split(' ')
        while len(words) < max_length:
            ngram_df = ngram_chain[key]
            sentence += ' ' + \
                np.random.choice(ngram_df['word'], 1, p=probs)[0]

            words = sentence.split(' ')
            key = ' '.join(words[-(n-1):len(words)])
        sentences.append(sentence)
    return sentences

# Explicitly provided dialogue/sentences or large string to be broken down.

def load_ngram_chain(n, lang):
    if lang not in ['en','es','de','jp','zh']:
        return None

    # TODO use pandas
    #df = pd.read_table('../data/' + lang + '/ngrams_coca/w' + str(n) + '_.txt')



    #"""
    with open('../data/' + lang + '/ngrams_coca/' + str(n) + 'gram_case_pos.txt',
            encoding='utf-8') as ngram_file:
        content = csv.reader(ngram_file, delimiter='\t')

        ngram_chain = {}
        for line in content:
            key = ' '.join(line[1:n])
            if key in ngram_chain:
                ngram_chain[key].append(pd.DataFrame({
                    'word': [line[n]],
                    'freq': int(line[0])
                }))
            else:
                ngram_chain[key] = pd.DataFrame({
                    'word': [line[n]],
                    'freq': int(line[0])
                })

        ngram_df['freq'] = ngram_df['freq'] / ngram_df['freq'].sum()

        print("finished one ngram_chain, n = " + str(n))
        print(ngram_chain.keys())
        return ngram_chain
    #"""
    return None

def markov_chain_syntax(max_length, n, num_sentences=1, lang='en')
    """
    Markov Chain based on syntax alone. Words of correct syntax are filled into
    the choosen syntax spots.
    """
    return

def markov_chain_text(max_length, num_sentences=1, text=None, lang='en'):
    # load ngrams (or be ready with them)
    text_model = markovify.Text(text)

    sentences = []
    for i in range(num_sentences):
        sentences.append(text_model.make_short_sentence(max_length))

    return sentences

def main():
    sentences = markov_chain_static_n(8, 2, num_sentences=10)
    print(sentences)

if __name__ == '__main__':
    main()
