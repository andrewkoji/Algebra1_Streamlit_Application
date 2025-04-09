import pandas as pd
import numpy as np
import requests 
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import os


def main():
    data = {
    "Caffeine Consumption(mg)": [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],
    "Sleep Quality Score(out of 10)": [9, 8, 8, 7, 6, 5, 5, 4, 3, 2]
    }
    st.markdown("<h1 style='text-align: center;'>Caffeine Consumption vs Sleep Quality</h1>", unsafe_allow_html=True)
    # Create a pandas DataFrame
    df = pd.DataFrame(data)
    # st.dataframe(df, width=700, height=400)
    # Create a Matplotlib figure for the table
    fig, ax = plt.subplots(figsize=(6, 2))  # Adjust size as needed
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(
        cellText=df.values, 
        colLabels=["Caffeine Consumption (mg)", "Sleep Quality Score (out of 10)"], 
        cellLoc='center', 
        loc='center'
    )
    images_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../images"))
    # Display the PNG in Streamlit
    st.image(os.path.join(images_dir, "Q34june24.png"))
    # Perform linear regression
    x = df["Caffeine Consumption(mg)"]
    y = df["Sleep Quality Score(out of 10)"]
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    # Calculate r^2
    r_squared = r_value**2

    # Display the linear regression equation and statistics
    st.markdown("### LinReg(ax + b):")
    st.markdown(f"<h4>y = ax + b</h4>", unsafe_allow_html=True)
    st.markdown(f"<h4>a = {slope}</h4>", unsafe_allow_html=True)
    st.markdown(f"<h4>b = {intercept:.2f}</h4>", unsafe_allow_html=True)
    st.markdown(f"<h4>y = {slope:.2f}x + {intercept:.2f}</h4>", unsafe_allow_html=True)
    st.markdown(f"<h4>r = {r_value:.2f}</h4>", unsafe_allow_html=True)
    st.markdown(f"<h4>r² = {r_squared:.2f}</h4>", unsafe_allow_html=True)

    # Optional: Plot the data and regression line
    fig, ax = plt.subplots()
    ax.scatter(x, y, label="Data Points", color="blue")
    ax.plot(x, slope * x + intercept, color="red", label="Regression Line")
    ax.set_xlabel("Caffeine Consumption (mg)")
    ax.set_ylabel("Sleep Quality Score(out of 10)")
    ax.set_title("Linear Regression: Caffeine vs Sleep Quality")
    ax.legend()
    st.pyplot(fig)



if __name__ == "__main__":
    main()  