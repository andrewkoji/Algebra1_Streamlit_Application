import streamlit as st
from streamlit.components.v1 import html  # Add this import
import requests

st.markdown("<h3 style='text-align: center;'>Real-Time LaTeX Preview</h3>", unsafe_allow_html=True)

response = requests.get('https://fastapi-b6dv.onrender.com/latex-textbox')

# Parse the JSON response or use a fallback
if response.status_code == 200:
    html_code = response.json().get('latex_html_code', '')
else:
    st.warning("Failed to fetch LaTeX textbox. Using fallback template.")
    html_code = r"""
    <div style="text-align: center;">
        <div id="latex-output" style="margin-top: 20px; font-size: 20px; color: black; display: inline-block; border: 1px solid #ccc; padding: 10px; min-height: 50px; position: relative; background-color: white; border-radius: 10px;">
            <span id="latex-rendered"></span>
        </div>
    </div>
    <script>
        const latexRendered = document.getElementById("latex-rendered");

        // Example LaTeX content for demonstration
        const latex = "\\frac{a}{b} + c^2";

        // Render the LaTeX content using KaTeX
        latexRendered.innerHTML = katex.renderToString(latex, { throwOnError: false });
    </script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.13.18/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.13.18/dist/katex.min.js"></script>
    """

# Render the HTML and JavaScript
if html_code:
    html(html_code, height=300)