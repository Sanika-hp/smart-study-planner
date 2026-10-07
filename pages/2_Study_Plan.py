import streamlit as st
import json
import os
from datetime import date

st.title("📅 Study Plan")

st.write("Create and save your study timetable.")

st.divider()

FILE_NAME = "study_data.json"

new_plan = st.session_state.get("new_plan", True)

# Load saved subjects ONLY when opening saved plan
if not new_plan and os.path.exists(FILE_NAME):

    with open(FILE_NAME, "r") as file:
        data = json.load(file)

else:

    data = {
        "student": st.session_state.get("student", {}),
        "subjects": []
    }


st.subheader("📚 Subjects and Exam Dates")

num_subjects = st.number_input(
    "Number of Subjects",
    min_value=1,
    max_value=10,
    value=max(1, len(data.get("subjects", []))),
    step=1
)

subjects = []

for i in range(num_subjects):

    col1, col2 = st.columns([0.45, 0.55], gap="small")

    old_subject = ""

    if i < len(data.get("subjects", [])):

        old_subject = data["subjects"][i].get(
            "name",
            ""
        )

    with col1:

        subject_name = st.text_input(
            f"Subject {i + 1}",
            value=old_subject,
            key=f"subject_{i}"
        )

    old_date = date.today()

    if i < len(data.get("subjects", [])):

        try:

            old_date = date.fromisoformat(
                data["subjects"][i].get(
                    "exam_date",
                    str(date.today())
                )
            )

        except:

            old_date = date.today()

    with col2:

        exam_date = st.date_input(
            f"Exam Date {i + 1}",
            value=old_date,
            min_value=date.today(),
            key=f"exam_{i}"
        )

    if subject_name:

        old_completed = False

        if i < len(data.get("subjects", [])):

            old_completed = data["subjects"][i].get(
                "completed",
                False
            )

        subjects.append({
            "name": subject_name,
            "exam_date": str(exam_date),
            "completed": old_completed
        })


st.divider()

if st.button("💾 Save Study Plan"):

    if subjects:

        # Save student information too
        data["student"] = st.session_state.get(
            "student",
            data.get("student", {})
        )

        data["subjects"] = subjects

        with open(FILE_NAME, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

        st.session_state["new_plan"] = False

        st.success(
            "✅ Study plan saved successfully!"
        )

    else:

        st.warning(
            "⚠️ Please enter at least one subject."
        )


st.divider()

st.subheader("📋 Your Saved Timetable")

if data.get("subjects"):

    for subject in data["subjects"]:

        st.write(
            f"📘 **{subject['name']}**"
        )

        st.write(
            f"🗓️ Exam Date: {subject['exam_date']}"
        )

        st.divider()

else:

    st.info("No study plan saved yet.")


col1, col2 = st.columns(2)

with col1:

    if st.button("⬅️ Back: Information"):

        st.switch_page(
            "pages/1_Information.py"
        )


with col2:

    if st.button("➡️ Next: Progress"):

        if subjects:

            st.switch_page(
                "pages/3_Progress.py"
            )

        else:

            st.warning(
                "⚠️ Please save your study plan first."
            )