"""main of wave reader project
"""

# Standard library import
import struct

# Third party import
from pyaudio import PyAudio

# Local imports
from constant import FILE_NAME, MUSIC_SPEED, STOPING


wav = open(FILE_NAME, "rb")

wav.seek(22)
num_channels = struct.unpack('<h', wav.read(2))[0]
sample_rate = int(struct.unpack('<l', wav.read(4))[0] * MUSIC_SPEED)
wav.seek(34)
bits_per_sample = struct.unpack('<h', wav.read(2))[0]

audio = PyAudio()
stream = audio.open(format=audio.get_format_from_width(bits_per_sample/8),
                    channels=num_channels,
                    rate=sample_rate,
                    output=True)

data = wav.read(sample_rate)
COUNT = 0
while data:
    stream.write(data)
    if STOPING[0] and COUNT == STOPING[1]:
        wav.seek(34)
        COUNT = 0
    data = wav.read(sample_rate)
    COUNT += 1

stream.stop_stream()
stream.close()
audio.terminate()
wav.close()
