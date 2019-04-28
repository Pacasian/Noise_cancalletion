import librosa
from pysndfx import AudioEffectsChain
import numpy as np
import math
import python_speech_features
import scipy as sp
from scipy import signal



def read_file(file_name):
    sample_file = file_name
    sample_directory = 'samples/'
    sample_path = sample_directory + sample_file

    
    y, sr = librosa.load(sample_path)

    return y, sr

def reduce_noise_power(y, sr):

    cent = librosa.feature.spectral_centroid(y=y, sr=sr)

    threshold_h = round(np.median(cent))*1.5
    threshold_l = round(np.median(cent))*0.1

    less_noise = AudioEffectsChain().lowshelf(gain=-30.0, frequency=threshold_l, slope=0.8).highshelf(gain=-12.0, frequency=threshold_h, slope=0.5)
    y_clean = less_noise(y)

    return y_clean

def trim_silence(y):
    y_trimmed, index = librosa.effects.trim(y, top_db=20, frame_length=2, hop_length=500)
    trimmed_length = librosa.get_duration(y) - librosa.get_duration(y_trimmed)

    return y_trimmed, trimmed_length



def enhance(y):
    apply_audio_effects = AudioEffectsChain().lowshelf(gain=10.0, frequency=260, slope=0.1).reverb(reverberance=25, hf_damping=5, room_scale=5, stereo_depth=50, pre_delay=20, wet_gain=0, wet_only=False)#.normalize()
    y_enhanced = apply_audio_effects(y)

    return y_enhanced


def output_file(destination ,filename, y, sr, ext=""):
    destination = destination + filename[:-4] + ext + '.wav'
    librosa.output.write_wav(destination, y, sr)
    
    samples = ['01_counting.m4a','02_wind_and_cars.m4a','03_truck.m4a','04_voices.m4a','05_ambeint.m4a','06_office.m4a']

for s in samples:
 
    filename = s
    y, sr = read_file(filename)

    
    y_reduced_power = reduce_noise_power(y, sr)
    

    # trimming silences
    y_reduced_power, time_trimmed = trim_silence(y_reduced_power)


    
    output_file('output/' ,filename, y_reduced_power, sr, '_pwr')
    output_file('output/' ,filename, y, sr, '_org')