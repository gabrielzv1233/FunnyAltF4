# Converts audio file to base64 to be pasted in FunnyAltF4.py
import base64
import sys
import os

compile_file = '/Sound Effect.mp3'

with open(compile_file, 'rb') as file:
    mp3_data = file.read()

mp3_base64 = base64.b64encode(mp3_data).decode('utf-8')

with open(os.path.dirname(os.path.abspath(sys.argv[0]))+'\output.txt', 'w') as file:
    file.write(mp3_base64)
