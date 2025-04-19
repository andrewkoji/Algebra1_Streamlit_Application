import streamlit as st
import random
import streamlit.components.v1 as components
import fractions
import requests
import numpy as np
import pandas as pd
import os
import openai
import asyncio
import re

def SLOPE():
    a = np.random.randint(-15, 15)
    b = np.random.randint(-10, 10)
    c = np.random.randint(-50, 50)
    d = np.random.randint(-5, 5)
   
    # Calculate the slope (m) using the formula m = (y2 - y1) / (x2 - x1)
    if (c-a) == 0:
        slope = "undefined"
    elif (d-b) == 0:
        slope =  "zero"
    else:
        num = d - b
        denom = c - a
        slope = fractions.Fraction(num, denom)
        slope = str(slope).replace('/', ' / ')
    return {
        "point1": f'({a},{b})',
        "point2": f'({c},{d})',
        "slope": slope,
        "formula": rf'\frac{{({d}) - ({b})}}{{({c}) - ({a})}} = \frac{{{d - b}}}{{{c - a}}} = {slope}'
    }

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_slope_quiz_questions(num_questions):
    """Generate the specified number of slope quiz questions with 3 incorrect slope answers."""
    questions = []
    for i in range(num_questions):
        slope_data = SLOPE()  # Generate slope data using the SLOPE function
        correct_slope = slope_data["slope"]
        point1 = slope_data["point1"]
        point2 = slope_data["point2"]

        # Define the prompt for OpenAI to generate the question
        prompt = (
            f"Create a unique multiple-choice question about calculating the slope of a line passing through two points. "
            f"The points are {point1} and {point2}. The correct slope is {correct_slope}. "
            f"Provide 3 incorrect slope options that are plausible but clearly wrong. "
            f"Format the question as follows:\n"
            f"{{\n"
            f"  \"question\": \"What is the slope of the line passing through the points {point1} and {point2}?\",\n"
            f"  \"options\": [\"Option 1\", \"Option 2\", \"Option 3\", \"Option 4\"],\n"
            f"  \"correct_answer\": \"{correct_slope}\"\n"
            f"}}\n"
            f"Make sure the correct answer is randomly placed among the options, and the incorrect options are unique and not similar to each other.\n"
        )

        # Use OpenAI API to generate the question
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates quiz questions."},
                {"role": "user", "content": prompt}
            ]
        )

        # Parse the response content into a dictionary
        try:
            question_data = eval(response["choices"][0]["message"]["content"].strip())

            # Ensure the correct answer is included in the options
            if question_data["correct_answer"] not in question_data["options"]:
                question_data["options"].append(question_data["correct_answer"])

            # Shuffle the options to randomize their order
            random.shuffle(question_data["options"])

            questions.append(question_data)
        except Exception as e:
            st.error(f"Error parsing question data: {e}")

    return questions

# Streamlit UI
st.markdown("<h1 style='text-align: center;'>Slope Quiz</h1>", unsafe_allow_html=True)

# Number of questions input
num_questions = st.number_input("Number of Questions", min_value=1, max_value=20, value=5, step=1)

# Generate quiz questions
if st.button("Generate New Quiz"):
    async def generate_and_store_questions():
        st.session_state.quiz_data_list = await generate_slope_quiz_questions(num_questions)

    asyncio.run(generate_and_store_questions())

quiz_data_list = st.session_state.get("quiz_data_list", [])

# Initialize score
if "score" not in st.session_state:
    st.session_state.score = 0

# Ensure answers list is dynamically resized
if "answers" not in st.session_state or len(st.session_state.answers) != len(quiz_data_list):
    st.session_state.answers = [None] * len(quiz_data_list)

# Display the current score
st.write(f"### Current Score: {st.session_state.score}")

# Display quiz questions
for i, quiz_data in enumerate(quiz_data_list):
    st.write(f"### Question {i + 1}")
    st.write(quiz_data["question"])

    # Render options in LaTeX format
    latex_options = [f"${option}$" for option in quiz_data["options"]]
    selected_answer = st.radio(
        f"Choose your answer for Question {i + 1}:", latex_options, key=f"question_{i}"
    )

    # Submit answer
    if st.button(f"Submit Answer for Question {i + 1}", key=f"submit_{i}"):
        user_answer = selected_answer.replace("$", "").strip()

        # Normalize answers
        def normalize_answer(text):
            """Normalize answers by removing LaTeX formatting and extra spaces."""
            text = re.sub(r"\\[a-zA-Z]+|\$|{|}|\\", "", text)
            return "".join(text.split()).lower()

        normalized_user_answer = normalize_answer(user_answer)
        normalized_correct_answer = normalize_answer(quiz_data["correct_answer"])

        if normalized_user_answer == normalized_correct_answer:
            st.session_state.score += 1
            st.success("Correct! Well done.")
        else:
            st.error(f"Incorrect. The correct answer is {quiz_data['correct_answer']}.")

# Display final score
st.write(f"### Final Score: {st.session_state.score}/{len(quiz_data_list)}")