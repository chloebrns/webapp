import streamlit as st

st.title("Formulaire")
with st.form("Form1"):
    user_name = st.text_input("Entrez votre nom")
    user_firstname = st.text_input("Entrez votre prénom")
    user_age = st.select_slider("Ton âge", options=range(0,99))
    user_etude = st.selectbox("Ton niveau d'études:", ("BAC","BAC+2","BAC+3","BAC+4","BAC+5"))
    if st.form_submit_button("Send"):
        st.write("Envoyé")

if user_age:
    try:
        age = int(user_age)
        if age < 18:
            st.write("Vous êtes mineur")
        else:
            st.write("Vous êtes majeur")
    except ValueError:
        st.write("Veuillez entrer un âge valide.")
