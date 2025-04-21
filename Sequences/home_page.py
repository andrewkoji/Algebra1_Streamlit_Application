import streamlit as st
import requests

# Note: If you encounter issues with OpenAI API, ensure you are using the latest version.
# Refer to the migration guide: https://github.com/openai/openai-python/discussions/742

st.set_page_config(
    page_title="Patterns and Sequences",
    page_icon="➕",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("<h1 style='text-align: center;'>Arithmetic and Geometric Sequences</h1>", unsafe_allow_html=True)
st.sidebar.success("Select a page above.")
# Define page options


        
st.markdown("<h3 style='text-align: center; color: White;'>Available Pages</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: White;'>🏠 Home</h4>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h4 style='text-align: left; color: White;'>Patterns</h4>", unsafe_allow_html=True)
    st.markdown("<li>Sequence - list of numbers by pattern</li>", unsafe_allow_html=True)

    st.markdown("<li>Arithmetic</li>", unsafe_allow_html=True)
    st.markdown("<li>➕ or ➖ to next term</li>", unsafe_allow_html=True)
    st.markdown("<li>Geometric</li>", unsafe_allow_html=True)
    st.markdown("<li>✖️ or ➗ to get to next term</li>", unsafe_allow_html=True)
    

with col2:
    st.markdown("<h4 style='text-align: left; color: White;'>Arithmetic Sequences</h4>", unsafe_allow_html=True)
    st.markdown("<li>Formula and terminology</li>", unsafe_allow_html=True)
    st.markdown("<li>Examples for practice</li>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: White;'>Geometric Sequences</h4>", unsafe_allow_html=True)
    st.markdown("<li>Formula and terminology</li>", unsafe_allow_html=True)
    st.markdown("<li>Examples for practice</li>", unsafe_allow_html=True)
    st.markdown("<ul style='color: White;'>", unsafe_allow_html=True)
    
    
    st.markdown("</ul>", unsafe_allow_html=True)
