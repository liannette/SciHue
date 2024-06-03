"""Generation of the colors in a color palette"""

from colorutils.transform import hex_to_hls, hls_to_hex
from itertools import cycle
import random


def generate_palette(main_hex_color, n_colors, n_hues, hue_diff):
    """Generates a color palette"""
    main_hue = hex_to_hls(main_hex_color)[0] * 360
    hues = [hue/360 for hue in _calculate_hues(main_hue, n_hues, hue_diff)]
    lightnesses = _random(n_colors-1, sorted_bool=True)
    saturations = _random(n_colors-1)
    additional_hex_colors = [
        hls_to_hex(hls) for hls in zip(cycle(hues), lightnesses, saturations)
        ]
    return [main_hex_color, *additional_hex_colors]

def _calculate_hues(main_hue, n_hues, hue_diff) -> tuple:
    """Generates a tuple of hues for the color scheme, based on its main color"""
    hues = [main_hue+hue_diff, main_hue-hue_diff, main_hue]
    return tuple(hues[-n_hues:])

def _random(n, sorted_bool=False):
    random_values = [random.random() for i in range(n)]
    if sorted_bool:
        random_values.sort()
    return random_values
    
    


