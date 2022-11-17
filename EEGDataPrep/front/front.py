from tkinter import *
from tkinter.filedialog import askopenfilename
from EEGDataPrep.dataprep.dataprep import *


# Class of software window
# We can create as many windows as we wish
# You can create instances through runner.py
# ---------------------------
class MyWindow:
    def __init__(self, win):
        # Creating the visuals
        # ---------------------------
        # Labels
        self.lblTitle = Label(win, font="Helvetica 16 bold", text='BRAINPUT - EEG Raw data Processor')
        self.lblSubtitle = Label(win, text='Choose your EEG data')
        self.lblBtnLeft = Label(win, font="Helvetica 14 bold", text='Create plots from file')
        self.lblBtnRight = Label(win, font="Helvetica 14 bold", text='Process Your File')
        self.lblStep1 = Label(win, text='Bandpass, re-referencing & Channel inspection')
        self.lblStep2 = Label(win, text='Removing bad channels, epoching, inspecting epochs,')
        self.lblStep2a = Label(win, text='ICA & Save processed file')
        # Buttons
        self.btnOpenFile = Button(win, text='Load File', command=self.select_file)
        self.btnRawPlot = Button(win, text='Plot Raw', command=self.create_plot)
        self.btnStep1 = Button(win, text='Step one', command=self.first_step)
        self.btnStep2 = Button(win, text='Step two', command=self.second_step)
        # EEG file loaded by user
        # ---------------------------
        self.selectedFile = "No file loaded"
        self.midProcess = mne.create_info(4, sfreq=40)
        # Placing the objects
        # ---------------------------
        # Labels
        self.lblTitle.place(x=20, y=50)
        self.lblSubtitle.place(x=20, y=90)
        self.lblBtnLeft.place(x=20, y=140)
        self.lblBtnRight.place(x=240, y=140)
        self.lblStep1.place(x=300, y=180)
        self.lblStep2.place(x=300, y=220)
        self.lblStep2a.place(x=300, y=240)
        # Buttons
        self.btnOpenFile.place(x=170, y=90)
        self.btnRawPlot.place(x=20, y=180)
        self.btnStep1.place(x=240, y=180)
        self.btnStep2.place(x=240, y=220)

    # Triggered when Load File is pressed
    def select_file(self):
        # All file types working with the software
        filetypes = (
            ('set files', '*.set'),
            ('BrainVision files', '*.vhdr'),
            ('BrainVision files', '*.vmrk'),
            ('BrainVision files', '*.eeg'),
            ('European data format files', '*.edf'),
            ('BioSemi data format files', '*.bdf'),
            ('General data format files', '*.gdf'),
            ('Neuroscan CNT files', '*.cnt'),
            ('EGI simple binary files', '*.egi'),
            ('EGI MFF files', '*.mff'),
            ('EEGLAB files', '*.set'),
            ('EEGLAB files', '*.fdt'),
            ('Nicolet files', '*.data'),
            ('eXimia EEG data files', '*.nxe'),
            ('Persyst EEG data files', '*.lay'),
            ('Persyst EEG data files', '*.dat'),
            ('Nihon Kohden EEG data files', '*.21e'),
            ('Nihon Kohden EEG data files', '*.pnt'),
            ('Nihon Kohden EEG data files', '*.log'),
            ('Nihon Kohden EEG data files', '*.21e'),
            ('XDF EEG data files', '*.xdf'),
            ('XDF EEG data files', '*.xdfz'),
            ('Elekta NeuroMag data files', '*.fif')
        )
        self.selectedFile = askopenfilename(filetypes=filetypes, title='Open a file')

    # Triggered when Plot Raw is pressed
    def create_plot(self):
        plot_raw(self.selectedFile)

    def first_step(self):
        self.midProcess = step1(self.selectedFile)

    def second_step(self):
        print('here we will have second step')
