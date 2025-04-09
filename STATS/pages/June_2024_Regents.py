import streamlit as st
import os

def main():
    # Get the absolute path to the images folder
    images_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../images"))

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Question #34, June 2024 Regents")
        st.image(os.path.join(images_dir, "Q34june24.png"))  # Dynamically constructed path
        
    with col2:
        st.markdown("Score: 4 out of 4")
        st.image(os.path.join(images_dir, "Q34ansjune24.png"))  # Dynamically constructed path

if __name__ == "__main__":
    main()