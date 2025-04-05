import streamlit as st
import openai
import os
from gtts import gTTS
import base64

# Function to generate and return audio as a downloadable link
def generate_audio(text):
    tts = gTTS(text, lang="en")
    tts.save("response.mp3")
    with open("response.mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()
    # Encode audio to base64 for embedding in Streamlit
    b64_audio = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
    <audio controls>
        <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
    """
    return audio_html
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
    button_prompt = "Show me a boxplot of a dataset of 10 random numbers. " \
    "Tell me the max, min, mean, Quartile 1, median, Quartile 3, and standard deviation of the data. " \
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
    with st.chat_message("assistant"):
        # st.markdown(answer)

    # Generate and display audio response
        audio_html = generate_audio(answer)
        st.markdown(audio_html, unsafe_allow_html=True)

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

    # Generate and display audio response
    audio_html = generate_audio(answer)
    st.markdown(audio_html, unsafe_allow_html=True)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})