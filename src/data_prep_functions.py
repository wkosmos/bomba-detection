import librosa as lb
import librosa.display
import pandas as pd
import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from pydub import AudioSegment
import shutil



# 90 bpm = 1.5 bps; 44100 samples per sec, so 66150 samples per beat.
# hop_length set to 44100 (exactly 2/3 of samples per beat) to avoid catcing half-beats
def detect_beats(parent, filename, hop_length=44100, start_bpm=85, units='time'):
    """Load audio file from given path, detect tempo and beats.
    
    Args:
    filepath (str): location of audio file to read
    hop_length (int, default 44100): number of samples between successive onsets
    start_bpm (int, default 85): initial guess for the tempo estimator

    Returns:
    tempo (int, in bpm), beats (np.ndarray, in milliseconds)
    """
    y, sr = lb.load(parent + filename)
    tempo, beats = lb.beat.beat_track(y, sr, units='time', start_bpm=start_bpm)

    if not 115 > tempo > 80:
        print('WARNING: tempo detected not between 80 and 115 BPM')
    return tempo, beats * 1000


def group_beats(beats, group_size=2):
    """Delete every nth beat"""
    return np.delete(beats, slice(None, None, group_size))


def split_audio_into_bars(parent, filename, bar_indexes):
    """Split a given wav file into segments based on given start locations."""
    save_name = parent +'chunks/' + filename[:-4]

    audio_file = AudioSegment.from_wav(parent + filename)

    # gears = np.loadtxt(open(parent + 'gears/' + filename[:-4] + '_gears.csv', 'rb'), delimiter=',')

    chunk_list = []
    # save from each index to the next as a separate file
    for i in range(len(bar_indexes) - 1):
        chunk = audio_file[bar_indexes[i]:bar_indexes[i+1]]
        # if gears[i] == 0:
        #     chunk_name =  save_name + '_bar_' + str(i) + '_0'
        # else:
        #     chunk_name =  save_name + '_bar_' + str(i) + '_1'
        chunk_name =  save_name + '_bar_' + str(i) + '.wav'
        chunk.export(chunk_name, format='wav')
        chunk_list.append(chunk_name)

    return chunk_list


def move_chunks_to_dirs(parent):
    """Move audio chunks to subdirectories based on final character being 1 or 0."""
    files = os.listdir(path=parent)

    for filename in files:
        class_num = filename.split('_')[0][-1]
        if class_num == '0' or class_num == '1':
            shutil.move(parent + filename, parent + '/' + class_num + '/' + filename)
        else:
            pass


def save_spectrogram(filepath, cmap='plasma'):
    """Create spectrogram from audio file at specified path, using specified colormap.
    
    Args:
    filepath (str): location of audio file
    cmap (str): matplotlib cmap name (default 'plasma')
    
    Returns:
    nothing
    """
    y, sr = lb.load(filepath)
    D = lb.stft(y, hop_length=256, n_fft=4096)
    S_db = lb.amplitude_to_db(np.abs(D), ref=np.max)

    fig, ax = plt.subplots()
    lb.display.specshow(S_db, y_axis='log', ax=ax, cmap=cmap)

    fig.savefig(filepath[:-4] + '.png')
    plt.close(fig)
    del fig
    

def all_wavs_in_dir_to_2_beat_chunks(path):
    for filename in os.listdir(path):
        if filename.endswith('.wav'):
            # get tempo and beat indexes from file
            tempo, beats = detect_beats(path, filename)
            # get every 2nd beat index
            bar_indexes = group_beats(beats)
            # split file by bar indexes and save csv list of those chunks
            chunk_list = split_audio_into_bars(path, filename, bar_indexes)
            print('chunk list: ', chunk_list)

            # plot spectrogram of each chunk
            # for chunk in chunk_list:
            #     save_spectrogram(chunk)

            


if __name__ == "__main__":

    path = '/home/ww/Documents/projects/timba-gear-detection/data/audio/400_chunks/1/'

    # all_wavs_in_dir_to_2_beat_chunks(path)
    

    for filename in os.listdir(path):
        if filename.endswith('.wav'):
            save_spectrogram(path + filename)
        



