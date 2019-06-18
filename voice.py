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
    VocalType('Soprano', tone.name_to_tone('C4'), tone.name_to_tone('G5')),
    VocalType('Alto', tone.name_to_tone('G3'), tone.name_to_tone('D5')),
    VocalType('Tenor', tone.name_to_tone('C3'), tone.name_to_tone('G4')),
    VocalType('Bass', tone.name_to_tone('E2'), tone.name_to_tone('C4')))


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