import streamlit as st

# ---------------------------------------------------
# Seitenkonfiguration
# ---------------------------------------------------

st.set_page_config(
    page_title="Chemie ohne Kopfschmerzen",
    page_icon="🧪",
    layout="centered"
)

# ---------------------------------------------------
# Modernes Design
# ---------------------------------------------------

st.markdown("""
<style>

/* Hintergrund */
.stApp {
    background:
    linear-gradient(
        180deg,
        #fff8eb 0%,
        #fffdf8 40%,
        #ffffff 100%
    );
}

/* Gesamter Content */
.block-container {
    max-width: 950px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Banner */
img {
    border-radius: 28px;
    box-shadow: 0 18px 45px rgba(0,0,0,0.12);
}

/* Intro Card */
.intro-card {
    background: rgba(255,255,255,0.72);

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.45);

    border-radius: 26px;

    padding: 1.7rem 1.8rem;

    margin-top: 1.8rem;
    margin-bottom: 2rem;

    box-shadow:
        0 12px 35px rgba(0,0,0,0.07),
        inset 0 1px 0 rgba(255,255,255,0.6);

    color: #363645;

    line-height: 1.8;

    font-size: 1.07rem;
}

/* Titel */
.title-text {
    text-align: center;

    font-size: 1.45rem;

    font-weight: 700;

    color: #2f2f3a;

    margin-top: 1rem;
    margin-bottom: 1.3rem;
}

/* Buttons */
.stButton > button {

    width: 100%;

    padding: 0.95rem;

    border-radius: 18px;

    border: 1px solid #efe2c4;

    background: rgba(255,255,255,0.9);

    color: #2f2f3a;

    font-size: 1.06rem;

    font-weight: 650;

    box-shadow:
        0 8px 20px rgba(0,0,0,0.06);

    transition: all 0.22s ease;
}

/* Hover Effekt */
.stButton > button:hover {

    transform: translateY(-3px);

    background: #fff1c9;

    border: 1px solid #f0c96a;

    color: #1d1d28;

    box-shadow:
        0 14px 28px rgba(0,0,0,0.10);
}

/* Kleine Abstände zwischen Buttons */
.element-container {
    margin-bottom: 0.7rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Banner
# ---------------------------------------------------

st.image(
    "assets/banner.png",
    use_container_width=True
)

# ---------------------------------------------------
# Beschreibung
# ---------------------------------------------------

st.markdown("""
<div class="intro-card">

<h2 style="margin-top:0; color:#2f2f3a;">
🧪 Chemie ohne Kopfschmerzen
</h2>

Von Konzentrationen und Teilchen über die Molformel bis zur molaren Masse mit PSE findest du hier alles,
was du für den Chemie-Alltag brauchst.

<br><br>

Der Chemie-Rechner kombiniert Berechnungen, Formeln und automatische Protokolle in einer modernen Oberfläche,
damit Experimente, Aufgaben und Ergebnisse immer übersichtlich bleiben.

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Bereichstitel
# ---------------------------------------------------

st.markdown("""
<div class="title-text">
Wähle einen Bereich aus
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Navigation Buttons
# ---------------------------------------------------

if st.button("🧬 Periodensystem", use_container_width=True):
    st.switch_page("views/periodensystem.py")

if st.button("📚 Formelsammlung", use_container_width=True):
    st.switch_page("views/formelsammlung.py")

if st.button("📓 Logbuch", use_container_width=True):
    st.switch_page("views/logbuch.py")

if st.button("📝 Protokoll", use_container_width=True):
    st.switch_page("views/protokoll.py")