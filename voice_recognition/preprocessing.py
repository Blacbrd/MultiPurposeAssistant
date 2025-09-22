import os
import librosa
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

N_MFCC = 40

# Load one example file
sample = f"{os.getenv("AUDIO_DATA_BACKGROUND_FILE_PATH")}/1.wav"
data, sample_rate = librosa.load(sample)

# len(data) = seconds * sample rate
audio_duration_sec = len(data) / sample_rate

# Plot wave form
plt.title("Wave form")
librosa.display.waveplot(data, sr=sample_rate)
plt.show()

# Hop tells us how often to "look" at the wave
HOP_LENGTH = int(sample_rate * 0.01)    # 10ms hop

mfccs = librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=N_MFCC, hop_length=HOP_LENGTH, n_fft=512)
print(f"Shape of mfcc: {mfccs.shape}")

frames = mfccs.shape[1]
approx_frames_per_sec = sample_rate / HOP_LENGTH

plt.figure(figsize=(8, 3))
plt.title("MFCC")
librosa.display.spaceshow(mfccs, sr=sample_rate, x_axis="time")
plt.colorbar()
plt.show()

all_data = []

data_path_dict = {
    0: ["background/" + file_path for file_path in os.listdir("background/")],
    1: ["wakeword/" + file_path for file_path in os.listdir("wakeword/")]
}

# TODO: Need this explained
for class_label, list_of_files in data_path_dict.items():
    for file in list_of_files:
        data, sample_rate = librosa.load(file)
        mfccs = librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40)
        mfcc_processed = np.mean(mfccs.T, axis=0)
        all_data.append([mfcc_processed, class_label])
    
    print(f"INFO: |Successfully preprocessed class label {class_label}")

df = pd.DataFrame(all_data, columns=["feature", "class_labels"])
df.to_pickle("final_audio_data_csv/audio_data.csv")
