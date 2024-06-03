"""Color Schemes"""

class ColorScheme():
    def __init__(self, name, description, n_hues, hue_diff_settings) -> None:
        self.name = name
        self.description = description
        self.n_hues = n_hues
        self.hue_diff_settings = hue_diff_settings


def import_color_schemes():
    color_schemes = dict()

    color_schemes["monochromatic"] = ColorScheme(
        name = "monochromatic",
        description = [
            "Uses different shades, tints, and tones of a single color",
            "Creates a clean and consistent look", 
            "Ideal for visualizations where the focus is on data trends rather than color differentiation",
            "Useful in heatmaps and intensity maps in scientific visuals",
        ],
        n_hues = 1,
        hue_diff_settings = (0, 0, 0)
    )

    color_schemes["analogous"] = ColorScheme(
        name = "analogous",
        description = [
            "Uses colors that are next to each other on the color wheel",
            "Provides a harmonious and soothing effect",
            "Good for showing data that is related or has a progression",
            "Useful for diagrams where categories are related but distinct, such as ecological or biological classifications",
        ],
        n_hues = 3,
        hue_diff_settings = (10, 40, 30),
    )

    color_schemes["complementary"] = ColorScheme(
        name = "complementary",
        description = [
            "Uses colors that are opposite each other on the color wheel",
            "Creates a vibrant and high-contrast look",
            "Useful for highlighting differences or making certain data points stand out",
            "Effective in comparative charts and graphs where contrasting elements are essential",
        ],
        n_hues = 2,
        hue_diff_settings = (180, 180, 180)
    )
    
    color_schemes["split_complementary"] = ColorScheme(
        name = "split_complementary",
        description = [
            "Uses a base color and two adjacent colors to its complement",
            "Maintains contrast while offering more color variety than complementary schemes",
            "Ideal for complex charts where multiple distinctions are necessary but still need a cohesive look",
            "Useful in presenting multi-faceted data sets, like social science data",
        ],
        n_hues = 3,
        hue_diff_settings = (150, 175, 170),
    )
    
    # Add triadic, tetradic - maybe also cool colors, warm colors, neutral colors?
    
    return color_schemes


