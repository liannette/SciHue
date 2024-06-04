"""Conversion functions between RGB and other color systems."""

import colorsys
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
    
# Hex color codes: "#" followed by six letters and/or numbers
# first two refer to red
# next two refer to green
# last two refer to blue 
# The color values are between 00 and FF (hexadecimal/16-based)

def hex_to_rgb(hex_color):
    """Convert hex color code to RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """Convert RGB to hex color code."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

# HLS: Hue, Luminance, Saturation
# H: position in the spectrum
# L: color lightness
# S: color saturation

def rgb_to_hls(rgb):
    """Convert RGB to HLS (Hue, Lightness, Saturation)."""
    return colorsys.rgb_to_hls(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)

def hls_to_rgb(hls):
    """Convert HLS back to RGB."""
    return tuple(int(i * 255) for i in colorsys.hls_to_rgb(hls[0], hls[1], hls[2]))

def hex_to_hls(hex):
    """Convert hex color code to HLS (Hue, Lightness, Saturation)."""
    return rgb_to_hls(hex_to_rgb(hex))

def hls_to_hex(hls):
    """Convert HLS to hex color code."""
    return rgb_to_hex(hls_to_rgb(hls))