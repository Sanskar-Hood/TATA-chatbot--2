import streamlit as st

st.title("Sedans")

if st.button(label="Tata Tigor",use_container_width=True) :
    st.switch_page("cars/EVS/EV.py")

if st.button(label="Tata Tigor EV",use_container_width=True) :
    st.switch_page("cars/EVS/EV.py")

st.write("              Thats all folks !                          ")