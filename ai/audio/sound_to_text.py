# encoding=utf8
import os
import wave
import pyaudio
from aip import AipSpeech
from time import time

APP_ID = '18021223'
API_KEY = 'dkFrntdS3E9VIPc4ZK8pv9kg'
SECRET_KEY = 'KVsrMNlsihOrMvkppZQGsWRrcsV34Nsr'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 16000  # Record at 16000 samples per second
seconds = 5


def record_audio():
    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    print('Recording...')
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')
    return frames


def save_wav_file(path, data):
    """保存data到.wac文件"""
    wf = wave.open(path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(2)
    wf.setframerate(fs)
    wf.writeframes(b''.join(data))
    wf.close()
    return path


def get_file_info(file_path):
    with open(file_path, 'rb') as f:
        return f.read()


def main():
    frame = record_audio()
    # filename = input('Input record filename:')
    filename = 'test.pcm'
    filename = save_wav_file(filename, frame)

    start = time()
    res = client.asr(get_file_info(filename), 'wav', 16000, dict(dev_pid=1537))
    if res.get('err_msg') == 'success.':
        print('识别结果为: ', res.get('result')[0])
        print('耗时: ', time() - start)
    else:
        raise Exception(res.get('err_no'), res.get('err_msg'))
    # os.remove(filename)


if __name__ == '__main__':
    main()
