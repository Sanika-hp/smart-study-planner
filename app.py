import streamlit as st
import os

st.set_page_config(
    page_title="Smart Study Planner",
    page_icon="📚",
    layout="centered"
)

st.markdown(
    """
    <style>
    .block-container {
        max-width: 1400px;
        margin: auto;
        padding-top: 50px;
        padding-left: 80px;
        padding-right: 80px;
    }

    h1 {
        font-size: 48px !important;
    }

    h2 {
        font-size: 34px !important;
    }

    h3 {
        font-size: 28px !important;
    }

    p {
        font-size: 20px !important;
    }

    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 20px !important;
        font-weight: 600;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📚 Smart Study Planner")

st.subheader("👋 Welcome!")

st.write(
    "Plan your studies, organize your exams, "
    "and track your progress in one place."
)

st.divider()

st.markdown("### What you can do")

st.write("👤 Enter your student information")
st.write("📅 Create your timetable")
st.write("📊 Track your study progress")

st.divider()

if st.button("🆕 Create New Plan", use_container_width=True):
    st.session_state.clear()
    st.session_state["new_plan"] = True
    st.switch_page("pages/1_Information.py")

if st.button("📂 Open Saved Plan", use_container_width=True):
    if os.path.exists("study_data.json"):
        st.session_state["new_plan"] = False
        st.switch_page("pages/1_Information.py")
    else:
        st.warning("⚠️ No saved plan found yet.")