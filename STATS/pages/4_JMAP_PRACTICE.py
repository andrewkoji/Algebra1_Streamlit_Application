import streamlit as st


def main():
    # Set up the configuration
    st.set_page_config(
        page_title="Display PDFs",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Title of the app
    st.markdown("<h1 style='text-align: center;'>BOXPLOTS</h1>", unsafe_allow_html=True)

    # List of PDF links
    pdf_links = [
        "https://www.jmap.org/Worksheets/S.ID.A.1.BoxPlots1.pdf",
        "https://www.jmap.org/Worksheets/S.ID.A.1.BoxPlots2.pdf",
    ]

    # Display each PDF in the app
    for link in pdf_links:
        st.markdown(f"<iframe src='{link}' width='100%' height='600px'></iframe>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>LINEAR REGRESSION</h1>", unsafe_allow_html=True)
      # List of PDF links
    pdf_links_linreg = [
        "https://www.jmap.org/Worksheets/S.ID.B.6.Regression1.pdf",
        "https://www.jmap.org/Worksheets/S.ID.B.6.Regression2.pdf",
    ]

    # Display each PDF in the app
    for link in pdf_links_linreg:
        st.markdown(f"<iframe src='{link}' width='100%' height='600px'></iframe>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()