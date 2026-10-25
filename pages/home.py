import streamlit as st
from data import PROFILE, PROJECTS, SKILLS

st.title(f"Hi, I'm {PROFILE['name']}")
st.subheader(PROFILE["title"])

left, right = st.columns([1, 2])
with left:
    st.image("assets/photo.png", width=220)
with right:
    st.write(PROFILE["about"])
    st.markdown(f"**City:** {PROFILE['city']}")
    st.markdown(f"**Email:** {PROFILE['email']}")
    with open("assets/cv.pdf", "rb") as f:
        st.download_button("Download my CV", f, file_name="cv.pdf")
st.divider()

# Q5 : trouver la meilleure compétence avec une boucle
best = None
for skill in SKILLS:
    if best is None or SKILLS[skill] > SKILLS[best]:
        best = skill

col1, col2, col3 = st.columns(3)
col1.metric("Projects", len(PROJECTS))
col2.metric("Skills", len(SKILLS))
col3.metric("Best skill", best)