import math
import numpy as np
import modified_stdaudio as stdaudio


_SPS = 44100
_DURATION = 2
_BASS_FREQUENCY = 440


def generate_samples(freq, dur):
    return [math.sin(freq*i*2*math.pi/_SPS) for i in range(_SPS*dur)]


bass = generate_samples(freq=_BASS_FREQUENCY, dur=_DURATION)
treble = generate_samples(freq=_BASS_FREQUENCY*1.5, dur=_DURATION)

samples = [b/2+t/8 for b, t in zip(bass, treble)]
stdaudio.playSamples(samples)