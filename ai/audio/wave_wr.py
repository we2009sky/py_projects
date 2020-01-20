# encoding=utf8
import os
import wave
from pydub import AudioSegment

CHUNK = 1024
file_path = r'D:\CloudMusic\Music\a teens - upside down.mp3'
new_file = 'output.wav'
sound = AudioSegment.from_mp3(file_path)
sound.export(new_file, format='.wav')

rf = wave.open(file_path, 'rb')
data = rf.readframes(CHUNK)

wf = wave.open(new_file, 'wb')
wf.setnchannels(rf.getnchannels())
wf.setframerate(rf.getframerate())
wf.setsampwidth(rf.getsampwidth())
wf.writeframes(rf.getnframes())

wf.close()
rf.close()