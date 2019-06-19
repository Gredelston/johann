import random

import params
import phrase
import voice

class Song(object):
    """A complete piece of choral music."""
    def __init__(self):
        """Initial setup for the song. Establish heavy constraints."""
        self.tempo = params.random_from_bounds(params.TEMPO_BOUNDS, 4)

        num_phrases = params.random_from_bounds(params.NUM_PHRASES_BOUNDS)
        beats_per_phrase = random.choice(params.PHRASE_LENGTHS)
        self.phrases = []
        for _ in range(num_phrases):
            self.phrases.append(phrase.Phrase(beats_per_phrase))

        self.voices = voice.create_four_voices(self)
    
    def get_num_phrases(self):
        return len(self.phrases)
    
    def get_phrase(self, num):
        return self.phrases[num]