import os

import sys
if sys.platform == "windows":
    sys.path.append("H:\stdlib\libs")
else:
    sys.path.append("../libs")

import math
import stdio
import stdarray
import modified_stdaudio as stdaudio

# Read sound samples from standard input, and play the sound to
# standard audio.

SPS = 44100
CONCERT_A = 440.0
NOTES_ON_SCALE = 12.0

while not stdio.isEmpty():

    pitch = stdio.readInt()
    duration = stdio.readFloat()
    hz = CONCERT_A * (2.0 ** (pitch / NOTES_ON_SCALE))
    n = int(SPS * duration)
    note = stdarray.create1D(n+1, 0.0)
    for i in range(n+1):
        note[i] = math.sin(2.0 * math.pi * i * hz / SPS)
    stdaudio.playSamples(note)

stdaudio.wait()