import streamlit as st
from data import PROFILE

st.set_page_config(page_title=PROFILE["name"], page_icon=":briefcase:", layout="wide")

# Bonus Q18 : compteur de visites avec st.session_state
if "visits" not in st.session_state:
    st.session_state["visits"] = 0
st.session_state["visits"] = st.session_state["visits"] + 1

with st.sidebar:
    st.image("assets/photo.png", width=120)
    st.markdown(f"### {PROFILE['name']}")
    st.markdown(f"[GitHub]({PROFILE['github']})")
    st.markdown(f"[LinkedIn]({PROFILE['linkedin']})")
    st.divider()
    st.caption(f"Pages viewed in this session: {st.session_state['visits']}")

pages = [
    st.Page("pages/home.py", title="About me", icon=":material/person:", default=True),
    st.Page("pages/projects.py", title="Projects", icon=":material/code:"),
    st.Page("pages/skills.py", title="Skills", icon=":material/bar_chart:"),
    st.Page("pages/contact.py", title="Contact", icon=":material/mail:"),
    st.Page("pages/lab_results.py", title="Lab results", icon=":material/monitoring:"),
]
st.navigation(pages).run()