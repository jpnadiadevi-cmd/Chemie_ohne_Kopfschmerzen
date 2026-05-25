import streamlit as st

st.set_page_config(
    page_title="Formelsammlung",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fff8eb 0%, #fffdf8 45%, #ffffff 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero-card {
    background: rgba(255,255,255,0.82);
    border-radius: 26px;
    padding: 1.8rem 2rem;
    box-shadow: 0 12px 35px rgba(0,0,0,0.07);
    border: 1px solid rgba(255,255,255,0.5);
    margin-bottom: 2rem;
}

.hero-card h1 {
    margin: 0;
    font-size: 2.6rem;
    color: #30303d;
}

.hero-card p {
    margin-top: 0.9rem;
    font-size: 1.08rem;
    line-height: 1.7;
    color: #5b5b68;
}

.section-title {
    text-align: center;
    font-size: 1.4rem;
    font-weight: 750;
    color: #30303d;
    margin-bottom: 1.4rem;
}

.stButton > button {
    height: 85px;
    font-size: 1.15rem;
    font-weight: 700;
    border-radius: 22px;
    border: 1px solid #efe2c4;
    background: rgba(255,255,255,0.9);
    color: #30303d;
    box-shadow: 0 8px 22px rgba(0,0,0,0.07);
    transition: all 0.22s ease;
    margin-bottom: 1rem;
}

.stButton > button:hover {
    transform: translateY(-3px);
    background: #fff1c9;
    border-color: #f0c96a;
    box-shadow: 0 14px 30px rgba(0,0,0,0.11);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-card">
    <h1>📚 Formelsammlung</h1>
    <p>
        Hier findest du wichtige Formeln und Berechnungen für den Chemie-Alltag.
        Von Konzentrationen und Teilchen über die Molformel bis zur molaren Masse mit PSE –
        alles übersichtlich an einem Ort.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
Wähle ein Thema aus
</div>
""", unsafe_allow_html=True)

if st.button("🧪 Konzentrationen und Teilchen", use_container_width=True):
    st.switch_page("views/formelsammlung_unterseiten/formelsammlung_konzentrationen.py")

if st.button("🧬 Die Molformel", use_container_width=True):
    st.switch_page("views/formelsammlung_unterseiten/formelsammlung_molformel.py")

if st.button("⚗️ Die molare Masse mit PSE", use_container_width=True):
    st.switch_page("views/formelsammlung_unterseiten/formelsammlung_molmasse.py")