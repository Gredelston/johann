import random

import params
import song_section

class Song(object):
    def __init__(self):
        self.tempo = params.random_from_bounds(params.TEMPO_BOUNDS, 4)
        num_sections = params.random_from_bounds(params.NUM_SECTIONS_BOUNDS)
        section_length = random.choice(params.SECTION_LENGTHS)
        self.sections = []
        for i in range(num_sections):
            self.sections.append(song_section.SongSection(section_length))
