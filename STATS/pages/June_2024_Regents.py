import streamlit as st

def main():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Question #34, June 2024 Regents")
        st.image("Q34june24.png")
        
    with col2:
        st.markdown("Score: 4 out of 4")
        st.image("Q34ansjune24.png")
        

if __name__ == "__main__":
    main()