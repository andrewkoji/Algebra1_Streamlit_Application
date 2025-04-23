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
            <span style="color: gray;" id="placeholder">Enter LaTeX here...</span>
        </div>
        <textarea id="latex-input" placeholder="Enter LaTeX expression..." style="width: 100%; height: 50px; margin-top: 10px;"></textarea>
    </div>
    <script>
        const input = document.getElementById("latex-input");
        const output = document.getElementById("latex-output");
        const placeholder = document.getElementById("placeholder");

        input.addEventListener("input", () => {
            const latex = input.value;
            if (latex.trim() === "") {
                placeholder.style.display = "inline";
                output.innerHTML = "";
            } else {
                placeholder.style.display = "none";
                output.innerHTML = latex;
            }
        });
    </script>
    """

# Render the HTML and JavaScript
if html_code:
    html(html_code, height=300)