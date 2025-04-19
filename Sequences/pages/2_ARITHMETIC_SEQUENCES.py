import streamlit as st
import random
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# SECTION: Generate Arithmetic Sequence
if "m" not in st.session_state:
    st.session_state.m = np.random.randint(-30, 50)
if "b" not in st.session_state:
    st.session_state.b = np.random.randint(-300, 300)

m = st.session_state.m
b = st.session_state.b
sequence = [(m)*x + b for x in range(0, 200)]
df = pd.DataFrame(sequence, columns=["Arithmetic Sequence"])
sequence = df.to_dict(orient="records")

# SECTION: Display Header and Formula
st.markdown("<h1 style='text-align: center;'>Arithmetic Sequences</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Explicit Formula:</h2>", unsafe_allow_html=True)
st.latex(r"""a_n = a_1 + (n-1)d""")

# SECTION: Explain Formula Components
st.divider()
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.latex(r"""a_n""")
    st.markdown("<p style='text-align: center;'>nth term of the sequence</p>", unsafe_allow_html=True)
with col2:
    st.latex(r"""a_1""")
    st.markdown("<p style='text-align: center;'>first term of the sequence</p>", unsafe_allow_html=True)
with col3:
    st.latex(r"""n""")
    st.markdown("<p style='text-align: center;'>the term position in the sequence</p>", unsafe_allow_html=True)
with col4:
    st.latex(r"""d""")
    st.markdown("<p style='text-align: center;'>common difference</p>", unsafe_allow_html=True)

st.header("", divider='rainbow')

# SECTION: Input for Term Position (n)
col1, col2 = st.columns([1, 3])
with col1:
    n = st.number_input("Enter a value for n:", min_value=1, max_value=len(df['Arithmetic Sequence']), value=4, step=1, label_visibility="visible")
with col2:
    st.write("")  # Empty space for alignment

# SECTION: Calculate Values for Formula
if "a_1" not in st.session_state:
    st.session_state.a_1 = df['Arithmetic Sequence'][0]
if "d" not in st.session_state:
    st.session_state.d = df['Arithmetic Sequence'][1] - df['Arithmetic Sequence'][0]

a_1 = st.session_state.a_1
d = st.session_state.d
a_n = a_1 + (n - 1) * d  # Ensure this value is not recalculated dynamically

# SECTION: Display Example Sequence
st.markdown("<h3 style='text-align: left;'>Example: Consider the sequence:</h4>", unsafe_allow_html=True)
st.markdown(
    f"<h3 style='text-align: center;'>"
    f"<span style='color: blue;'>{a_1}</span>, "
    f"<span style='color: red;'>{a_1 + d}</span>, "
    f"{', '.join(map(str, df['Arithmetic Sequence'][2:5].tolist()))}..."
    f"</h3>",
    unsafe_allow_html=True
)

# SECTION: Prompt to Find nth Term
st.markdown("<h4 style='text-align: left;'>Find the {}{} term of the sequence.</p>".format(n, 'st' if str(n).endswith('1') else 'nd' if str(n).endswith('2') else 'rd' if str(n).endswith('3') else 'th'), unsafe_allow_html=True)

# SECTION: Display Values Needed for Formula
with st.expander("You need these values for the formula:"):
    st.markdown("<h4 style='text-align: Left;'>Value of n:</h3>", unsafe_allow_html=True)
    st.latex(r"""n = {}""".format(n))
    st.markdown("<h4 style='text-align: Left;'>1st term of the sequence</h3>", unsafe_allow_html=True)
    st.latex(r"""a_1 = {}""".format(a_1))
    if a_1 > 0:
        text = (
            "Common Difference: 2nd term - 1st term = "
            f"<span style='color: red;'>{a_1 + d}</span> - "
            f"<span style='color: blue;'>{a_1}</span>"
        )
    else:
        text = (
            "Common Difference: 2nd term - 1st term = "
            f"<span style='color: red;'>{a_1 + d}</span> - "
            f"(<span style='color: blue;'>{a_1}</span>)"
        )
    st.markdown(f"<h4 style='text-align: Left;'>{text}</h3>", unsafe_allow_html=True)
    st.latex(r"""d = {}""".format(d))

# SECTION: Validate Input and Display Answer
with st.expander("Click here to show answer"):
    st.latex(r"""a_n = a_1 + (n-1)d""")
    st.divider()
    st.latex(r"""a_{{{}}} = {} + ({}-1)({})""".format(n, a_1, n, d))  # Wrap n in curly braces
    st.divider()
    st.latex(r"""a_{{{}}} = {}""".format(n, a_n))  # Wrap n in curly braces

# Input for user to try their answer
answer = st.number_input("Try:", value=0, step=1, label_visibility="visible")  # Set default value to 0

# Only run the logic if the user has entered a value
if answer != 0:
    if answer == a_n:  # Compare numeric values
        st.success("Correct!")
    else:
        st.error("Incorrect. Try again.")

