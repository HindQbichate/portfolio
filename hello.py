import streamlit as st
print("run")  # Q1 : affiché 4 fois = 1 à l'ouverture + 1 à chaque interaction, car Streamlit relance tout le script à chaque interaction
st.title("Hello!")
name = st.text_input("What is your name?")
if name:
    st.write(f"Nice to meet you, {name}.")
age = st.slider("Your age", 15, 70, 20)

if age < 30:
    st.write(f"You will be 30 in {30 - age} years.")
elif age > 30:
    st.write(f"You turned 30 {age - 30} years ago.")
else:
    st.write("You are 30 this year!")