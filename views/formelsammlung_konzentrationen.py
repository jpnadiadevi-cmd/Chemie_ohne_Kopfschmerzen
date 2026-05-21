import streamlit as st
from datetime import datetime
import json

from utils.storage import save_to_switchdrive


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Konzentrationen & Teilchenzahl",
    page_icon="🧪",
    layout="wide"
)

# ---------------------------------------------------
# DESIGN
# ---------------------------------------------------

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        180deg,
        #fff8eb 0%,
        #fffdf8 45%,
        #ffffff 100%
    );
}

/* Content */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* HERO */
.hero-box {
    background: rgba(255,255,255,0.85);

    border-radius: 28px;

    padding: 2rem;

    box-shadow:
        0 15px 40px rgba(0,0,0,0.08);

    margin-bottom: 2rem;
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    color: #30303d;
    margin-bottom: 0.7rem;
}

.hero-text {
    font-size: 1.1rem;
    line-height: 1.8;
    color: #5e5e6d;
}

/* RECHNER */
.calc-card {
    margin-bottom: 2rem;
}

.calc-title {
    font-size: 1.7rem;
    font-weight: 800;
    color: #30303d;
    margin-bottom: 0.4rem;
}

.calc-subtitle {
    color: #70707d;
    margin-bottom: 1.5rem;
    font-style: italic;
}

/* METRIC */
[data-testid="stMetric"] {

    background: #fff8ea;

    border: 1px solid #f3dfb6;

    padding: 1rem;

    border-radius: 22px;

    box-shadow:
        0 5px 15px rgba(0,0,0,0.04);
}

/* INFO BOXEN */
.stAlert {

    background: #fff8eb !important;

    border: 1px solid #f0dfbd !important;

    border-radius: 22px !important;

    padding: 1.2rem !important;

    font-size: 1.3rem !important;

    font-weight: 700 !important;

    color: #30303d !important;

    box-shadow:
        0 5px 15px rgba(0,0,0,0.04);
}

/* INPUTS */
.stNumberInput > div {

    border-radius: 14px;
}

/* BUTTONS */
.stButton > button {

    width: 100%;

    border-radius: 18px;

    border: none;

    background:
        linear-gradient(
            135deg,
            #ffe6a7,
            #ffd36b
        );

    color: #30303d;

    font-weight: 700;

    padding: 0.7rem;

    box-shadow:
        0 8px 20px rgba(0,0,0,0.08);

    transition: all 0.2s ease;
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 14px 28px rgba(0,0,0,0.12);
}

