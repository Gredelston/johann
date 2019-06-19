import chord

class Phrase(object):
    """A discrete chunk of a song, ending in a cadence."""
    def __init__(self, length):
        self.chords = []
        for _ in range(length):
            self.chords.append(chord.Chord())