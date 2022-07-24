import os
import sys
import ffmpeg
from subprocess import run, PIPE
from pathlib import Path
from stream import ssteam

from test import test

video_location='vids/Dota.mp4'
try:
   
    stream = ffmpeg.input('./vids/Dota.mp4')
    stream = ffmpeg.filter(stream,'fps',fps=25,round='up')
    stream = ffmpeg.output(stream,'output2.mp4')
    ffmpeg.run(stream)
    test('output2.mp4')
    ssteam('output2.mp4')
except:
    print('Error')