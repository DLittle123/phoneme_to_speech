from server import server
from server.controllers.words import word_to_phoneme, phoneme_to_sound

@server.route('/')
@server.route('/index')
def index():
    return "Hello, World!"

@server.route('/word/<string:composed_word>', methods=['GET'])

def word(composed_word):
  value = word_to_phoneme(composed_word)
  if type(value) == str:
    return 'Couldn\'t find word'
  else:
    phoneme_to_sound(value)
    return 'Success'