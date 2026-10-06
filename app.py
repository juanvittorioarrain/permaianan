import streamlit as st
import random

st.title(" GAME ADADEH HAHAHA!")

st.image("https://unsplash.com", 
         caption="Dapatkan 10 point kalau bisa HAHAHA!", use_container_width=True)

if "skor" not in st.session_state:
    st.session_state.skor = 0
if "angka1" not in st.session_state:
    st.session_state.angka1 = random.randint(1,10)
    st.session_state.angka2 = random.randint(1,10)

skor_akhir = 10

if st.session_state.skor < skor_akhir:
    a1 = st.session_state.angka1
    a2 = st.session_state.angka2
    kunci = a1 + a2
    
    st.write(f" Skor Anda sekarang: **{st.session_state.skor}** / 10")
    
    jawaban = st.number_input(f"Berapa hasil dari {a1} + {a2}? hayo tebak ezz kok =", step=1, value=0)
    
    if st.button("Yakin Kahh ???"):
        if jawaban == kunci:
            st.session_state.skor += 1
            st.success("🎉 Tumben jago HAHAHA... Skor bertambah!")
            st.session_state.angka1 = random.randint(1, 10)
            st.session_state.angka2 = random.randint(1, 10)
            st.rerun()
        else:
            st.error(" OON aihh kamu... LEMAH.")
else:
    st.balloons() 
    st.success("🏆 Selamat! Anda telah memenangkan pertandingan dengan skor 10!")
    if st.button("Main Lagi 🔄"):
        st.session_state.skor = 0
        st.rerun()
