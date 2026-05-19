import streamlit as st

st.set_page_config(page_title="Formelsammlung", layout="wide")

st.title("📚 Formelsammlung")

"""Hier findest du wichtige Formeln und Berechnungen für den Chemie Alltag. Von Konzentrationen und Teilchen über die Molformel bis zur molaren Masse mit PSE – alles an einem Ort! Klicke einfach auf die Buttons, um zu den jeweiligen Themen zu gelangen. 🧪"""

st.markdown("---")
    
# Hauptinhalt
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🧪 Konzentrationen und Teilchen", use_container_width=True):
        st.switch_page("views/formelsammlung_konzentrationen.py")

with col2:
    if st.button("🧬 Die Molformel", use_container_width=True):
        st.switch_page("views/formelsammlung_molformel.py")

with col3:
    if st.button("⚗️ Die molare Masse mit PSE", use_container_width=True):
        st.switch_page("views/formelsammlung_molmasse.py")
