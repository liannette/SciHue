import streamlit as st
from streamlit_js_eval import streamlit_js_eval

def initialize_session_state():
    if "saved_color_palettes" not in st.session_state:
        st.session_state.saved_color_palettes = list()

def select_color_scheme(all_color_schemes):
    cols = st.columns(2)
    choice = cols[0].radio(" ", options=all_color_schemes.keys())
    color_scheme = all_color_schemes[choice]
    cols[1].caption("  \n* ".join(color_scheme.description))
    return color_scheme

def select_hue_difference(min_diff, max_diff, default_diff):
    if len({min_diff, max_diff, default_diff}) == 1:
        hue_diff = default_diff
    else:
        cols = st.columns(2)
        hue_diff = cols[0].slider("Distances from main color: ", min_diff, max_diff, default_diff)
    return hue_diff

def select_main_color_and_number_of_colors(main_color, min_n, max_n, default_n):
    cols = st.columns(2)
    main_hex_color = cols[0].color_picker("Pick the main color", main_color)
    n_colors = cols[1].slider("Number of colors in palette: ", min_n, max_n, default_n)
    return main_hex_color, n_colors

def get_window_width():
    return streamlit_js_eval(js_expressions='window.innerWidth', key='WIDTH', want_output=True)

def calculate_column_width(window_width, n_colors):
    return window_width * 1.03 / n_colors

def show_color_palette(color_palette, n_cols, col_width):
    """ Generates a color palette"""
    cols = st.columns(n_cols)
    for i in range(len(color_palette)):
        cols[i].markdown(f'<div style="background-color: {color_palette[i]}; width: {col_width}px; height: 50px;"></div>', unsafe_allow_html=True)
    for i in range(len(color_palette)):
        cols[i].write(str(color_palette[i]))
        
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
    