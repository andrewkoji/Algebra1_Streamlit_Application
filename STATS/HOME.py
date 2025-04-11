import streamlit as st
import requests

st.set_page_config(
    page_title="Statistics and Probability",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("<h1 style='text-align: center;'>Statistics and Probability</h1>", unsafe_allow_html=True)
st.sidebar.success("Select a page above.")
# Define page options


        
st.markdown("<h3 style='text-align: center; color: White;'>Available Pages</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: White;'>🏠 Home</h4>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    
    st.markdown("<ul style='color: White;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: White;'>📊 1 Variable Statistics</h4>", unsafe_allow_html=True)
    st.markdown("<ul>", unsafe_allow_html=True)
    st.markdown("<li>Box-Plots</li>", unsafe_allow_html=True)
    st.markdown("<li>Dot-Plots</li>", unsafe_allow_html=True)
    st.markdown("<li>Histograms</li>", unsafe_allow_html=True)
    st.markdown("<li>Quartiles (Q1, Q2, Q3)</li>", unsafe_allow_html=True)
    st.markdown("<li>Standard Deviation (Sx)</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

with col2:
    st.markdown("<h4 style='text-align: left; color: White;'>🤖 Chatbot</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color: White;'>This is a chatbot for math help</p>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: White;'>📈 Linear Regression</h4>", unsafe_allow_html=True)
    st.markdown("<ul style='color: White;'>", unsafe_allow_html=True)
    st.markdown("<li>LinReg (ax + b) - Linear Regression Equation</li>", unsafe_allow_html=True)
    st.markdown("<li>Correlation Coefficient (r)</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
