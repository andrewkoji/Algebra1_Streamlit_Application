import streamlit as st
import requests

# Note: If you encounter issues with OpenAI API, ensure you are using the latest version.
# Refer to the migration guide: https://github.com/openai/openai-python/discussions/742

st.set_page_config(
    page_title="Linear Equations",
    page_icon="➕",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("<h1 style='text-align: center;'>Linear Equations</h1>", unsafe_allow_html=True)
st.sidebar.success("Select a page above.")
# Define page options


        
st.markdown("<h3 style='text-align: center; color: White;'>Available Pages</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: White;'>🏠 Home</h4>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    
    st.markdown("<ul style='color: White;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: White;'>Slope-Intercept Form</h4>", unsafe_allow_html=True)
    st.markdown("<ul>", unsafe_allow_html=True)
    st.markdown("<li>Slope-Intercept Form: y = mx + b</li>", unsafe_allow_html=True)
    st.markdown("<li>Slope: m</li>", unsafe_allow_html=True)
    st.markdown("<li>y-intercept</li>", unsafe_allow_html=True)
    st.markdown("<li>Standard form to slope-intercept form</li>", unsafe_allow_html=True)
    st.markdown("<li>Point-Slope Form</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

with col2:
    st.markdown("<h4 style='text-align: left; color: White;'>SLOPE</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color: White;'>This is a chatbot for math help</p>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: White;'>Verifying Solutions</h4>", unsafe_allow_html=True)
    st.markdown("<ul style='color: White;'>", unsafe_allow_html=True)
    st.markdown("<li>Checking solutions for Equations in standard form</li>", unsafe_allow_html=True)
    st.markdown("<li>Slope between two points</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
