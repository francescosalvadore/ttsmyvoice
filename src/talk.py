#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
import sys

voice_name = "francesco"
cwd = os.getcwd()
cwd = os.path.abspath(os.path.join(cwd, os.pardir))

def play_word_mp3(word_file):
    subprocess.Popen(['mpg123', '-q', word_file]).wait()
#import vlc
#p = vlc.MediaPlayer("file:///mnt/hgfs/TEXTTOSPEECH/100splitAudio/guerra.mp3")
#p.play()

def play_text_mp3(text):
    words = text.split(" ")
    for word in words:
        if len(word) == 1:
            subfolder = word[0]+word[0]
        else:
            if word[1] == "'":
                subfolder = word[0]+"a"
            else:
                subfolder = word[0]+word[1]
        folders = [cwd, "voices", voice_name, "out", subfolder]
        out_voice_folder = os.path.join(*folders)
        filepath = os.path.join(out_voice_folder, word+".mp3")

        folders = [cwd, "voices", voice_name, "out", "ca"]
        out_voice_folder = os.path.join(*folders)
        fallbackpath = os.path.join(out_voice_folder, "casa.mp3")
        print filepath
        if os.path.exists(filepath):
            play_word_mp3(filepath)
        else:
            play_word_mp3(fallbackpath)

text = "uomo giorno volta casa parte"
play_text_mp3(text)
