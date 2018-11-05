import os
from nltk.corpus import cmudict
import soundfile as sf
import sounddevice as sd

def word_to_phoneme(word):
  return cmudict.dict().get(word, "No word found")


def phoneme_to_sound(phoneme_array):
  first = phoneme_array[0]
  for phoneme in first:
    string = ''.join([x for x in phoneme if x.isalpha()])
    data, fs = sf.read(os.environ.get(FILE_URL)+ string + '.aif')
    sd.play(data, fs, blocking=True)