"""main of wave reader project
"""

import struct
from pyaudio import PyAudio

MUSIC_SPEED = 1.1
STOPING = (False, 100)

wav = open("music.wav", "rb")

wav.seek(22)
num_channels = struct.unpack('<h', wav.read(2))[0]
sample_rate = int(struct.unpack('<l', wav.read(4))[0] * MUSIC_SPEED)

wav.seek(34)
bits_per_sample = struct.unpack('<h', wav.read(2))[0]


p = PyAudio()

stream = p.open(format=p.get_format_from_width(bits_per_sample/8),
                channels=num_channels,
                rate=sample_rate,
                output=True)

data = wav.read(sample_rate)
bit = 0
while data:
    stream.write(data)
    if STOPING[0] and bit == STOPING[1]:
        wav.seek(34)
        bit = 0
    data = wav.read(sample_rate)
    bit += 1

stream.stop_stream()
stream.close()
p.terminate()
wav.close()
