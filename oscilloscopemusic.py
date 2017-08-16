from struct import pack
from math import sin, cos
import wave

RATE=44100

wv = wave.open('test_stereo.wav', 'w')
wv.setparams((2, 2, RATE, 0, 'NONE', 'not compressed'))
maxVol=2**15-1.0 #maximum amplitude
wvData=""

# circle
for i in range(0, 80000):
    wvData+=pack('h', maxVol*sin(i))
    wvData+=pack('h', maxVol*cos(i))

# square
for i in range(0, 200):
    for i in range(0, 1000):
	wvData+=pack('h', maxVol*sin(i))
        wvData+=pack('h', maxVol*-0.999)
    for i in range(0, 1000):
        wvData+=pack('h', maxVol*-0.999)
	wvData+=pack('h', maxVol*sin(i))
    for i in range(0, 1000):
	wvData+=pack('h', maxVol*sin(i))
        wvData+=pack('h', maxVol)
    for i in range(0, 1000):
        wvData+=pack('h', maxVol)
	wvData+=pack('h', maxVol*sin(i))

wv.writeframes(wvData)
wv.close()

