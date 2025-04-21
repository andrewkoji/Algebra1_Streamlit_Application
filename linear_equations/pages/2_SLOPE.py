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

st.markdown("<h1 style='text-align: center;'>SLOPE</h3>", unsafe_allow_html=True)
st.header("", divider="rainbow")
st.markdown("<h3 style='text-align: center;'>SLOPE formula</h3>", unsafe_allow_html=True)
st.latex(r'\frac{y_2 - y_1}{x_2 - x_1}')

st.header("", divider="rainbow")
st.header("Examples")
st.divider()


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
    

    with st.expander("Show Solution:"):
        st.latex(slope_data["formula"])
    st.divider()  # Add a divider between examples


