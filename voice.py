import tone

class Voice(object):
    """A voice part in a specific piece of music."""
    def __init__(self, name, low_tone, high_tone):
        self.name = name
        self.low_tone = low_tone
        self.high_tone = high_tone
    
    def get_name(self):
        return self.name
    
    def get_abbr(self):
        return self.name[0]
    
    def get_range(self):
        return (self.low_tone, self.high_tone)


def create_four_voices():
    return (
        Voice('Soprano', tone.name_to_tone('C4'), tone.name_to_tone('G5')),
        Voice('Alto', tone.name_to_tone('G3'), tone.name_to_tone('D5')),
        Voice('Tenor', tone.name_to_tone('C3'), tone.name_to_tone('G4')),
        Voice('Bass', tone.name_to_tone('E2'), tone.name_to_tone('C4')))