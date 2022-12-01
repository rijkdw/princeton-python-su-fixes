import sys
if sys.platform == "windows":
    sys.path.append("H:\stdlib\libs")
else:
    sys.path.append("../libs")

import modified_stdaudio as stdaudio
import stdarray

import math


SPS = 44100                   # samples per second
hz = 440.0                    # concert A
duration = 10.0               # ten seconds
n = int(SPS * duration)
a = stdarray.create1D(n+1)
for i in range(n+1):
    a[i] = math.sin(2.0 * math.pi * i * hz / SPS)
stdaudio.playSamples(a)
stdaudio.wait()