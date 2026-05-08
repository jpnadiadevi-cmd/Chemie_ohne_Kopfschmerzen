import streamlit as st

# Banner anzeigen
st.image("assets/banner.png", use_container_width=True)

st.markdown("""
Von Konzentrationen und Teilchen über die Molformel bis zur molaren Masse mit PSE findest du hier alles, was du für den Chemie Alltag brauchst. Der Chemie Rechner kombiniert Berechnungen, Formeln und automatische Protokolle in einer modernen Oberfläche, damit Experimente, Aufgaben und Ergebnisse immer übersichtlich bleiben. 🧪
""")

st.markdown("---")

if st.button("🧬 Periodensystem", use_container_width=True):
    st.switch_page("views/periodensystem.py")

if st.button("📚 Formelsammlung", use_container_width=True):
    st.switch_page("views/formelsammlung.py")

if st.button("📓 Logbuch", use_container_width=True):
    st.switch_page("views/logbuch.py")

if st.button("📝 Protokoll", use_container_width=True):
    st.switch_page("views/protokoll.py")