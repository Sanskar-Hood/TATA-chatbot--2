import streamlit as st

st.set_page_config(page_title="TATA MOTORS", page_icon=":material/edit:")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.title("TATA MOTORS")
st.text("Unleash the true potential of Tata Vehicles by exploring it with our AI powered ChatBots")
st.text("Get your custom questions answered by us at any scale. Experience the true Next-Gen !!!")

SUVS = st.Page("cars/create.py", title="SUVs", icon=":material/add_circle:")

Sedans = st.Page("cars/delete.py", title="Sedans", icon=":material/square:")

Trucks=st.Page("cars/trucks.py", title='Trucks', icon=":material/circle:")

Buses=st.Page("cars/bus.py", title="Buses", icon=":material/add:")

EVs=st.Page("cars/EV.py", title="EVs", icon=":material/thumb_up:")



search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")


pg = st.navigation(
        {
            "Cars": [SUVS,Sedans,EVs],
            "Buses" : [Buses],
            "Trucks" : [Trucks],

            "Tools": [search, history],
        })
pg.run()

