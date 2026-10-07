import streamlit as st
import json
import os

FILE_NAME = "study_data.json"

st.title("📊 Study Progress")
st.write("Track your progress for each subject.")

st.divider()

# -----------------------------------
# Check saved data
# -----------------------------------

if not os.path.exists(FILE_NAME):
    st.warning("⚠️ No study plan found yet.")

    if st.button("📚 Create Study Plan", use_container_width=True):
        st.switch_page("pages/1_Information.py")

    st.stop()


# -----------------------------------
# Load data
# -----------------------------------

try:
    with open(FILE_NAME, "r") as file:
        data = json.load(file)

except (json.JSONDecodeError, FileNotFoundError):
    st.error("⚠️ Unable to read the saved study plan.")
    st.stop()


student = data.get("student", {})
subjects = data.get("subjects", [])


# -----------------------------------
# Student Information
# -----------------------------------

st.subheader("👤 Student Information")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Name:** {student.get('name', 'Not available')}")
    st.write(f"**Program:** {student.get('program', 'Not available')}")

with col2:
    st.write(f"**Email:** {student.get('email', 'Not available')}")
    st.write(f"**Semester:** {student.get('semester', 'Not available')}")


st.divider()


# -----------------------------------
# Overall Progress
# -----------------------------------

st.subheader("📈 Overall Progress")

if not subjects:

    st.info("📚 No subjects have been added yet.")

else:

    total_progress = 0

    for subject in subjects:
        total_progress += int(subject.get("progress", 0))

    overall_progress = total_progress / len(subjects)

    st.metric(
        "Overall Completion",
        f"{overall_progress:.0f}%"
    )

    st.progress(
        overall_progress / 100
    )

    if overall_progress == 100:
        st.success("🎉 Excellent! You completed all your subjects!")

    elif overall_progress >= 75:
        st.success("🔥 Great progress! Keep going!")

    elif overall_progress >= 50:
        st.info("💪 You're halfway there. Keep studying!")

    elif overall_progress > 0:
        st.warning("📖 Keep working on your subjects!")

    else:
        st.info("🚀 Start studying and update your progress!")


# -----------------------------------
# Subject-wise Progress
# -----------------------------------

st.divider()

st.subheader("📚 Subject-wise Progress")

if subjects:

    for subject in subjects:

        name = subject.get("name", "Unknown Subject")
        progress = int(subject.get("progress", 0))
        exam_date = subject.get("exam_date", "Not specified")
        difficulty = subject.get("difficulty", "Not specified")

        st.markdown(f"### 📘 {name}")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(f"📅 **Exam:** {exam_date}")

        with col2:
            st.write(f"⚡ **Difficulty:** {difficulty}")

        with col3:
            st.write(f"📊 **Progress:** {progress}%")

        st.progress(progress / 100)

        if progress == 100:
            st.success("✅ Completed")

        elif progress >= 75:
            st.info("🔥 Almost completed")

        elif progress >= 50:
            st.warning("💪 Good progress")

        else:
            st.write("📖 Keep studying")

        st.divider()


# -----------------------------------
# Navigation
# -----------------------------------

st.subheader("Navigation")

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "⬅️ Back to Study Plan",
        use_container_width=True
    ):
        st.switch_page("pages/2_Study_Plan.py")


with col2:

    if st.button(
        "🏠 Back to Home",
        use_container_width=True
    ):
        st.switch_page("app.py")