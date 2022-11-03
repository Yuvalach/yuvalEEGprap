import os
import mne

def plot_raw(file):
    raw = mne.io.read_raw(file, preload=True)
    raw.pick(['Pz', 'Cz', 'Fz', 'C3', 'C4'])
    raw.plot(duration=4)

