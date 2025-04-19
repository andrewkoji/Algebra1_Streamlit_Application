import streamlit as st
import requests
import openai
import os
import re
import numpy 
import random
import asyncio  # Import asyncio to handle asynchronous calls



def XY_solution():
    """Generate a random equation ax + by = c and ensure there is always a valid (x, y) pair that satisfies it."""
    # Generate random coefficients for the equation
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    # Ensure a and b are not both zero to avoid a degenerate equation
    while a == 0 and b == 0:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

    # Randomly choose a valid (x, y) pair
    x = random.randint(-25, 25)
    y = random.randint(-25, 25)

    # Calculate c to ensure the equation is satisfied
    c = a * x + b * y

    # Find all valid (x, y) pairs
    valid_pairs = []
    invalid_pairs = []  # List to store invalid pairs for debugging
    for x_candidate in range(-25, 26):  # Iterate through possible values of x
        for y_candidate in range(-25, 26):  # Iterate through possible values of y
            if a * x_candidate + b * y_candidate == c:  # Check if the equation is satisfied
                valid_pairs.append((x_candidate, y_candidate))  # Add the valid pair to the list
            else:
                invalid_pairs.append((x_candidate, y_candidate))  # Add the invalid pair to the list
    for x_candidate in range(-25, 26):  # Iterate through possible values of x
        for y_candidate in range(-25, 26):  # Iterate through possible values of y
            if a * x_candidate + b * y_candidate == c:  # Check if the equation is satisfied
                valid_pairs.append((x_candidate, y_candidate))  # Add the valid pair to the list

    # Select a random solution from the valid pairs
    solution = random.choice(valid_pairs)
    non_solutions = random.sample(invalid_pairs, min(3, len(invalid_pairs)))  # Select up to 3 random non-solutions
    result = {
        "equation": f"{f'{a}x ' if a != 0 else ''}{f'+ {b}y ' if b > 0 else f'- {-b}y ' if b < 0 else ''}= {c}".strip(),
        "solution": solution,
        "verification": f"{a}({solution[0]}) + {b}({solution[1]}) = {c}",
        "Non-solutions": non_solutions,
    }

    return result

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_quiz_questions(num_questions): 
    """Generate the specified number of quiz questions using OpenAI API with unique prompts for each solution."""
    questions = []
    for i in range(num_questions):
        xy_result = solutions[i]  # Get the corresponding solution for this question
        prompt = (
            f"Create a unique multiple-choice question related to determining which point lies on a given line in Standard form. "
            f"Format it as follows:\n"
            f"Question: [Which point lies on the following line for the equation: {xy_result['equation']}?]\n"
            f"make {xy_result['solution']} one of the options\n"
            "A) [Option 1]\n"
            "B) [Option 2]\n"
            "C) [Option 3]\n"
            "D) [Option 4]\n"
            f"Correct Answer: [Option letter]) {xy_result['solution']}\n"
            "Make sure the answer is option is randomly placed and only one of the options is correct.\n"
            "Make sure the options are unique and not similar to each other.\n"
            "Make sure you write y instead of 1y, and x instead of 1x, -y instead of -1y, -x instead of -1x.\n"
        )
        response = await openai.ChatCompletion.acreate(  # Await the asynchronous call
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates quiz questions."},
                {"role": "user", "content": prompt}
            ]
        )
        questions.append(response["choices"][0]["message"]["content"].strip())

    return questions

# Basic Quiz Application
# Center the title using Streamlit's markdown with alignment
st.markdown("<h1 style='text-align: center;'>Verifying Solutions Quiz</h1>", unsafe_allow_html=True)
# Move the "Generate New Questions" button to appear with the question number input
# st.write("### Enter the number of questions for the quiz:")
num_questions = 5    # st.number_input("Number of Questions", min_value=1, max_value=20, value=10, step=1)

if st.button("Generate New Quiz"):
    # Generate a list of equations and solutions for use in the quiz
    solutions = [XY_solution() for _ in range(num_questions)]

    # Generate only the number of questions requested
    async def generate_and_store_questions():
        st.session_state.quiz_data_list = await generate_quiz_questions(num_questions)

    asyncio.run(generate_and_store_questions())  # Run the asynchronous function

quiz_data_list = st.session_state.get("quiz_data_list", [])

# Add a score counter and ensure all questions are answered before scoring
if "score" not in st.session_state:
    st.session_state.score = 0

# Ensure answers list is dynamically resized when new questions are generated
if "answers" not in st.session_state or len(st.session_state.answers) != len(quiz_data_list):
    st.session_state.answers = [None] * len(quiz_data_list)

# Display the current score
st.write(f"### Current Score: {st.session_state.score}")

