#Creați o aplicație pentru DJ care poate analiza și afișa numărul de bătăi pe minut (BPM) dintr-o piesă audio.

import librosa
import os
import winsound
import threading

def calcul_BPM(file_path):
    y, sr = librosa.load(file_path)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
    return tempo[0]

def asculta(file_path):
    winsound.PlaySound(file_path, winsound.SND_FILENAME)

def priveste(file_path):
    bpm = calcul_BPM(file_path)
    print(f"Numărul de bătăi pe minut (BPM) este: {int(bpm.round())}")

samples={
        "acoustic guitar": os.path.join(os.path.dirname(__file__), "Samples/")+"acoustic-guitar-chords-small-town_66bpm_C_major.wav",
        "doom thrust bass": os.path.join(os.path.dirname(__file__), "Samples/")+"doom-thrust-bass_172bpm_E_minor.wav",
        "groove soul": os.path.join(os.path.dirname(__file__), "Samples/")+"groove-soul-acoustic-guitar-melody_80bpm_D_minor.wav",
        "": os.path.join(os.path.dirname(__file__), "Samples/")+"",
        "": os.path.join(os.path.dirname(__file__), "Samples/")+"",
        "": os.path.join(os.path.dirname(__file__), "Samples/")+"",
        "": os.path.join(os.path.dirname(__file__), "Samples/")+"",
        "": os.path.join(os.path.dirname(__file__), "Samples/")+"",
        "": os.path.join(os.path.dirname(__file__), "Samples/")+""
    }

def main():
    file_path = samples["groove soul"]

    thread1 = threading.Thread(target=asculta, args=(file_path,))
    thread2 = threading.Thread(target=priveste, args=(file_path,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Ambele thread-uri s-au terminat!")

if __name__ == "__main__":
    main()