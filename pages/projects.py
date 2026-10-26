import streamlit as st
from data import PROJECTS
from utils import all_tags, filter_projects

st.title("Projects")

# Q9 : le filtre par tag
chosen = st.multiselect("Filter by tag", all_tags(PROJECTS))
projects = filter_projects(PROJECTS, chosen)

# Q10 : le tri par année
order = st.selectbox("Sort by year", ["Most recent first", "Oldest first"])
if order == "Most recent first":
    projects = sorted(projects, key=lambda p: p["year"], reverse=True)
else:
    projects = sorted(projects, key=lambda p: p["year"], reverse=False)

# Q9 : le nombre de projets trouvés
st.write(f"{len(projects)} project(s) found")

# Q9 : les cartes sur 2 colonnes
columns = st.columns(2)
for i, project in enumerate(projects):
    with columns[i % 2]:
        with st.container(border=True):
            st.subheader(project["title"])
            st.write(project["description"])
            st.write("Tags: " + ", ".join(project["tags"]))
            st.caption(project["year"])
            st.link_button("See the code", project["link"])