import streamlit as st
from data import PROFILE

st.set_page_config(page_title=PROFILE["name"], page_icon=":briefcase:", layout="wide")

with st.sidebar:
    st.image("assets/photo.png", width=120)
    st.markdown(f"### {PROFILE['name']}")
    st.markdown(f"[GitHub]({PROFILE['github']})")      # NOUVEAU
    st.markdown(f"[LinkedIn]({PROFILE['linkedin']})")  # NOUVEAU

pages = [
    st.Page("pages/home.py", title="About me", icon=":material/person:", default=True),
    st.Page("pages/projects.py", title="Projects", icon=":material/code:"),
    st.Page("pages/skills.py", title="Skills", icon=":material/bar_chart:"),
    st.Page("pages/contact.py", title="Contact", icon=":material/mail:"),
]
st.navigation(pages).run()