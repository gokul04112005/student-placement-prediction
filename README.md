# AI-Based Student Placement Prediction System

## Abstract

This project is a machine learning-based system that predicts whether a student is likely to be placed based on academic and skill-related factors such as CGPA, aptitude score, technical skills, communication skills, internship experience, projects, and backlogs.

A Random Forest classification algorithm is used to train the model and generate placement predictions.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest
- Streamlit

## Features

- Student academic details input
- Aptitude and technical skill assessment
- Internship and project information
- Placement prediction
- Simple Streamlit user interface

## Input Features

- CGPA
- Aptitude Score
- Technical Skill Score
- Communication Score
- Internship Experience
- Number of Projects
- Number of Backlogs

## How It Works

1. Student data is collected.
2. Data is processed using Python.
3. A Random Forest model is trained.
4. The trained model is saved as `placement_model.pkl`.
5. Student details are entered through the Streamlit application.
6. The model predicts the placement status.

## Project Structure

```text
student-placement-prediction/
├── app.py
├── placement_model.pkl
├── requirements.txt
└── README.md
