"""main of wave reader project
"""

from pyaudio import PyAudio
import struct

music_speed = 1.1
stoping = (False, 100)

wav = open("music.wav", "rb")

wav.seek(22)
num_channels = struct.unpack('<h', wav.read(2))[0]
sample_rate = int(struct.unpack('<l', wav.read(4))[0] * music_speed)

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
    if stoping[0] and bit == stoping[1]:
        wav.seek(34)
        bit = 0
    data = wav.read(sample_rate)
    bit += 1
