import pyaudio
import numpy as np
import pyautogui
import time


CHUNK = 1024
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
THRESHOLD = 0.5 

def detect_snap(data):
    return np.mean(np.abs(data)) > THRESHOLD


p = pyaudio.PyAudio()


stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Snap-to-Pause program started. Snap your fingers to pause media.")

while True:
  
    data = np.frombuffer(stream.read(CHUNK), dtype=np.float32)

 
    if detect_snap(data):
       
        pyautogui.press('playpause')
        print("Snap detected! Pausing media...")


stream.stop_stream()
stream.close()
p.terminate()
