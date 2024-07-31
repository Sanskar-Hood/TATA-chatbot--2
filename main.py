import streamlit as st

st.set_page_config(page_title="TATA MOTORS", page_icon=":material/edit:")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                 cd        padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.title("TATA MOTORS")
st.text("Unleash the true potential of Tata Vehicles by exploring it with our AI powered ChatBots")
st.text("Get your custom questions answered by us at any scale. Experience the true Next-Gen !!!")

Nexon = st.Page("nexon.py", title="Nexon", icon=":material/add_circle:")

Punch = st.Page("punch.py", title="Punch", icon=":material/square:")


Safari=st.Page("safari.py", title="Safari", icon=":material/thumb_up:")

Harrier = st.Page("harrier.py", title="Harrier ", icon=":material/thumb_up:")

Tiago = st.Page("Tiago.py", title="Tiago ", icon=":material/thumb_up:")

Altroz = st.Page("Altroz.py", title="Altroz ", icon=":material/thumb_up:")
pg = st.navigation(
        {
            "SUVS": [Nexon,Punch,Safari,Harrier],
            "Sedans" :[Tiago,Altroz]

        })


pg.run()

