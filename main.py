"""main of wave reader project
"""

from pyaudio import PyAudio
import struct

music_speed = 1.1

wav = open("music.wav", "rb")

wav.seek(22)
num_channels = struct.unpack('<h', wav.read(2))[0]
sample_rate = int(struct.unpack('<l', wav.read(4))[0] * music_speed)
