import streamlit as st
from gtts import gTTS
import os
import base64



def generate_audio(text):
    tts = gTTS(text, lang="en", tld="com.au", slow=False)
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
