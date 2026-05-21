import streamlit as st

st.set_page_config(
    page_title="Chemie ohne Kopfschmerzen",
    page_icon="🧪",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fff7e8 0%, #ffffff 55%);
}

.block-container {
    max-width: 950px;
    padding-top: 2rem;
}

img {
    border-radius: 24px;
    box-shadow: 0 14px 35px rgba(0,0,0,0.14);
}

.intro-card {
    background: white;
    padding: 1.5rem 1.7rem;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    border-left: 7px solid #f4c95d;
    font-size: 1.08rem;
    line-height: 1.75;
    margin-top: 1.2rem;
    margin-bottom: 1.8rem;
}

.section-title {
    text-align: center;
    font-size: 1.35rem;
    font-weight: 700;
    margin: 1rem 0 1.2rem 0;
    color: #2f2f3a;
}

.stButton > button {
    width: 100%;
    border-radius: 16px;
    padding: 0.9rem 1rem;
    font-size: 1.05rem;
    font-weight: 650;
    background: #ffffff;
    color: #2f2f3a;
    border: 1px solid #ead9b5;
    box-shadow: 0 6px 18px rgba(0,0,0,0.07);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    background: #fff1c6;
    border-color: #f4c95d;
    color: #1f1f29;
}
</style>
""", unsafe_allow_html=True)

st.image("assets/banner.png", use_container_width=True)

st.markdown("""
<div class="intro-card">
Von Konzentrationen und Teilchen über die Molformel bis zur molaren Masse mit PSE findest du hier alles,
was du für den Chemie-Alltag brauchst. Der Chemie-Rechner kombiniert Berechnungen, Formeln und automatische
Protokolle in einer modernen Oberfläche, damit Experimente, Aufgaben und Ergebnisse immer übersichtlich bleiben. 🧪
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Was möchtest du berechnen oder nachschlagen?</div>', unsafe_allow_html=True)

if st.button("🧬 Periodensystem", use_container_width=True):
    st.switch_page("views/periodensystem.py")

if st.button("📚 Formelsammlung", use_container_width=True):
    st.switch_page("views/formelsammlung.py")

if st.button("📓 Logbuch", use_container_width=True):
    st.switch_page("views/logbuch.py")

if st.button("📝 Protokoll", use_container_width=True):
    st.switch_page("views/protokoll.py")