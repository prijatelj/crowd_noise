"""
Example audio analysis script. Performs basic spectrum analysis and generates
graphics with scipy and matplotlib.

TODO: tweak parameters of spectrogram and periodogram in order to generate 
      more informative graphics

TODO: explore more options for visualizing power spectral density; stft etc.

:author: Tim Ireland
"""

import os
import scipy.signal as signal
import matplotlib.pyplot as plt 
import matplotlib.colors as colors
import numpy as np
from argparse import ArgumentParser
from pydub import AudioSegment
from IPython.core.debugger import Tracer

def analyze(audio,verbose=False):
    """Perform spectrum analysis on an AudioSegment and render associated graphics"""

    #NOTE:performs a split to mono; technically only captures dynamics of left channel
    audio_arr = np.asarray(audio.split_to_mono()[0].get_array_of_samples())
    sampling_freq = audio.frame_rate
    
    ### Plot a periodogram
    if verbose: print("Generating periodogram with log scaling")
    f, Power = signal.periodogram(audio_arr, fs=sampling_freq)
    plt.semilogy(f, Power)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('Power Spectral Density [V**2/Hz]')
    plt.show()

    ### Plot a spectrogram
    if verbose: print("Generating spectrogram with log-scaling")
    f,t,Spec_density = signal.spectrogram(audio_arr,fs=sampling_freq)
    plt.pcolormesh(t, f, Spec_density,norm=colors.LogNorm())
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()

    if verbose: print("Done!")


if __name__ == '__main__':

    parser = ArgumentParser(description="Perform spectrum analysis on a mp3 file")
    parser.add_argument('--file','-f', type=str, help="Name of results file to be analyzed")
    parser.add_argument('--verbose','-v', action='store_true', help="Increases verbosity")

    args = parser.parse_args()
    file_path = os.path.join(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0],"results",args.file)

    if args.verbose: print("Attempting to read mp3 file at: "+file_path)
    audio_file = AudioSegment.from_mp3(file_path)

    if args.verbose: print("Beginning analysis")
    analyze(audio_file,verbose=args.verbose)

