import streamlit as st
from utils import check, save

st.title("Contact")
st.write("Leave me a message, I will answer by e-mail.")

with st.form("contact"):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Your message")
    sent = st.form_submit_button("Send")

if sent:
    problems = check(name, email, message)
    if len(problems) > 0:
        for problem in problems:
            st.error(problem)
    else:
        save(name, email, message)
        st.success("Thank you, your message has been sent!")