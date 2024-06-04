import streamlit as st
from color.schemes import import_color_schemes
from color.calculations import generate_palette

def color_palettes_for_graphics(
        max_colors_in_palette, 
        default_n_colors,
        min_n_colors, 
        default_main_color,
        window_width
    ):
    initialize_session_state()
    all_color_schemes = import_color_schemes()
    scheme = select_color_scheme(all_color_schemes)
    hue_diff = select_hue_difference(*scheme.hue_diff_settings)
    st.divider()
    main_hex_color, n_colors = select_main_color_and_number_of_colors(
        default_main_color, 
        min_n_colors, 
        max_colors_in_palette, 
        default_n_colors
        )
    st.divider()
    color_palette = generate_palette(main_hex_color, n_colors, scheme.n_hues, hue_diff)
    if window_width is not None:
        n_cols = max_colors_in_palette + 1
        col_width = calculate_column_width(window_width, n_cols)
        show_color_palette(color_palette, n_cols, col_width)
        show_rerun_buttons()
        current_color_palette(color_palette)
        show_saved_color_palettes(col_width, n_cols)

def initialize_session_state():
    if "saved_color_palettes" not in st.session_state:
        st.session_state.saved_color_palettes = list()

def select_color_scheme(all_color_schemes):
    cols = st.columns(3)
    choice = cols[0].radio("Color combination", options=all_color_schemes.keys())
    color_scheme = all_color_schemes[choice]
    cols[1].image(f"images/colorschemes/{color_scheme.name}.png")
    cols[2].caption("  \n* ".join([" ", *color_scheme.description]))
    return color_scheme

def select_hue_difference(min_diff, max_diff, default_diff):
    if len({min_diff, max_diff, default_diff}) == 1:
        hue_diff = default_diff
    else:
        cols = st.columns(2)
        hue_diff = cols[0].slider("Distance on colorwheel (in °): ", min_diff, max_diff, default_diff)
    return hue_diff

def select_main_color_and_number_of_colors(main_color, min_n, max_n, default_n):
    cols = st.columns(2)
    main_hex_color = cols[0].color_picker("Pick the main color", main_color)
    n_colors = cols[1].slider("Number of colors in palette: ", min_n, max_n, default_n)
    return main_hex_color, n_colors

def calculate_column_width(window_width, n_colors):
    return window_width * 1.03 / n_colors

def show_color_palette(color_palette, n_cols, col_width):
    """ Generates a color palette"""
    cols = st.columns(n_cols)
    for i in range(len(color_palette)):
        hex_color = color_palette[i]
        color_box = f"""
        <div style="background-color:{hex_color}; width:{col_width}px; height:40px; padding-top:7px; ;padding-bottom:7x; margin-bottom:20px">
            <p style="color:{hex_color};text-align:center;">{hex_color}</p>
        </div>
        """
        cols[i].markdown(color_box, unsafe_allow_html=True)
    with cols[-1].popover("📋"):
        st.code(repr(color_palette))
        
def show_rerun_buttons():
    cols = st.columns(2)
    rerun = cols[0].button("rerun")
    save_and_rerun = cols[1].button("Save & Rerun")
    if save_and_rerun:
        st.session_state.saved_color_palettes.append(st.session_state.current_color_palette)
    
def current_color_palette(color_palette):
    st.session_state.current_color_palette = color_palette

def show_saved_color_palettes(col_width, n_colors):
    for saved_color_palette in reversed(st.session_state.saved_color_palettes):
        show_color_palette(saved_color_palette, n_colors, col_width)
    