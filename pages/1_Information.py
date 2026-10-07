import streamlit as st
import json
import os

st.title("👋 Welcome to Smart Study Planner")

st.write("Enter your details to create your personalized study plan.")

st.divider()

FILE_NAME = "study_data.json"

# Check whether user is opening an old plan
open_saved = st.session_state.get("new_plan", True) == False

# Load saved information only when opening saved plan
saved_info = {}

if open_saved and os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    saved_info = data.get("student", {})

st.subheader("👤 Student Information")

name = st.text_input(
    "Student Name",
    value=saved_info.get("name", "")
)

email = st.text_input(
    "Email",
    value=saved_info.get("email", "")
)

program = st.text_input(
    "Program",
    value=saved_info.get("program", "")
)

semester_options = [
    "1st Semester",
    "2nd Semester",
    "3rd Semester",
    "4th Semester",
    "5th Semester",
    "6th Semester",
    "7th Semester",
    "8th Semester"
]

saved_semester = saved_info.get("semester", "1st Semester")

semester = st.selectbox(
    "Semester",
    semester_options,
    index=semester_options.index(saved_semester)
)

st.divider()

# Save Information
if st.button("💾 Save Information"):

    if not name or not email or not program:

        st.warning("⚠️ Please fill in all the details.")

    else:

        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
        else:
            data = {
                "student": {},
                "subjects": []
            }

        data["student"] = {
            "name": name,
            "email": email,
            "program": program,
            "semester": semester
        }

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        st.session_state["new_plan"] = False

        st.success("✅ Information saved successfully!")

st.divider()

# Next button
if st.button("➡️ Next: Study Plan"):

    if name and email and program:

        st.session_state["student"] = {
            "name": name,
            "email": email,
            "program": program,
            "semester": semester
        }

        st.switch_page("pages/2_Study_Plan.py")

    else:

        st.warning("⚠️ Please fill in all the details first.")

st.divider()

# Home button
if st.button("⬅️ Back: Home"):
    st.switch_page("app.py")