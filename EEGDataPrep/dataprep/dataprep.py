import os
import mne


def plot_raw(file):
    raw = mne.io.read_raw(file, preload=True)
    raw.pick(['Pz', 'Cz', 'Fz', 'C3', 'C4'])
    bandpass_filter(raw)
    raw.plot(duration=4)
    return raw


# Step One functions
# ---------------------------
# Bandpass, high pass, low pass, re-referencing, picking bad channels
def step1(file):  # file to str of file location
    raw = mne.io.read_raw(file, preload=True)
    raw.pick(['Pz', 'Cz', 'Fz', 'C3', 'C4'])
    bandpass_filter(raw)
    rereference(raw)
    print('-------------------------------------')
    print('Pick bad filters')
    raw.plot(duration=4)
    return raw


# Bandpass filter function
def bandpass_filter(raw):
    # Filtering to low-pass and high-pass, picking specific electrodes
    raw.filter(l_freq=1, h_freq=40)
    raw.resample(sfreq=250)
    freqs = (60, 120, 180, 240)
    raw.notch_filter(freqs=freqs, picks='eeg', method='spectrum_fit', filter_length='4s')


def rereference(raw):
    # Using Cz as reference, it has bad signaling due to its location
    raw.set_eeg_reference(ref_channels=['Cz'])

