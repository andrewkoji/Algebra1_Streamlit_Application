import streamlit as st


def main():
    # Set up the page configuration
    st.set_page_config(
        page_title="Display PDFs",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Title of the app
    st.markdown("<h1 style='text-align: center;'>Display PDFs</h1>", unsafe_allow_html=True)

    # List of PDF links
    pdf_links = [
        "https://www.jmap.org/Worksheets/S.ID.B.6.Regression1.pdf",
        "https://www.jmap.org/Worksheets/S.ID.B.6.Regression2.pdf",
    ]

    # Display each PDF in the app
    for link in pdf_links:
        st.markdown(f"<iframe src='{link}' width='100%' height='600px'></iframe>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()