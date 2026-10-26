import streamlit as st
import pandas as pd
from data import SKILLS, TIMELINE

st.title("Skills")

# Q11 : deux onglets
tab1, tab2 = st.tabs(["Skills", "Education"])

# Onglet 1 : les compétences
with tab1:
    # une barre de progression par compétence
    for skill, level in SKILLS.items():
        st.write(f"**{skill}** : {level}/100")
        st.progress(level / 100)

    # un graphique en barres de toutes les compétences
    st.subheader("All my skills")
    df = pd.DataFrame({"skill": list(SKILLS.keys()), "level": list(SKILLS.values())})
    st.bar_chart(df, x="skill", y="level")

# Onglet 2 : la formation
with tab2:
    for years, school in TIMELINE:
        with st.container(border=True):
            st.markdown(f"**{years}**")
            st.write(school)