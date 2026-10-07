import streamlit as st

st.set_page_config(
    page_title="Progress",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Study Progress")

st.write("Track your preparation and see how much of your study plan is completed.")

st.divider()

# Subject progress
st.subheader("📚 Subject-wise Progress")

subjects = {
    "Python": 75,
    "DBMS": 60,
    "Artificial Intelligence": 50,
    "Data Structures": 65,
    "Web Technology": 80
}

for subject, progress in subjects.items():
    st.write(f"**{subject} — {progress}%**")
    st.progress(progress / 100)

st.divider()

# Overall progress
st.subheader("🎯 Overall Progress")

overall_progress = sum(subjects.values()) / len(subjects)

st.metric(
    "Overall Completion",
    f"{overall_progress:.0f}%"
)

st.progress(overall_progress / 100)

st.divider()

# Study statistics
st.subheader("📈 Study Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Subjects", "5")

with col2:
    st.metric("Completed", "2")

with col3:
    st.metric("Remaining", "3")

st.divider()

# Completed topics
st.subheader("✅ Completed Topics")

completed_topics = [
    "Python Basics",
    "Database Basics",
    "HTML & CSS",
    "AI Introduction"
]

for topic in completed_topics:
    st.write(f"✅ {topic}")

st.divider()

# Goal
st.subheader("🎯 Weekly Goal")

weekly_goal = st.slider(
    "Set your weekly study goal (hours)",
    min_value=1,
    max_value=40,
    value=10
)

hours_completed = st.number_input(
    "Hours completed this week",
    min_value=0,
    max_value=weekly_goal,
    value=6
)

goal_percentage = (hours_completed / weekly_goal) * 100

st.write(
    f"Weekly goal progress: **{goal_percentage:.0f}%**"
)

st.progress(goal_percentage / 100)

if goal_percentage >= 100:
    st.success("🎉 Great job! You completed your weekly study goal!")
elif goal_percentage >= 50:
    st.info("👍 Good progress! Keep going.")
else:
    st.warning("📖 Try to spend more time on your study goal.")

st.divider()

st.info(
    "💡 Tip: Update your progress regularly so you can identify "
    "subjects that need more attention."
)
