import librosa as lb
import librosa.display
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


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
    """Delete every 2nd beat"""
    return beats.reshape(-1,2)[:1:].flatten()


def save_spectrogram(y, sample_rate, ):
    D = lb.stft(y)
    S_db = lb.amplitude_to_db(np.abs(D), ref=np.max())

    fig, ax = plt.subplots()
    img = lb.display.specshow(S_db, ax=ax)

    fig.save('/home/ww/Documents/projects/bomba-detection/data/' + )
    


def process_all_wavs_in_dir():
    pass

if __name__ == "__main__":

    path = '/home/ww/Documents/projects/bomba-detection/data/audio/'
    # for filename in os.listdir(path):
    #     if filename.endswith('.wav'):
    #         tempo, beats = detect_beats(path + filename)
    #         print('detected tempo for ' + filename + ': ' + str(tempo))
    #         np.savetxt('test.csv', beats, delimiter=',', fmt='%f')
    #     else:
    #         continue



    test_file = '/home/ww/Documents/projects/bomba-detection/data/audio/El Bla Bla Bla - Charanga habanera.wav'

    y, sr = lb.load(test_file)

    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
    D = librosa.stft(y)  # STFT of y
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
    plt.figure()
    librosa.display.specshow(S_db)
    plt.colorbar()