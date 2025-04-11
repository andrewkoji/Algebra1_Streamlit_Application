import streamlit as st
import openai
import os
from gtts import gTTS
import base64
import matplotlib.pyplot as plt
import numpy as np

openai.api_key = os.getenv("OPENAI_API_KEY")
# Generate response using OpenAI API

# App title and description
st.markdown("<h3 style='text-align: center;'>🤖📊ALGEBOT</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Ask Algebot a question!</h3>", unsafe_allow_html=True)

# Create three columns for buttons
left, middle_left, middle_right,far_right = st.columns(4)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize a variable to store the button prompt
button_prompt = None

# Check which button is clicked and set the prompt accordingly
if left.button("One Variable Stats", icon="😃", use_container_width=True):
    button_prompt = "Give me a dataset of 10 random numbers " \
    "Tell me the max, min, mean, Quartile 1, median, Quartile 3, and standard deviation of the data. " \

if middle_left.button("Calculator for one variable stats", icon="😊", use_container_width=True):
    button_prompt = "Tell me the keystrokes for using the ti-84 calculator to find the max, min, mean, Quartile 1, median, Quartile 3, and standard deviation of a dataset of 10 random numbers. " \
    "Just tell me how to get to the 1varstats using the stat-calc-1. 1varstats options" \

if middle_right.button("Boxplots", icon="😏", use_container_width=True):
    # Generate a random dataset of 10 numbers
    data = np.random.randint(1, 101, size=10)

    # Create a boxplot
    fig, ax = plt.subplots()
    ax.boxplot(data, vert=False, patch_artist=True)
    ax.set_title("Boxplot of Random Dataset")
    ax.set_xlabel("Value")
    ax.set_yticks([])  # Remove y-axis ticks for simplicity

    # Display the boxplot in Streamlit
    st.pyplot(fig)

    # Display the statistics of the dataset
    st.write(f"Max: {np.max(data)}")
    st.write(f"Min: {np.min(data)}")
    st.write(f"Mean: {np.mean(data):.2f}")
    st.write(f"Quartile 1: {np.percentile(data, 25):.2f}")
    st.write(f"Median: {np.median(data):.2f}")
    st.write(f"Quartile 3: {np.percentile(data, 75):.2f}")
    st.write(f"Standard Deviation: {np.std(data):.2f}")

# If a button was clicked, simulate the chat input
if far_right.button("Clear History", use_container_width=True):
    st.session_state.messages = []  # Clear the chat history
    st.success("Chat history cleared!")


if button_prompt:
    # Add the button prompt to chat history
    st.session_state.messages.append({"role": "user", "content": button_prompt})

    # Generate response using OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        )
        answer = response.choices[0].message["content"]
    except Exception as e:
        answer = f"An error occurred: {e}"

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})

    # Display assistant response in chat message container
    # with st.chat_message("assistant"):
    #     st.markdown(answer)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if user_input := st.chat_input("Pick a level you want to try or ask a question"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response using OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        )
        answer = response.choices[0].message["content"]
    except Exception as e:
        answer = f"An error occurred: {e}"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})