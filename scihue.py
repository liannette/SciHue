import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from frontend.graphics import color_palettes_for_graphics

# include predefinded color palettes from https://docs.bokeh.org/en/latest/docs/reference/palettes.html

def color_palettes_for_plots():
    data_type = st.radio("Data type", options=["sequential", "diverging", "qualitative", "cyclic"])
    with st.popover("Data type description"):
        st.markdown(
            """
        Qualitative data – Data values represent distinct groups or categories with no inherent order.
        Sequential data – Data values are ordered from low to high, representing a progression.  
        Diverging data – Data values are ordered and diverge around a meaningful midpoint point (e.g. positive and negative deviations from zero or a mean).
        """
        )
    n_colors = st.slider("Number of colors", 3, 23, 6)
    colorblind = st.toggle("Colorblind friendly")

def get_window_width():
    return streamlit_js_eval(js_expressions='window.innerWidth', key='WIDTH', want_output=True)

def main():
    st.title("Sci-Hue")
    tab_plots, tab_graphics = st.tabs(["For Plots", "For Graphics"])
    window_width = get_window_width()
    with tab_plots:
        color_palettes_for_plots()
    with tab_graphics:
        max_colors_in_palette = 8
        default_n_colors = 7
        min_n_colors = 3
        default_main_color = "#6D0707"
        color_palettes_for_graphics(
            max_colors_in_palette, 
            default_n_colors,
            min_n_colors, 
            default_main_color,
            window_width
        )

if __name__ == "__main__":
    main()