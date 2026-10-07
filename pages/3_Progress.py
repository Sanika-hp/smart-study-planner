import streamlit as st
import json
import os

st.title("📊 Progress")

st.write("Track your study hours and progress.")

st.divider()

FILE_NAME = "study_data.json"

# Load saved plan
if os.path.exists(FILE_NAME):

    with open(FILE_NAME, "r") as file:
        data = json.load(file)

else:

    data = {
        "student": {},
        "subjects": []
    }


subjects = data.get("subjects", [])

if not subjects:

    st.info(
        "📚 Please create and save your Study Plan first."
    )

else:

    st.subheader("📚 Study Progress")

    total_planned_hours = 0
    total_completed_hours = 0

    for i, subject in enumerate(subjects):

        st.markdown(
            f"### 📘 {subject['name']}"
        )

        col1, col2 = st.columns(2)

        saved_planned = subject.get(
            "planned_hours",
            2
        )

        saved_completed = subject.get(
            "completed_hours",
            0
        )

        with col1:

            planned_hours = st.number_input(
                "Planned Study Hours",
                min_value=1.0,
                max_value=100.0,
                value=float(saved_planned),
                step=0.5,
                key=f"planned_{i}"
            )

        with col2:

            completed_hours = st.number_input(
                "Hours Studied",
                min_value=0.0,
                max_value=float(planned_hours),
                value=min(
                    float(saved_completed),
                    float(planned_hours)
                ),
                step=0.5,
                key=f"completed_{i}"
            )

        subject_progress = (
            completed_hours / planned_hours
        )

        st.progress(subject_progress)

        st.write(
            f"**{completed_hours:.1f} / "
            f"{planned_hours:.1f} hours** completed"
        )

        st.write(
            f"Progress: **"
            f"{subject_progress * 100:.0f}%**"
        )

        subject["planned_hours"] = planned_hours
        subject["completed_hours"] = completed_hours

        total_planned_hours += planned_hours
        total_completed_hours += completed_hours

        st.divider()


    overall_progress = (
        total_completed_hours /
        total_planned_hours
        if total_planned_hours > 0
        else 0
    )

    st.subheader("📈 Overall Progress")

    st.progress(overall_progress)

    st.write(
        f"### {overall_progress * 100:.0f}%"
    )

    st.write(
        f"**{total_completed_hours:.1f} / "
        f"{total_planned_hours:.1f} hours studied**"
    )

    st.divider()

    if st.button("💾 Save Progress"):

        data["subjects"] = subjects

        with open(FILE_NAME, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

        st.success(
            "✅ Progress saved successfully!"
        )


    if overall_progress == 1:

        st.success(
            "🎉 You completed all your planned study hours!"
        )

    elif overall_progress >= 0.5:

        st.info(
            "👍 Good progress! Keep going!"
        )

    else:

        st.warning(
            "📚 Keep studying. You've got this!"
        )


st.divider()

if st.button("⬅️ Back: Study Plan"):

    st.switch_page(
        "pages/2_Study_Plan.py"
    )