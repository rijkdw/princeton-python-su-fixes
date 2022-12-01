import modified_stdaudio as stdaudio
import math


print("Playing a sliding noise")
for i in range(44100*2):
    stdaudio.playSample(math.sin(2*math.pi*i*(220+i/44100*440) / 44100))
stdaudio.wait()

print("1 second of silence")
stdaudio.playSamples([0]*44100)

print("Generating a 1-2-3 scale's frequencies")
SPS = 44100                   # samples per second
hz = 440.0                    # concert A
duration = 1.0                # one second
n = int(SPS * duration)
array = []
for j in range(3):
    a = [0 for _ in range(n+1)]
    f = hz * 2**(j/6)
    for i in range(n+1):
        a[i] = math.sin(2.0 * math.pi * i * f / SPS)
    array += a

print("Playing the 1-2-3 scale")
stdaudio.playSamples(array)
stdaudio.wait()

print("Saving it to file 123.wav")
stdaudio.save("123", array)

print("Playing back 123.wav")
stdaudio.playFile("123")

print("Playing babyelephant.wav")
stdaudio.playFile("babyelephant")