import streamlit as st
import random
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



# SECTION: Generate Arithmetic Sequence
if "m" not in st.session_state:
    st.session_state.m = np.random.randint(1, 5)
if "b" not in st.session_state:
    st.session_state.b = np.random.choice(list(range(-10, 0)) + list(range(1, 10)))

m = st.session_state.m
b = st.session_state.b
arith_sequence = [(m)*x + b for x in range(0, 200)]

# Handle overflow in geometric sequence by capping large values
geo_sequence = []
for x in range(0, 200):
    try:
        value = m * (b ** x)
        if abs(value) > 1e308:  # Cap values exceeding the floating-point limit
            value = float('inf') if value > 0 else float('-inf')
        geo_sequence.append(value)
    except OverflowError:
        geo_sequence.append(float('inf') if b > 0 else float('-inf'))

df_arith = pd.DataFrame(arith_sequence, columns=["Arithmetic Sequence"])
df_geo = pd.DataFrame(geo_sequence, columns=["Geometric Sequence"])

arith_sequence = df_arith.to_dict(orient="records")
a_1_arith = df_arith['Arithmetic Sequence'][0]
a_1_geo = df_geo['Geometric Sequence'][0]
d = df_arith['Arithmetic Sequence'][1] - df_arith['Arithmetic Sequence'][0]
r = df_geo['Geometric Sequence'][1] / df_geo['Geometric Sequence'][0]



col_1,col_2 = st.columns(2)

with col_1:
    st.markdown("<h2 style='text-align: center;'>Arithmetic Sequence</h2>", unsafe_allow_html=True)
    st.markdown("<li>Number gets added each time</li>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<h2 style='text-align: center;'>Geometric Sequence</h2>", unsafe_allow_html=True)
    st.markdown("<li>Number gets multiplied each time</li>", unsafe_allow_html=True)
with col_2:
    if d == 0:
        pass
    else:
        st.markdown(
            f"<h2 style='text-align: center;'>"
            # f"<span style='color: blue;'>{a_1_arith}</span>, "
            # f"<span style='color: red;'>{a_1_arith + d}</span>, "
            f"{', '.join(map(str, df_arith['Arithmetic Sequence'][:5].tolist()))},..."
            f"</h3>",
            unsafe_allow_html=True
        )
        st.markdown("<li>Common Difference: {}</li>".format(d), unsafe_allow_html=True)
        st.divider()
        st.markdown(
            f"<h2 style='text-align: center;'>"
            # f"<span style='color: blue;'>{a_1_geo}</span>, "
            # f"<span style='color: red;'>{a_1_geo * r}</span>, "
            f"{', '.join(map(str, df_geo['Geometric Sequence'][:4].tolist()))},..."
            f"</h3>",
            unsafe_allow_html=True
        )
        st.markdown("<li>Common Ratio: {}</li>".format(r), unsafe_allow_html=True)
# SECTION: Animated Square Pattern
st.title("Patterns - Visual")

# Create a figure for the animation
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_xlim(-5, 100)
ax.set_ylim(-5, 5)
ax.axis('off')

# Define the square coordinates globally for reuse
x = [-1, 1, 1, -1, -1]
y = [-1, -1, 1, 1, -1]

# Create a slider to control the number of squares
n = st.slider("n", min_value=1, max_value=10, value=1, step=1)

def make_square(shift_x):
    x = [-1, 1, 1, -1, -1]
    y = [-1, -1, 1, 1, -1]
    # Corrected x-coordinates by adding shift_x directly
    line, = ax.plot([i + shift_x for i in x], y, lw=2, color='blue')
    return line

# Generate the squares for all configurations up to n
shift = 0  # Initialize the horizontal shift
for current_n in range(1, n + 1):
    num_boxes = 2 * current_n - 1  # Calculate the number of boxes for the current configuration
    for i in range(num_boxes):
        make_square(shift + 2 * i)  # Apply the shift for the current configuration
    shift += 2 * num_boxes + 5  # Update the shift for the next configuration, adding 1 unit of spacing

# Initialize the line for animation
line, = ax.plot(x, y, lw=2, color='blue')

# Animation function
def update(frame):
    scale = 1 + 0.1 * frame  # Scale the square
    new_x = [i * scale for i in x]
    new_y = [i * scale for i in y]
    line.set_data(new_x, new_y)
    return line,

# Create the animation
frames = 10  # Number of frames
ani = FuncAnimation(fig, update, frames=frames, interval=100, blit=True)

# Display the animation in Streamlit
st.pyplot(fig)


