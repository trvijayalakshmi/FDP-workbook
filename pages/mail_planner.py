import streamlit as st
# from google import genai
st.title("Welcome to MealPlanner")
age = st.number_input("Enter Your Age")
weight = st.number_input("Enter tour weight (kg)")
height = st.number_input("Enter your Height (cm)")
location  =st.text_input("Enter your Location")
goal = st.text_input("Write goal - weight loss, weight gain")
preferences = st.text_input("Enter - vegiterian, non vegiterian")
# if st.button("Generate"):
#     prompt = f'I am ${age} years old person. my weight is ${weight}kg and my height is ${height}cm. I lives in ${location} and my goal to generate weekley meal planner for ${goal} and my preferences are ${preferences}. Generate a mealplanner having brakfast, lunch, snacks and dinner at column and week days at rows. Generate only table as response'

#     client = genai.Client(api_key="AIzaSyAFQntBKa-4WmNDw7bzYiXBbLu0Y9y2Jdw")
#     response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
#     st.write(response.text)
 