import streamlit as st
import os


def main():
    st.markdown("<h3 style='text-align: center; color: White;'>Old Regents Exams</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    def generate_exam_link(year, month, month_name):
        return st.markdown(
            f"""
            <a href="https://www.nysedregents.org/algebraone/{month}{year}/algone{month}20{year}-exam.pdf" target="_blank" style="font-size:20px; font-weight:bold; color:Red; text-decoration:none;">
                📄 {month_name} 20{year} A1R Exam
            </a>
            """,
            unsafe_allow_html=True
        )

    with col1:

        with col1:
            # Define a list of years and months for the exams
            exams = [
                {"year": "24", "month": "6", "month_name": "June"},
                {"year": "23", "month": "6", "month_name": "June"},
                {"year": "22", "month": "6", "month_name": "June"},
                {"year": "20", "month": "6", "month_name": "June"},
                {"year": "19", "month": "6", "month_name": "June"},
            ]

        # Loop through the exams and generate links
        for exam in exams:
            generate_exam_link(exam["year"], exam["month"], exam["month_name"])
    with col2:
        with col1:
            # Define a list of years and months for the exams
            exams = [
                {"year": "24", "month": "1", "month_name": "January"},
                {"year": "23", "month": "1", "month_name": "January"},
                {"year": "22", "month": "1", "month_name": "January"},
                {"year": "20", "month": "1", "month_name": "January"},
                {"year": "19", "month": "1", "month_name": "January"},
            ]

        # Loop through the exams and generate links
        for exam in exams:
            generate_exam_link(exam["year"], exam["month"], exam["month_name"])
    with col3:
        # Define a list of years and months for the exams
        exams = [
            {"year": "24", "month": "8", "month_name": "August"},
            {"year": "23", "month": "8", "month_name": "August"},
            {"year": "22", "month": "8", "month_name": "August"},
            {"year": "20", "month": "8", "month_name": "August"},
            {"year": "19", "month": "8", "month_name": "August"},
        ]

        # Loop through the exams and generate links
        for exam in exams:
            generate_exam_link(exam["year"], exam["month"], exam["month_name"])

if __name__ == "__main__":
    main()