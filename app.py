
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🎓 Student Placement Prediction System")

st.write("Enter the student's details below.")

# Inputs
cgpa = st.number_input("CGPA", 0.0, 10.0, 7.0)

aptitude = st.number_input("Aptitude Score", 0, 100, 60)

technical = st.number_input("Technical Skill Score", 0, 100, 60)

communication = st.number_input(
    "Communication Score", 0, 100, 60
)

internship = st.selectbox(
    "Internship Experience",
    ["No", "Yes"]
)

projects = st.number_input(
    "Number of Projects", 0, 10, 1
)

backlogs = st.number_input(
    "Number of Backlogs", 0, 10, 0
)

# Prediction button
if st.button("Predict Placement"):

    internship_value = 1 if internship == "Yes" else 0

    student = np.array([[
        cgpa,
        aptitude,
        technical,
        communication,
        internship_value,
        projects,
        backlogs
    ]])

    prediction = model.predict(student)

    if prediction[0] == 1:
        st.success("🎉 Prediction: PLACED")
    else:
        st.error("Prediction: NOT PLACED")
