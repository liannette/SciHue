import streamlit as st
from colorutils.schemes import import_color_schemes
from colorutils.palette import generate_palette
from frontend import ui

# include predefinded color palettes from https://docs.bokeh.org/en/latest/docs/reference/palettes.html

# Constants
MAX_COLORS_IN_PALETTE = 7
DEFAULT_N_COLORS = 7
MIN_N_COLORS = 3
DEFAULT_MAIN_COLOR = "#008dff"

def main():
    ui.initialize_session_state()
    st.header("SciHue")
    all_color_schemes = import_color_schemes()
    scheme = ui.select_color_scheme(all_color_schemes)
    hue_diff = ui.select_hue_difference(*scheme.hue_diff_settings)
    st.divider()
    main_hex_color, n_colors = ui.select_main_color_and_number_of_colors(
        DEFAULT_MAIN_COLOR, 
        MIN_N_COLORS, 
        MAX_COLORS_IN_PALETTE, 
        DEFAULT_N_COLORS
        )
    st.divider()
    color_palette = generate_palette(main_hex_color, n_colors, scheme.n_hues, hue_diff)
    window_width = ui.get_window_width()
    if window_width is not None:
        n_cols = MAX_COLORS_IN_PALETTE
        col_width = ui.calculate_column_width(window_width, n_cols)
        ui.show_color_palette(color_palette, n_cols, col_width)
        ui.show_rerun_buttons()
        ui.current_color_palette(color_palette)
        ui.show_saved_color_palettes(col_width, n_cols)

if __name__ == "__main__":
    main()