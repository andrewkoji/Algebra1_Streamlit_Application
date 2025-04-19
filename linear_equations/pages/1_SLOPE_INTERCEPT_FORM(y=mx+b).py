import streamlit as st
import random
import streamlit.components.v1 as components
import fractions
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get('https://fastapi-b6dv.onrender.com/linear-equation')
if response.status_code == 200:
    linear_function = response.json()
else:
    st.write("Error fetching linear equation.")


st.header("Linear Equations - Slope-Intercept Form")

linear_function  = linear_function


def desmos_integration(linear_function):
    slope = linear_function['slope']
    y_intercept = linear_function['y_intercept']

    # Handle slope as a string
    if '/' in slope:
        # If slope is a fraction, split it into numerator and denominator
        numerator, denominator = map(int, slope.split('/'))
    else:
        # If slope is an integer, set denominator to 1
        numerator, denominator = int(slope), 1

    # Calculate the next point with integer coordinates
    if denominator == 1:
        # If slope is an integer, use x=1
        x_next = 1
        y_next = y_intercept + numerator
    else:
        # Use the denominator as the next x and calculate the corresponding y
        x_next = denominator
        y_next = y_intercept + numerator

    # Ensure y_next is an integer
    y_next = int(y_next)

    desmos_script = f"""
    <script src="https://www.desmos.com/api/v1.6/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
    <div id="calculator" style="width: 1000px; height: 1000px;"></div>
    <script>
        var elt = document.getElementById('calculator');
        var calculator = Desmos.GraphingCalculator(elt, {{
            settings: {{
                invertColors: true  // Enable reverse contrast (dark mode)
            }}
        }});
        calculator.setExpression({{ latex: "{linear_function['equation'].replace(' ', '')}" }});
        calculator.setExpression({{ latex: "(0,{y_intercept})", label: 'y-intercept', showLabel: true }});
        calculator.setExpression({{ latex: "({x_next},{y_next})", showLabel: true }});
    </script>
    """
    components.html(desmos_script, height=500)


# Initialize session state for rerun
if "rerun" not in st.session_state:
    st.session_state.rerun = False

# Button to generate a new linear equation
if st.button("Generate New Linear Equation"):
    st.session_state.rerun = not st.session_state.rerun  # Toggle the rerun state

# Fetch the linear equation again if rerun is triggered
if st.session_state.rerun:
    response = requests.get('https://fastapi-b6dv.onrender.com/linear-equation')
    if response.status_code == 200:
        linear_function = response.json()
    else:
        st.write("Error fetching linear equation.")

# Display the equation
st.latex(r"y = mx + b")
st.latex(linear_function["equation"])

# Render slope, y-intercept, and equation as a PNG
fig, ax = plt.subplots(figsize=(5, 1))  # Adjust the figure size as needed
ax.axis('off')  # Turn off axes
text = (
    f"Slope (m): {linear_function['slope']}\n"
    f"y-Intercept (b): {int(linear_function['y_intercept'])}\n"
)
ax.text(0.5, 0.5, text, fontsize=12, ha='center', va='center', wrap=True)  # Center the text
plt.savefig("linear_info.png", bbox_inches='tight', dpi=300)
plt.close(fig)

# Display the PNG in Streamlit
st.image("linear_info.png")
desmos_integration(linear_function)



# Parse the table_of_values from the JSON response
table_of_values = pd.DataFrame(linear_function['table_of_values'])

# Render the DataFrame as a PNG
fig, ax = plt.subplots(figsize=(5, 2))  # Adjust the figure size as needed
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=table_of_values.values, colLabels=table_of_values.columns, loc='center')
plt.savefig("table_of_values.png", bbox_inches='tight', dpi=300)
plt.close(fig)

# Display the PNG in Streamlit
st.image("table_of_values.png")