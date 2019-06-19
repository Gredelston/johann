import tone
import vocal_phrase

class Voice(object):
    """A voice part in a song."""
    def __init__(self, name, low_tone_name, high_tone_name, song):
        self.name = name
        self.low_tone = tone.name_to_tone(low_tone_name)
        self.high_tone = tone.name_to_tone(high_tone_name)
        self.song = song

        # Define vocal phrases
        self.phrases = []
        for phrase_num in range(self.song.get_num_phrases()):
            self.phrases.append(vocal_phrase.VocalPhrase(
                self, self.song.get_phrase(phrase_num)))
    
    def get_name(self):
        return self.name
    
    def get_abbr(self):
        return self.name[0]
    
    def get_range(self):
        return (self.low_tone, self.high_tone)


def create_four_voices(song):
    return (
        Voice('Soprano', 'C4', 'G5', song),
        Voice('Alto', 'G3', 'D5', song),
        Voice('Tenor', 'C3', 'G4', song),
        Voice('Bass', 'E2', 'C4', song)
    )