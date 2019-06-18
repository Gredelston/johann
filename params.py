import random

# Bounds
TEMPO_BOUNDS = (60, 128)
NUM_SECTIONS_BOUNDS = (3, 8)

# Lists
SECTION_LENGTHS = [1.5, 2, 2.5, 3, 4, 6, 8]

def random_from_bounds(bounds, step=1):
    low, high = bounds
    return random.randrange(low, high + 1, step)
