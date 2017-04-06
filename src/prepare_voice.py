#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydub import AudioSegment
from pydub.silence import split_on_silence
import os, glob
import sys

alphabet = map(chr, range(97, 123))

voice_name = "francesco"
mp3_list = [] 

cwd = os.getcwd()
cwd = os.path.abspath(os.path.join(cwd, os.pardir))

# prepare out folders (aa, ab, ac, ad, ..., ba, bb, bc, ...)
for letter in alphabet:
    for inner_letter in alphabet:
        folders = [cwd, "voices", voice_name, "out", letter+inner_letter]
        out_voice_folder = os.path.join(*folders)
        if not os.path.exists(out_voice_folder):
            os.makedirs(out_voice_folder)
        
folders = [cwd, "voices", voice_name, "in"]
in_voice_folder = os.path.join(*folders)
os.chdir(in_voice_folder)
for mp3_file in glob.glob("*.mp3"):
    if len(mp3_list) == 0 or mp3_file in mp3_list:
        print mp3_file
        tmp = mp3_file.split(".")[0]
        dat_file = tmp.split("_")[0]+".dat"
        i_start_word = int(tmp.split("_")[1])
        i_end_word = int(tmp.split("_")[2])
        n_words = i_end_word - i_start_word + 1
        print mp3_file, dat_file, i_start_word, i_end_word, n_words

        word_list = []
        with open(dat_file, "r") as f:
            for i in xrange(i_start_word-1):
                f.readline()
            for i in xrange(n_words):
                # after "#" there are comments
                word_list.append(f.readline().split("#")[0].strip())

        # print word_list
        
        sound_file = AudioSegment.from_mp3(mp3_file)
        print "duration: ",sound_file.duration_seconds
        audio_chunks = split_on_silence(sound_file, 
            # must be silent for at least half a second
            min_silence_len=300,
            # consider it silent if quieter than -50 dBFS
            silence_thresh=-50
        )

        audio_len =  len(audio_chunks)
        if audio_len == n_words:
            print "number of words in mp3 verified ",n_words," equal to: ",audio_len
        else:
            print "incorrect number of words in mp3  ",n_words," not equal: ",audio_len
            print "exiting"
            sys.exit(1)

        for i, chunk in enumerate(audio_chunks):
            word = word_list[i]
            if len(word) == 1:
                subfolder = word[0]+word[0]
            else:
                if word[1] == "'":
                    subfolder = word[0]+"a"
                else:
                    subfolder = word[0]+word[1]
            folders = [cwd, "voices", voice_name, "out", subfolder]
            out_voice_folder = os.path.join(*folders)
            out_folder = list
            out_file = os.path.join(out_voice_folder, word+".mp3")
            print "exporting", out_file
            chunk.export(out_file, format="mp3")
