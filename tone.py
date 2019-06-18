MIDI_NUMBERS = {
    'C2': 36,
    'B#2': 36,

    'C#2': 37,
    'Db2': 37,

    'D2': 38,

    'D#2': 39,
    'Eb2': 39,

    'E2': 40,
    'Fb2': 40,

    'F2': 41,
    'E#2': 41,
    
    'F#2': 42,
    'Gb2': 42,

    'G2': 43,

    'G#2': 44,
    'Ab2': 44,
    
    'A2': 45,

    'A#2': 46,
    'Bb2': 46,
    
    'B2': 47,
    'Cb2': 47,
}
SEMITONE_RATIO = 2**(1/12.)
A4_FREQUENCY = 440
A4_MIDI_NUMBER = 69

class Tone(object):
    """Abstract representation of a pitch."""
    def __init__(self, name):
        self.name = name
        self.midi_number = get_midi_number(name)
        self.freq = midi_number_to_freq(self.midi_number)
    
    def __eq__(self, other):
        return self.midi_number == other.midi_number
    
    def __lt__(self, other):
        return self.midi_number < other.midi_number
    
    def __gt__(self, other):
        return self.midi_number > other.midi_number
    

def get_midi_number(name):
    pitch = name[:-1]
    octave = int(name[-1])
    if octave == 2:
        return MIDI_NUMBERS[name]
    elif octave < 2:
        one_octave_higher_name = pitch + str(octave + 1)
        return get_midi_number(one_octave_higher_name) - 12
    elif octave > 2:
        one_octave_lower_name = pitch + str(octave - 1)
        return get_midi_number(one_octave_lower_name) + 12


def midi_number_to_freq(midi_number):
    semitones_above_a4 = midi_number - A4_MIDI_NUMBER
    return A4_FREQUENCY * (SEMITONE_RATIO ** semitones_above_a4)