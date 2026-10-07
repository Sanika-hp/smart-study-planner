import streamlit as st
import json
import os

FILE_NAME = "study_data.json"

st.title("📚 Study Plan")

# -----------------------------------
# Load student information
# -----------------------------------

student = st.session_state.get("student", {})

if not student and os.path.exists(FILE_NAME):
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        student = data.get("student", {})
        st.session_state["student"] = student

    except (json.JSONDecodeError, FileNotFoundError):
        student = {}

if not student:
    st.warning("⚠️ Please enter your student information first.")

    if st.button("⬅️ Go to Information"):
        st.switch_page("pages/1_Information.py")

    st.stop()


# -----------------------------------
# Load subjects
# -----------------------------------

if "subjects" not in st.session_state:

    if os.path.exists(FILE_NAME):

        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            st.session_state["subjects"] = data.get("subjects", [])

        except (json.JSONDecodeError, FileNotFoundError):
            st.session_state["subjects"] = []

    else:
        st.session_state["subjects"] = []


subjects = st.session_state["subjects"]


# -----------------------------------
# Student details
# -----------------------------------

st.success(f"Welcome, {student.get('name', 'Student')}! 👋")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Program:** {student.get('program', '')}")

with col2:
    st.write(f"**Semester:** {student.get('semester', '')}")

st.divider()


# -----------------------------------
# Add Subject
# -----------------------------------

st.subheader("➕ Add Subject")

with st.form("add_subject_form"):

    subject_name = st.text_input(
        "Subject Name",
        placeholder="Example: Artificial Intelligence"
    )

    exam_date = st.date_input(
        "Exam Date"
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    study_hours = st.number_input(
        "Study Hours Per Day",
        min_value=1,
        max_value=12,
        value=2,
        step=1
    )

    add_subject = st.form_submit_button(
        "➕ Add Subject",
        use_container_width=True
    )


if add_subject:

    if not subject_name.strip():

        st.warning("⚠️ Please enter a subject name.")

    else:

        new_subject = {
            "name": subject_name.strip(),
            "exam_date": str(exam_date),
            "difficulty": difficulty,
            "hours": study_hours,
            "progress": 0
        }

        subjects.append(new_subject)

        # Save everything
        data = {
            "student": student,
            "subjects": subjects
        }

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        st.session_state["subjects"] = subjects

        st.success(
            f"✅ {subject_name.strip()} added to your study plan!"
        )

        st.rerun()


# -----------------------------------
# Display Study Plan
# -----------------------------------

st.divider()

st.subheader("📅 Your Study Plan")


if not subjects:

    st.info(
        "📖 No subjects added yet. "
        "Add your subjects above to create your study plan."
    )

else:

    for index, subject in enumerate(subjects):

        with st.container(border=True):

            st.markdown(
                f"### 📘 {subject['name']}"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(
                    f"📅 **Exam Date**  \n"
                    f"{subject['exam_date']}"
                )

            with col2:
                st.write(
                    f"⚡ **Difficulty**  \n"
                    f"{subject['difficulty']}"
                )

            with col3:
                st.write(
                    f"⏰ **Study Time**  \n"
                    f"{subject['hours']} hrs/day"
                )

            st.write("📈 **Progress**")

            progress = st.slider(
                "Completion",
                min_value=0,
                max_value=100,
                value=int(subject.get("progress", 0)),
                key=f"progress_slider_{index}"
            )

            subjects[index]["progress"] = progress

            col_a, col_b = st.columns(2)

            with col_a:

                if st.button(
                    "💾 Save Progress",
                    key=f"save_{index}",
                    use_container_width=True
                ):

                    data = {
                        "student": student,
                        "subjects": subjects
                    }

                    with open(FILE_NAME, "w") as file:
                        json.dump(data, file, indent=4)

                    st.success("✅ Progress saved!")


            with col_b:

                if st.button(
                    "🗑️ Remove",
                    key=f"remove_{index}",
                    use_container_width=True
                ):

                    subjects.pop(index)

                    data = {
                        "student": student,
                        "subjects": subjects
                    }

                    with open(FILE_NAME, "w") as file:
                        json.dump(data, file, indent=4)

                    st.rerun()


# -----------------------------------
# Save Entire Plan
# -----------------------------------

st.divider()

if st.button(
    "💾 Save Study Plan",
    use_container_width=True
):

    data = {
        "student": student,
        "subjects": subjects
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    st.success("✅ Study plan saved successfully!")


# -----------------------------------
# Navigation
# -----------------------------------

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    if st.button(
        "⬅️ Information",
        use_container_width=True
    ):
        st.switch_page("pages/1_Information.py")


with col2:

    if st.button(
        "📊 Progress",
        use_container_width=True
    ):
        st.switch_page("pages/3_Progress.py")


with col3:

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):
        st.switch_page("app.py")