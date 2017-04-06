# ttsmyvoice

Minimalist Python TTS using custom vocabulary.

## Quick-start (Linux only but with small changes should work on Win and Mac)
```bash
git clone https://github.com/francescosalvadore/ttsmyvoice.git
cd ttsmyvoice/src
python prepare_voice.py
python talk.py
```

To change the read text modify talk.py

To use your own word:
```bash
cd ../voices
mkdir -p <your_name>/in
```
and edit *prepare_voice.py* and *talk.py* to use your vocabulary (*voice_name* variable).

Put a list of words in a .dat file (only letters and numbers in the name of file please) 
with a word per line, an example is in francesco/in folder, *comuni1174.dat*.

Then record (e.g. using Audacity and a decent microphone) an interval of words to a .mp3 file, e.g.
*comuni1174_1_10.mp3*

Then run again *prepare_voice.py*

Suggestion: let at least half a second among the words, and, in case you encounter problems, 
tune the *prepare_voice.py* silence time *min_silence_len* and silence threshold *silence_thresh*.

For a very good list of italian words look at:
https://github.com/napolux/paroleitaliane
