#!/usr/bin/env python3

"""
Wait for button to be pressed and
trigger the audio sample after a short delay.
"""

import gpiozero
import time
from pydub import AudioSegment, playback
from multiprocessing import Process
import os

button = gpiozero.Button(3)
audio = AudioSegment.from_wav('/home/pi/sich_niederlassen/audio.wav')

def play_audio():
    playback.play(audio)

# Set volume to 97% which is as high as it will go without distorting
os.system('amixer -c 0 cset numid=1 97%')
# Force audio output to be on line-out
os.system('amixer -c 0 cset numid=3 1')

print('Setup complete, waiting for input.')

if __name__ == '__main__':
    while True:
        button.wait_for_press()
        print('Button was pressed.')

        for i in reversed(range(1,11)):
            print(i)
            time.sleep(1)

        audio_process = Process(target=play_audio)
        audio_process.start()
        print('Playback was started...')

        button.wait_for_release()
        print('Button was released.')

        audio_process.terminate()
        print('Playback was stopped.')
