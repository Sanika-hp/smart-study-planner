import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Study Plan",
    page_icon="📚",
    layout="centered"
)

st.title("📚 My Study Plan")
st.write("Plan your study time and keep track of your upcoming exams.")

# Study plan data
study_data = {
    "Subject": ["Python", "DBMS", "Artificial Intelligence", "Data Structures"],
    "Priority": ["High", "Medium", "High", "Medium"],
    "Study Time (hrs)": [2.0, 1.5, 2.0, 1.5],
    "Exam Date": ["15 Oct 2026", "18 Oct 2026", "21 Oct 2026", "24 Oct 2026"]
}

df = pd.DataFrame(study_data)

st.subheader("🗓️ Weekly Study Timetable")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# Total study hours
total_hours = df["Study Time (hrs)"].sum()

st.success(f"⏰ Total Planned Study Time: {total_hours:.1f} hours")

st.divider()

# Add a new study session
st.subheader("➕ Add Study Session")

subject = st.text_input("Subject")

priority = st.selectbox(
    "Priority",
    ["High", "Medium", "Low"]
)

study_hours = st.number_input(
    "Study Time (hours)",
    min_value=0.5,
    max_value=12.0,
    value=1.0,
    step=0.5
)

exam_date = st.date_input("Exam Date")

if st.button("Add to Study Plan"):
    if subject.strip():
        new_row = pd.DataFrame({
            "Subject": [subject],
            "Priority": [priority],
            "Study Time (hrs)": [study_hours],
            "Exam Date": [exam_date.strftime("%d %b %Y")]
        })

        st.success(f"✅ {subject} added to your study plan!")
        st.dataframe(
            pd.concat([df, new_row], ignore_index=True),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.warning("Please enter a subject name.")

st.divider()

st.subheader("💡 Study Tip")

st.info(
    "Give more study time to high-priority subjects and start preparing "
    "early for subjects with upcoming exams."
)
