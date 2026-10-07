import streamlit as st
import os

st.set_page_config(
    page_title="Smart Study Planner",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Smart Study Planner")

st.write(
    "Create a personalized study plan, manage your subjects, "
    "and track your progress."
)

st.divider()

# -----------------------------
# Create New Plan
# -----------------------------
if st.button("🆕 Create New Plan", use_container_width=True):

    # Clear all previous session data
    st.session_state.clear()

    # Mark this as a new plan
    st.session_state["new_plan"] = True

    # Delete old saved plan
    if os.path.exists("study_data.json"):
        os.remove("study_data.json")

    # Go to Student Information page
    st.switch_page("pages/1_Information.py")


# -----------------------------
# Open Saved Plan
# -----------------------------
if st.button("📂 Open Saved Plan", use_container_width=True):

    if os.path.exists("study_data.json"):

        # Mark this as opening an existing plan
        st.session_state["new_plan"] = False

        # Go to Student Information page
        st.switch_page("pages/1_Information.py")

    else:
        st.warning("⚠️ No saved plan found yet.")


st.divider()

st.info(
    "💡 Create a new plan if you are starting fresh. "
    "Choose Open Saved Plan to continue with your previous plan."
)