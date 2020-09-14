import librosa as lb
import numpy as np

class LibrosaAudioFile():

    def __init__(self, path):
        """Initialize an audio file loaded from the given path, detect the beats in the file."""
        self.y, self.sr = lb.load(path)
        self.detect_beats()
        
    
    def detect_beats(self):
        """Gets tempo (float) and beats (array).
        Preset hop-length and start_bpm for average timba included.
        """
        self.tempo, self.beats = lb.beat.beat_track(y=self.y,  sr=self.sr, hop_length=44100, start_bpm=90)
