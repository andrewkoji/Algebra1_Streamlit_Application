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
st.markdown("<h3 style='text-align: center; color: White;'>Old Regents Exams</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

def generate_exam_link(year, month, month_name):
    return st.markdown(
        f"""
        <a href="https://www.nysedregents.org/algebraone/{month}{year}/algone{month}20{year}-exam.pdf" target="_blank" style="font-size:20px; font-weight:bold; color:Red; text-decoration:none;">
            📄 {month_name} 20{year} A1R Exam
        </a>
        """,
        unsafe_allow_html=True
    )

with col1:

    with col1:
        # Define a list of years and months for the exams
        exams = [
            {"year": "24", "month": "6", "month_name": "June"},
            {"year": "23", "month": "6", "month_name": "June"},
            {"year": "22", "month": "6", "month_name": "June"},
            {"year": "20", "month": "6", "month_name": "June"},
            {"year": "19", "month": "6", "month_name": "June"},
        ]

    # Loop through the exams and generate links
    for exam in exams:
        generate_exam_link(exam["year"], exam["month"], exam["month_name"])
with col2:
    with col1:
        # Define a list of years and months for the exams
        exams = [
            {"year": "24", "month": "1", "month_name": "January"},
            {"year": "23", "month": "1", "month_name": "January"},
            {"year": "22", "month": "1", "month_name": "January"},
            {"year": "20", "month": "1", "month_name": "January"},
            {"year": "19", "month": "1", "month_name": "January"},
        ]

    # Loop through the exams and generate links
    for exam in exams:
        generate_exam_link(exam["year"], exam["month"], exam["month_name"])
with col3:
    # Define a list of years and months for the exams
    exams = [
        {"year": "24", "month": "8", "month_name": "August"},
        {"year": "23", "month": "8", "month_name": "August"},
        {"year": "22", "month": "8", "month_name": "August"},
        {"year": "20", "month": "8", "month_name": "August"},
        {"year": "19", "month": "8", "month_name": "August"},
    ]

    # Loop through the exams and generate links
    for exam in exams:
        generate_exam_link(exam["year"], exam["month"], exam["month_name"])

        
st.markdown("<h3 style='text-align: center; color: White;'>Available Pages</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h4 style='text-align: left; color: White;'>🏠 Home</h4>", unsafe_allow_html=True)
    st.markdown("<ul style='color: White;'>", unsafe_allow_html=True)
    st.markdown("<li>📊 <b>1 Variable Statistics</b></li>", unsafe_allow_html=True)
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
    st.markdown("<li>LinReg (ax + b)</li>", unsafe_allow_html=True)
    st.markdown("<li>Correlation Coefficient (r)</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
