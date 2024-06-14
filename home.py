import streamlit as st

#titre
st.title("Titre 1")

#sous titre
st.subheader("teste")

#texte
st.write("simple text")

#input
user_input = st.text_input("tape du texte")

st.write(user_input)

st.image("https://cdn1.epicgames.com/offer/cbd5b3d310a54b12bf3fe8c41994174f/EGS_VALORANT_RiotGames_S1_2560x1440-d9ca2c0fbaff9d80e8dedfbd726aa438")

with st.form("Form1"):
    user_name = st.text_input("Tape your name:")
    if st.form_submit_button("Send"):
        st.write(user_name)
