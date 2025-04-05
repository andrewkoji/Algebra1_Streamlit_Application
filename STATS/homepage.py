import streamlit as st
import requests

st.set_page_config(
    page_title="Statistics and Probability",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Statistics and Probability")
st.sidebar.success("Select a page above.")
# Define page options

st.markdown("<h3 style='text-align: center; color: White;'>Available Pages</h3>", unsafe_allow_html=True)
st.markdown(
    """
    <a href="https://www.nysedregents.org/algebraone/125/algone-12025-exam.pdf" target="_blank" style="font-size:20px; font-weight:bold; color:Red; text-decoration:none;">
        📄 June 2024 A1R Exam
    </a>
    """,
    unsafe_allow_html=True
)
# st.markdown(
#     """
#     <a href="https://www.nysedregents.org/algebraone/125/algone-12025-exam.pdf" target="_blank" style="font-size:20px; font-weight:bold; color:Red; text-decoration:none;">
#         📄 June 2024 A1R Exam
#     </a>
#     """,
#     unsafe_allow_html=True
# )
col1, col2 = st.columns(2)
# pdf_file = "pages/algone_12025_exam.pdf"  # Replace with the path to your PDF file
# pdf_display = f'<iframe src="{pdf_file}" width="100%" height="800px" type="application/pdf"></iframe>'
# st.markdown(pdf_display, unsafe_allow_html=True)
with col1:
    st.markdown("- 🏠 **Home**")
    st.markdown("- 📊 **1 Variable Statistics**")
    st.markdown("Box-Plots")
    st.markdown("Dot-Plots")
    st.markdown("Histograms")
    st.markdown("Quartiles(Q1, Q2, Q3)")
    st.markdown("Standard Deviation(Sx)")
with col2:
    st.markdown("- 🤖 **Chatbot**")
    st.markdown("This is a chatbot for math help")
    st.markdown("- 📈 **Linear Regression**")
    st.markdown("LinReg(ax + b)")
    st.markdown("Correlation Coefficient(r)")
