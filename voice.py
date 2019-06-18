import tone

class VocalType(object):
    """Abstract representation of a vocal range, such as Soprano or Alto."""
    def __init__(self, name, low_note, high_note):
        self.name = name
        self.low_note = low_note
        self.high_note = high_note
    
    def get_name(self):
        return name
    
    def get_abbr(self):
        return name[0]
    
    def get_range(self):
        return (self.low_note, self.high_note)


VOCAL_TYPES = (
    VocalType('Soprano', tone.Tone('C4'), tone.Tone('G5')),
    VocalType('Alto', tone.Tone('G3'), tone.Tone('D5')),
    VocalType('Tenor', tone.Tone('C3'), tone.Tone('G4')),
    VocalType('Bass', tone.Tone('E2'), tone.Tone('C4')))


class Voice(object):
    """A voice part in a specific piece of music."""
    def __init__(self, vocal_type):
        self.vocal_type = vocal_type
    
    def get_name(self):
        return self.vocal_type.get_name()
    
    def get_abbr(self):
        return self.vocal_type.get_abbr()
    
    def get_range(self):
        return self.vocal_type.get_range()