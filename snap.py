import pyaudio
import numpy as np
import pyautogui
import time

# Define constants
CHUNK = 1024
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
THRESHOLD = 0.5  # Snap detection threshold (adjust as needed)

# Function to detect snap sound
def detect_snap(data):
    return np.mean(np.abs(data)) > THRESHOLD

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open default input stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Snap-to-Pause program started. Snap your fingers to pause media.")

while True:
    # Read audio data from stream
    data = np.frombuffer(stream.read(CHUNK), dtype=np.float32)

    # Detect snap sound
    if detect_snap(data):
        # Simulate media play/pause key press
        pyautogui.press('playpause')
        print("Snap detected! Pausing media...")

# Close and terminate PyAudio
stream.stop_stream()
stream.close()
p.terminate()