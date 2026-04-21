import streamlit as st

st.set_page_config(page_title="Formelsammlung", layout="wide")

st.title("📚 Formelsammlung")

st.markdown("---")

# Navigation zu den Unterseiten
if st.button("🧪 Konzentrationen und Teilchen", use_container_width=True):
    st.switch_page("views/formelsammlung/konzentrationen_teilchen.py")

if st.button("🧬 Die Molformel", use_container_width=True):
    st.switch_page("views/formelsammlung/molformel.py")

if st.button("⚗️ Die molare Masse mit PSE", use_container_width=True):
    st.switch_page("views/formelsammlung/molare_masse.py")
