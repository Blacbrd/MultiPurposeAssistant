import os
from pathlib import Path
from dotenv import load_dotenv

import sounddevice as sd
from scipy.io.wavfile import write

load_dotenv()

FREQUENCY = 44100
SECONDS = 2

def get_audio_path(isWakeWord: bool, default: str = "") -> str:
    
    if isWakeWord:
        raw = os.getenv("AUDIO_DATA_WAKEWORD_FILE_PATH", default)
    else:
        raw = os.getenv("AUDIO_DATA_BACKGROUND_FILE_PATH", default)

    if raw is None:
        return None
    return str(Path(raw).expanduser())

def record_audio_and_save(amount_of_recordings: int = 100, channels: int = 2):
    input("To start recording audio, press Enter: ")

    for i in range(amount_of_recordings):
        recording = sd.rec(int(SECONDS * FREQUENCY), samplerate=FREQUENCY, channels=channels)
        sd.wait()
        write(get_audio_path(isWakeWord=True) + str(i) + ".wav", FREQUENCY, recording)

        print(f"Currently on: {i + 1}/{amount_of_recordings}")
        input("Press Enter to record next, or Ctrl + C to stop")
        

def record_background_save(amount_of_recordings: int = 100, channels: int = 2):
    input("To start recording background sounds, press Enter: ")

    for i in range(amount_of_recordings):
        recording = sd.rec(int(SECONDS * FREQUENCY), samplerate=FREQUENCY, channels=channels)
        sd.wait()
        write(get_audio_path(isWakeWord=False) + str(i) + ".wav", FREQUENCY, recording)

        print(f"Currently on: {i + 1}/{amount_of_recordings}")

record_audio_and_save()
