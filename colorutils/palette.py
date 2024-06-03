"""Generation of the colors in a color palette"""

from colorutils.transform import hex_to_hls, hls_to_hex
from itertools import cycle
import random


def generate_palette(main_hex_color, n_colors, n_hues, hue_diff):
    """Generates a color palette"""
    main_hls = hex_to_hls(main_hex_color)
    hues = [hue/360 for hue in _calculate_hues(main_hls[0]*360, n_hues, hue_diff)]
    lightnesses = _random(n_colors-1)
    saturations = _random(n_colors-1)
    additional_hls = [tuple(hls) for hls in zip(cycle(hues), lightnesses, saturations)]
    all_hls = sorted([main_hls, *additional_hls], key = lambda x: x[1])
    return [hls_to_hex(hls) for hls in all_hls]

def _calculate_hues(main_hue, n_hues, hue_diff) -> tuple:
    """Generates a tuple of hues (in degree), based on a main hue"""
    if n_hues == 1:
        hues = (main_hue,)
    elif n_hues == 2:
        hues = (main_hue+hue_diff, main_hue)
    elif n_hues == 3:
        hues = [main_hue+hue_diff, main_hue-hue_diff, main_hue]
    elif n_hues == 4:
        hues = [main_hue+180, main_hue+hue_diff, main_hue+hue_diff+180, main_hue]
    return hues

def _random(n, sorted_bool=False):
    random_values = [random.random() for i in range(n)]
    if sorted_bool:
        random_values.sort()
    return random_values
    
    