# Collect answers for all questions
for i, quiz_data in enumerate(quiz_data_list):
    st.header('',divider="rainbow")
    st.write(f"### Question {i + 1}")

    try:
        # Ensure `quiz_data` is a string before splitting
        if isinstance(quiz_data, str):
            lines = quiz_data.split("\n")
        else:
            raise ValueError("Invalid quiz data format.")

        question = lines[0].strip().replace("Question: ", "")
        options = []

        # Handle cases where options are on a single line
        for line in lines[1:]:
            if re.match(r"[A-D]\)", line):  # Match lines starting with A), B), C), or D)
                options.append(line.split(") ")[1].strip())
            elif re.match(r".*A\).*B\).*C\).*D\).*", line):  # Match single-line options
                options = [opt.strip() for opt in re.split(r"[A-D]\)", line) if opt.strip()]
                break

        # Extract the correct answer
        correct_answer_line = next((line for line in lines if line.startswith("Correct Answer:")), None)
        if correct_answer_line:
            correct_answer = correct_answer_line.split(": ")[1].strip()[2:]
        else:
            raise ValueError("Correct answer not found in quiz data.")
    except (IndexError, ValueError) as e:
        # Debugging: Display the problematic quiz data
        st.error(f"Error parsing the quiz data for Question {i + 1}. Regenerating the quiz...")
        st.write(f"Debug Info: {quiz_data}")  # Show the raw quiz data for debugging
        st.write(f"Error Details: {e}")  # Show the error details

        # Simulate clicking the "Generate New Quiz" button
        solutions = [XY_solution() for _ in range(num_questions)]

        async def regenerate_quiz():
            st.session_state.quiz_data_list = await generate_quiz_questions(num_questions)

        asyncio.run(regenerate_quiz())  # Run the asynchronous function

        # Reset the quiz data and reload the page
        st.session_state.quiz_data_list = []
        st.session_state.score = 0
        st.query_params.clear()  # Reset the query parameters to reload the page

        # Exit the loop after regeneration is complete
        break  # Exit the loop to avoid further processing of invalid data

    # Update the options to render in LaTeX format
    latex_options = [f"${option}$" for option in options]

    # Display the question and options
    
    st.write(question)
    selected_answer = st.radio(f"Choose your answer for Question {i + 1}:", latex_options, key=f"question_{i}")

    # Add a button to submit the answer for the current question
    if st.button(f"Submit Answer for Question {i + 1}", key=f"submit_{i}"):
        user_answer = selected_answer.replace("$", "").strip()  # Remove LaTeX formatting and strip spaces

        # Refine the normalization logic to handle LaTeX-rendered options consistently
        def normalize_answer(text):
            """Normalize answers by removing LaTeX formatting, extra spaces, and ensuring consistent case."""
            text = re.sub(r"\\[a-zA-Z]+|\$|{|}|\\", "", text)  # Remove LaTeX commands and symbols
            return "".join(text.split()).lower()  # Remove extra spaces and convert to lowercase

        # Normalize user and correct answers
        normalized_user_answer = normalize_answer(user_answer)

        try:
            # Extract the correct answer in plain text format
            correct_answer_raw = lines[5].split(": ")[1].strip()
            correct_answer_letter = correct_answer_raw.split(")")[0].strip()  # Extract the letter (e.g., "C")
            correct_answer_text = correct_answer_raw.split(") ")[1].strip()  # Extract the answer text (e.g., "(2, 3)")
            normalized_correct_answer = normalize_answer(correct_answer_text)

            if normalized_user_answer == normalized_correct_answer:
                st.session_state.score += 1  # Increment the score for a correct answer
                st.success("Correct! Well done.")  # Keep the "Correct!" animation
            else:
                # Display the correct answer in plain text format
                st.error(f"Incorrect. The correct answer is {correct_answer_letter}) {correct_answer_text}.")
        except (IndexError, ValueError) as e:
            # Debugging: Display the problematic correct answer parsing
            st.error("Error parsing the correct answer. Regenerating the quiz...")
            st.write(f"Debug Info: {lines}")  # Show the raw lines for debugging
            st.write(f"Error Details: {e}")  # Show the error details

            # Regenerate the quiz
            async def regenerate_quiz():
                st.session_state.quiz_data_list = await generate_quiz_questions(num_questions)

            asyncio.run(regenerate_quiz())  # Run the asynchronous function
            st.experimental_rerun()  # Rerun the Streamlit app to display the new quiz
            break  # Exit the loop to avoid further processing of invalid data

# Display the current score
st.write(f"### Current Score: {st.session_state.score}/{len(quiz_data_list)}")



