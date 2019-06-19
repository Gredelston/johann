import random

import params
import song_section
import voice

class Song(object):
    """A complete piece of choral music."""
    def __init__(self):
        """Initial setup for the song. Establish heavy constraints."""
        self.tempo = params.random_from_bounds(params.TEMPO_BOUNDS, 4)

        num_sections = params.random_from_bounds(params.NUM_SECTIONS_BOUNDS)
        section_length = random.choice(params.SECTION_LENGTHS)
        self.sections = []
        for _ in range(num_sections):
            self.sections.append(song_section.SongSection(section_length))

        self.voices = voice.create_four_voices()