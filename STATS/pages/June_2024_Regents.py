import streamlit as st
import os

def main():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Question #34, June 2024 Regents")
        st.image(os.path.join(os.path.dirname(__file__), "Q34june24.png"))
        
    with col2:
        st.markdown("Score: 4 out of 4")
        st.image(os.path.join(os.path.dirname(__file__), "Q34ansjune24.png"))
        

if __name__ == "__main__":
    main()