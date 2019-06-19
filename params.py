import random

# Bounds
TEMPO_BOUNDS = (60, 128) # Beats per minute
NUM_SECTIONS_BOUNDS = (3, 8)

# Lists
SECTION_LENGTHS = [6, 8, 10, 12, 16, 24, 32] # Beats

def random_from_bounds(bounds, step=1):
    low, high = bounds
    return random.randrange(low, high + 1, step)
