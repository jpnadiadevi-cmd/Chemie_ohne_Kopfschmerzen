import streamlit as st

# Banner anzeigen
st.image("assets/banner.png", use_container_width=True)

st.title("🧪 Chemie ohne Kopfschmerzen")
st.markdown("Wähle eine Funktion:")

st.markdown("---")

if st.button("🧬 Periodensystem", use_container_width=True):
    st.switch_page("views/periodensystem.py")

if st.button("📚 Formelsammlung", use_container_width=True):
    st.switch_page("views/formelsammlung.py")

if st.button("📓 Logbuch", use_container_width=True):
    st.switch_page("views/logbuch.py")

if st.button("📝 Protokoll", use_container_width=True):
    st.switch_page("views/protokoll.py")