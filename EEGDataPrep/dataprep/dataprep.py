import os
import mne
from mne.preprocessing import ICA


def plot_raw(file):  # presenting the raw data file
    raw = mne.io.read_raw(file, preload=True)  # uploading an EEG file
    raw.pick(['Pz', 'Cz', 'Fz', 'C3', 'C4'])  # choosing main channels
    bandpass_filter(raw)
    raw.plot(duration=4)  # setting the sampling time
    return raw


def plot_processed_file(file):
    data = mne.read_epochs(file, preload=True)
    data.plot(duration=4)
    return data


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
    freqs = (60, 120, 180, 240)  # setting the frequencies to filter
    raw.notch_filter(freqs=freqs, picks='eeg', method='spectrum_fit', filter_length='4s')


def rereference(raw):
    # Using Cz as reference, it has bad signaling due to its location
    raw.set_eeg_reference(ref_channels=['Cz'])


def step2(raw, file):
    # Removing bad channels and marking bad segments
    inspect_bads(raw)
    ica_analysis(raw)
    epochs = epoching(raw, True)
    print("---------------------------------")
    print("Pick bad epochs")
    epochs.plot()
    return epochs


def inspect_bads(raw):
    print("---------------------------------")
    if len(raw.info['bads']) > 0:
        raw.pick(picks='eeg', exclude="bads")
        print("Removed bad channels picked in step one")
    else:
        print("No bad channels picked")


def epoching(raw, reject):
    # filtering bad segments
    events = mne.make_fixed_length_events(raw, start=5, duration=2.5)
    if reject:
        reject_criteria = dict(eeg=150e-6)  # 250 µV
        return mne.Epochs(raw, events, reject=reject_criteria, tmin=-0.2, tmax=0.5, preload=True)
    else:
        return mne.Epochs(raw, events, tmin=-0.2, tmax=0.5, preload=True)


def ica_analysis(raw):
    ica = ICA(method='fastica', max_iter='auto')
    ica.fit(raw)
    return ica.apply(raw)


def save_processed_epochs(epochs, file):
    processed_file_name = f"Processed - {file.rsplit('/', 1)[-1].split('.')[0]}-epo.fif"
    epochs.save(fname=processed_file_name, overwrite=True)
    os.rename(processed_file_name, f"../data/preprocessed/{processed_file_name}")
