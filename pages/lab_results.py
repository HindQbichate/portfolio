import streamlit as st
import pandas as pd

st.title("Lab results")
st.write("Running time (in seconds) of the sorting algorithms of TP2, "
         "depending on the size of the list.")


@st.cache_data
def load_results(path):
    return pd.read_csv(path)


df = load_results("assets/tp2_results.csv")

# une colonne par algorithme, une ligne par taille n
table = df.pivot(index="n", columns="algorithm", values="time")

st.line_chart(table)
st.dataframe(table)