/* INFO TEXT */
.small-info {

    margin-top: 2rem;

    color: #666674;

    line-height: 1.7;

    font-size: 1rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO
# ---------------------------------------------------

st.markdown("""
<div class="hero-box">

<div class="hero-title">
🧪 Konzentrationen & Teilchenzahl
</div>

<div class="hero-text">
Berechne wichtige Konzentrationen und Teilchenzahlen in der Chemie.

Von Molarität über Molalität bis zur Teilchenzahl —
alle wichtigen Berechnungen übersichtlich an einem Ort.
</div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# STORAGE
# ---------------------------------------------------

def save_to_local(filename, data):

    try:
        json_data = json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_data)

        return True

    except Exception as e:
        st.error(f"Fehler beim lokalen Speichern: {str(e)}")
        return False


if "logbuch_daten" not in st.session_state:
    st.session_state.logbuch_daten = {
        "molmasse": [],
        "molformel": [],
        "konzentration": []
    }


AVOGADRO = 6.022e23


def speichere_ins_logbuch(eintrag):

    st.session_state.logbuch_daten["konzentration"].append(eintrag)

    save_to_local(
        "konzentration_logbuch.json",
        st.session_state.logbuch_daten["konzentration"]
    )

    if save_to_switchdrive(
        "konzentration_logbuch.json",
        st.session_state.logbuch_daten["konzentration"]
    ):
        st.success("✅ Auf SwitchDrive und lokal gespeichert!")
    else:
        st.info("💾 Lokal gespeichert")


# ---------------------------------------------------
# MOLARITÄT
# ---------------------------------------------------

st.markdown("""
<div class="calc-card">
<div class="calc-title">
1️⃣ Molarität: c [mol/L] = n / V
</div>

<div class="calc-subtitle">
Berechne die Konzentration einer Lösung
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.write("### Eingaben")

    n_molar = st.number_input(
        "Stoffmenge n [mol]",
        min_value=0.0,
        value=0.0,
        step=0.01
    )

    V_molar = st.number_input(
        "Volumen V [L]",
        min_value=0.0,
        value=0.0,
        step=0.01
    )

with col2:

    st.write("### Ergebnis")

    if V_molar > 0:

        c_molar = n_molar / V_molar

        st.metric(
            "Molarität c",
            f"{c_molar:.4f} mol/L"
        )

    else:
        st.info("Bitte gib ein Volumen > 0 ein")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# MOLALITÄT
# ---------------------------------------------------

st.markdown("""
<div class="calc-card">
<div class="calc-title">
2️⃣ Molalität: β [mol/g] = n / m
</div>

<div class="calc-subtitle">
Berechne die Molalität einer Lösung
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.write("### Eingaben")

    n_molal = st.number_input(
        "Stoffmenge n [mol]",
        min_value=0.0,
        value=0.0,
        step=0.01
    )

    m_molal = st.number_input(
        "Masse m [g]",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

with col2:

    st.write("### Ergebnis")

    if m_molal > 0:

        beta_molal = n_molal / m_molal

        st.metric(
            "Molalität β",
            f"{beta_molal:.4f} mol/g"
        )

    else:
        st.info("Bitte gib eine Masse > 0 ein")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# TEILCHENZAHL
# ---------------------------------------------------

st.markdown("""
<div class="calc-card">
<div class="calc-title">
3️⃣ Teilchenzahl: N = n × 6.022 × 10²³
</div>

<div class="calc-subtitle">
Berechne die Anzahl der Teilchen
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.write("### Eingaben")

    n_teilchen = st.number_input(
        "Stoffmenge n [mol]",
        min_value=0.0,
        value=0.0,
        step=0.01
    )

with col2:

    st.write("### Ergebnis")

    N = n_teilchen * AVOGADRO

    if N >= 1e9:
        st.metric(
            "Teilchenzahl N",
            f"{N:.3e}"
        )

    else:
        st.metric(
            "Teilchenzahl N",
            f"{N:,.0f}"
        )

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# INFO
# ---------------------------------------------------

st.markdown("""
<div class="small-info">

🔬 <b>Avogadro-Konstante:</b> 6.022 × 10²³ Teilchen/mol

<br><br>

💧 <b>Dichte von Wasser:</b> ungefähr 1 g/mL

<br><br>

📌 <b>Tipp:</b> Molalität ist temperaturunabhängig.

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOGBUCH
# ---------------------------------------------------

st.write("## 💾 Ergebnisse speichern")

col1, col2, col3 = st.columns(3)

with col1:

    if st.button(
        "Molarität speichern",
        use_container_width=True
    ):

        if V_molar > 0:

            eintrag = {
                "Datum & Uhrzeit":
                datetime.now().strftime("%d.%m.%Y %H:%M:%S"),

                "Rechnung":
                "Molarität",

                "Eingaben":
                f"n={n_molar} mol, V={V_molar} L",

                "Ergebnis":
                f"c={n_molar / V_molar:.4f} mol/L"
            }

            speichere_ins_logbuch(eintrag)

with col2:

    if st.button(
        "Molalität speichern",
        use_container_width=True
    ):

        if m_molal > 0:

            eintrag = {
                "Datum & Uhrzeit":
                datetime.now().strftime("%d.%m.%Y %H:%M:%S"),

                "Rechnung":
                "Molalität",

                "Eingaben":
                f"n={n_molal} mol, m={m_molal} g",

                "Ergebnis":
                f"β={n_molal / m_molal:.4f} mol/g"
            }

            speichere_ins_logbuch(eintrag)

with col3:

    if st.button(
        "Teilchenzahl speichern",
        use_container_width=True
    ):

        eintrag = {
            "Datum & Uhrzeit":
            datetime.now().strftime("%d.%m.%Y %H:%M:%S"),

            "Rechnung":
            "Teilchenzahl",

            "Eingaben":
            f"n={n_teilchen} mol",

            "Ergebnis":
            f"N={n_teilchen * AVOGADRO:.3e}"
        }

        speichere_ins_logbuch(eintrag)