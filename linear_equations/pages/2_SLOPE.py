import streamlit as st
import pandas as pd
import numpy as np
import random
import fractions
import signal
import sys
import requests
from streamlit.components.v1 import html



response = requests.get('https://fastapi-b6dv.onrender.com/linear-equation')


# if response.status_code == 200:
#     linear_function = response.json()
# else:
#     st.write("Error fetching linear equation.")


# st.header("SLOPE")

def SLOPE():
    a = np.random.randint(-15, 15)
    b = np.random.randint(-10, 10)
    c = np.random.randint(-50, 50)
    d = np.random.randint(-5, 5)
   
    # Calculate the slope (m) using the formula m = (y2 - y1) / (x2 - x1)
    if (c-a) == 0:
        slope = "undefined"
    elif (d-b) == 0:
        slope =  "zero"
    else:
        num = d - b
        denom = c - a
        slope = fractions.Fraction(num, denom)
        slope = str(slope).replace('/', ' / ')
    return {
        "point1": f'({a},{b})',
        "point2": f'({c},{d})',
        "slope": slope,
        "formula": rf'\frac{{({d}) - ({b})}}{{({c}) - ({a})}} = \frac{{{d - b}}}{{{c - a}}} = {slope}'
    }


if st.button("Generate New Examples"):
    st.query_params.clear()  # Simulate a page reload to generate new examples

st.markdown("<h3 style='text-align: center;'>SLOPE</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Slope of a line passing through two points</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>RISE OVER RUN</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Slope (m) = (y2 - y1) / (x2 - x1)</h4>", unsafe_allow_html=True)

st.header("", divider="rainbow")

# st.markdown("<h3 style='text-align: center;'>Real-Time LaTeX Preview</h3>", unsafe_allow_html=True)

# # Use HTML and JavaScript for real-time LaTeX rendering
# html_code = """
# <div style="text-align: center;">
#     <div id="latex-output" style="margin-top: 20px; font-size: 20px; color: white; display: inline-block; border: 1px solid #ccc; padding: 10px; min-height: 50px; position: relative;">
#         <span style="color: gray;" id="placeholder">Click here to type...</span>
#         <span id="cursor" style="display: block; position: absolute; width: 2px; height: 20px; background-color: white; animation: blink 1s step-end infinite;"></span>
#     </div>
#     <textarea id="latex-input" placeholder="Enter LaTeX expression..." style="opacity: 0; position: absolute; z-index: -1;"></textarea>
# </div>
# <script>
#     const input = document.getElementById("latex-input");
#     const output = document.getElementById("latex-output");
#     const placeholder = document.getElementById("placeholder");
#     const cursor = document.getElementById("cursor");

#     // Focus on the hidden input when clicking the rendered LaTeX area
#     output.addEventListener("click", () => {
#         input.focus();
#     });

#     // Update the rendered LaTeX in real-time as the user types
#     input.addEventListener("input", () => {
#         const latex = input.value;
#         if (latex.trim() === "") {
#             placeholder.style.display = "inline";
#             output.innerHTML = "";
#         } else {
#             placeholder.style.display = "none";
#             output.innerHTML = katex.renderToString(latex, { throwOnError: false });
#         }
#     });

#     // Ensure the cursor stays visible even when the input loses focus
#     input.addEventListener("blur", () => {
#         cursor.style.display = "block";
#     });

#     // Automatically focus on the hidden input when the page loads
#     window.onload = () => {
#         input.focus();
#     };
# </script>
# <style>
#     @keyframes blink {
#         50% {
#             opacity: 0;
#         }
#     }
# </style>
# <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.13.18/dist/katex.min.css">
# <script src="https://cdn.jsdelivr.net/npm/katex@0.13.18/dist/katex.min.js"></script>
# """

# # Render the HTML and JavaScript
# html(html_code, height=200)

for i in range(1, 4):  # Loop to show 3 examples
    slope_data = SLOPE()
    st.markdown(f"<h3 style='text-align: center;'>Example {i}: SLOPE between two points</h3>", unsafe_allow_html=True)

    col_1, col_2 = st.columns(2)

    with col_1:
        st.latex('(x_1, y_1)')
        point_one = slope_data['point1']
        st.latex(point_one)

    with col_2:
        st.latex('(x_2, y_2)')
        point_two = slope_data['point2']
        st.latex(point_two)

    st.markdown("<h3 style='text-align: center;'>SLOPE formula</h3>", unsafe_allow_html=True)
    st.latex(r'\frac{y_2 - y_1}{x_2 - x_1}')
    st.latex(slope_data["formula"])
    st.divider()  # Add a divider between examples


