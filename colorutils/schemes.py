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
            "Uses variations in lightness and saturation of a single color (0° hue difference)",
            "Creates a clean and consistent look", 
            "Good for designs, scientific posters, and charts to emphasize data without overwhelming the viewer."
        ],
        n_hues = 1,
        hue_diff_settings = (0, 0, 0)
    )
    color_schemes["analogous"] = ColorScheme(
        name = "analogous",
        description = [
            "Uses colors that are next to each other on the color wheel",
            "Creates a harmonious and soothing effect",
            "Ideal for sections or dashboards where related information is grouped together"
        ],
        n_hues = 3,
        hue_diff_settings = (10, 40, 30),
    )
    color_schemes["complementary"] = ColorScheme(
        name = "complementary",
        description = [
            "Uses colors that are opposite each other on the color wheel (180° hue difference)",
            "Creates a vibrant and high-contrast look",
            "Useful for highlighting differences or making certain aspects stand out",
        ],
        n_hues = 2,
        hue_diff_settings = (180, 180, 180)
    )
    color_schemes["split complementary"] = ColorScheme(
        name = "split complementary",
        description = [
            "Uses a base color and two adjacent colors of its opposite on the color wheel",
            "Maintains contrast while offering more color variety than a complementary scheme",
            "Ideal for complex figures where multiple distinctions are necessary but still need a cohesive look",
        ],
        n_hues = 3,
        hue_diff_settings = (150, 175, 170),
    )
    color_schemes["triadic"] = ColorScheme(
        name = "triadic",
        description = [
            "Uses three colors that are evenly spaced around the color wheel",
            "Creates vibrant and balanced designs",
            "Suitable for complex visualizations where multiple categories need distinction",
            "Tip: select one color as dominant and use the other two in lesser quantities with a lower saturation",
        ],
        n_hues = 3,
        hue_diff_settings = (120, 120, 120),
    )        
    color_schemes["tetradic (double-complementary)"] = ColorScheme(
        name = "tetradic",
        description = [
            "Uses two complementary color pairs",
            "Very powerful and rich visualizations, but can easily get overwhelming",
            "Effective in comparing multiple aspects or visualizing interactions between them",
            "Tips: Do not use all the four colors in equal amounts",
        ],
        n_hues = 4,
        hue_diff_settings = (5, 60, 90),
    )
    # Add maybe also cool colors, warm colors, neutral colors?
    return color_schemes


