import streamlit as st

st.set_page_config(
    page_title="Information",
    page_icon="ℹ️",
    layout="centered"
)

st.title("ℹ️ Academic Information")

st.write(
    "Welcome to Smart Study Planner! "
    "Use this page to view important academic information."
)

# Student Information
st.subheader("👩‍🎓 Student Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Program:** B.Tech AI & Data Science")
    st.write("**Semester:** 3rd Semester")

with col2:
    st.write("**Department:** AI & Data Science")
    st.write("**Academic Year:** 2026–2027")

st.divider()

# Subjects
st.subheader("📚 Current Subjects")

subjects = [
    "Artificial Intelligence",
    "Data Structures",
    "Database Management System",
    "Python Programming",
    "Web Technology"
]

for i, subject in enumerate(subjects, start=1):
    st.write(f"{i}. {subject}")

st.divider()

# Study Guidelines
st.subheader("📖 Study Guidelines")

guidelines = [
    "Create a daily study schedule.",
    "Give more time to high-priority subjects.",
    "Take short breaks during long study sessions.",
    "Review your notes regularly.",
    "Complete assignments before the deadline.",
    "Practice programming regularly."
]

for guideline in guidelines:
    st.write(f"✅ {guideline}")

st.divider()

# Quick Information
st.subheader("⚡ Quick Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Subjects", "5")

with col2:
    st.metric("Semester", "3")

with col3:
    st.metric("Study Planner", "Active")

st.success(
    "💡 Tip: Consistent daily study is more effective than studying "
    "everything at the last minute."
)
