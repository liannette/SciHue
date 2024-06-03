"""Conversion functions between RGB and other color systems."""

import colorsys

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

# differences between HLS and HSV: 
# https://www.tobiamontanari.com/hsl-and-hsv-explained-which-color-model-should-you-use/

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

# HSV: Hue, Saturation, Value
# H: position in the spectrum
# S: color saturation ("purity")
# V: color brightness

def rgb_to_hsv(rgb):
    """Convert RGB to HVS (Hue, Saturation, Value)."""
    return colorsys.rgb_to_hsv(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)

def hsv_to_rgb(hsv):
    """Convert HVS back to RGB."""
    return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2]))

def hex_to_hsv(hex):
    """Convert hex color code to HLS (Hue, Lightness, Saturation)."""
    return rgb_to_hsv(hex_to_rgb(hex))

def hsv_to_hex(hsv):
    """Convert HSV to hex color code."""
    return rgb_to_hex(hsv_to_rgb(hsv))