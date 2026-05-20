import streamlit as st

st.set_page_config(page_title="Formelsammlung", layout="wide")

st.title("📚 Formelsammlung")

st.markdown("---")

st.write("""
Hier findest du wichtige Formeln und Berechnungen für den Chemie Alltag.

Von Konzentrationen und Teilchen über die Molformel bis zur molaren Masse mit PSE – alles an einem Ort!

Klicke einfach auf die Buttons, um zu den jeweiligen Themen zu gelangen. 🧪
""")

st.markdown("---")


# BUTTON DESIGN
st.markdown("""
<style>

div.stButton > button {
    height: 80px;
    font-size: 24px;
    font-weight: 600;
    border-radius: 18px;
    margin-bottom: 18px;
}

</style>
""", unsafe_allow_html=True)


# BUTTONS UNTEREINANDER

if st.button(
    "🧪 Konzentrationen und Teilchen",
    use_container_width=True
):
    st.switch_page("views/formelsammlung_konzentrationen.py")


if st.button(
    "🧬 Die Molformel",
    use_container_width=True
):
    st.switch_page("views/formelsammlung_molformel.py")


if st.button(
    "⚗️ Die molare Masse mit PSE",
    use_container_width=True
):
    st.switch_page("views/formelsammlung_molmasse.py")