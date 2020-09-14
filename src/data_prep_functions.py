import librosa as lb
import librosa.display
import pandas as pd
import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from pydub import AudioSegment



# 90 bpm = 1.5 bps; 44100 samples per sec, so 66150 samples per beat.
# hop_length set to 44100 (exactly 2/3 of samples per beat) to avoid catcing half-beats
def detect_beats(filepath, hop_length=44100, start_bpm=85, units='time'):
    """Load audio file from given path, detect tempo and beats.
    
    Args:
    filepath (str): location of audio file to read
    hop_length (int, default 44100): number of samples between successive onsets
    start_bpm (int, default 85): initial guess for the tempo estimator

    Returns:
    tempo (int, in bpm), beats (np.ndarray, in milliseconds)
    """
    y, sr = lb.load(filepath)
    tempo, beats = lb.beat.beat_track(y, sr, units='time', start_bpm=start_bpm)

    if not 115 > tempo > 80:
        print('WARNING: tempo detected not between 80 and 115 BPM')
    return tempo, beats * 1000


def group_beats(beats, group_size=2):
    """Delete every nth beat"""
    return beats.reshape(-1,2)[:1:].flatten()


def split_audio_into_bars(filepath, bar_indexes):
    """Split a given wav file into segments based on given start locations."""
    save_name = filepath[:-4]

    audio_file = AudioSegment.from_wav(filepath)

    chunk_list = []
    # save from each index to the next as a separate file
    for i in range(len(bar_indexes) - 1):
        chunk = audio_file[bar_indexes[i]:bar_indexes[i+1]]
        chunk_name = save_name + '_bar_' + str(i), format='wav'
        chunk.export(chunk_name)
        chunk_list.append(chunk_name)

    chunk_name_file = open(save_name + 'chunk_list.csv', 'w')
    

    
    



def save_spectrogram(y, sample_rate, filepath):
    D = lb.stft(y)
    S_db = lb.amplitude_to_db(np.abs(D), ref=np.max())

    fig, ax = plt.subplots()
    lb.display.specshow(S_db, ax=ax)

    fig.save(filepath)
    

def process_all_wavs_in_dir(path):
    for filename in os.listdir(path):
        if filename.endswith('.wav'):
            tempo, beats = detect_beats(path + filename)
            bar_indexes = group_beats(beats)
            split_audio_into_bars(path + filename, bar_indexes)

            chunk_list = 


if __name__ == "__main__":

    path = '/home/ww/Documents/projects/bomba-detection/data/audio/'
    process_all_wavs_in_dir(path)



