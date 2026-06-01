import streamlit as st
from interface.streamlit_ui import render_ui


st.set_page_config(
    page_title="AI CV Filtering", page_icon="🤖", layout="wide"
)

render_ui()   