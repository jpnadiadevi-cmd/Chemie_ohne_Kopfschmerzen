import streamlit as st
from datetime import datetime
import json

from utils.storage import save_to_switchdrive
from functions.konzentration_rechner import (
    berechne_molaritaet,
    berechne_molalitaet,
    berechne_teilchenzahl
)


AVOGADRO = 6.022e23
LOGBOOK_PATH = "data/konzentration_logbuch.json"


st.set_page_config(
    page_title="Konzentrationen & Teilchenzahl",
    page_icon="🧪",
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
    background: rgba(255,255,255,0.85);
    border-radius: 26px;
    padding: 1.8rem 2rem;
    box-shadow: 0 12px 35px rgba(0,0,0,0.07);
    border: 1px solid rgba(255,255,255,0.5);
    margin-bottom: 2rem;
}

.hero-card h1 {
    margin: 0;
    font-size: 2.5rem;
    color: #30303d;
}

.hero-card p {
    margin-top: 0.9rem;
    font-size: 1.08rem;
    line-height: 1.7;
    color: #5b5b68;
}

.info-list {
    background: rgba(255,255,255,0.72);
    border-radius: 22px;
    padding: 1.3rem 1.6rem;
    box-shadow: 0 8px 25px rgba(0,0,0,0.06);
    margin-bottom: 2rem;
}

.calc-card {
    background: rgba(255,255,255,0.88);
    border-radius: 24px;
    padding: 1.5rem 1.7rem;
    box-shadow: 0 10px 28px rgba(0,0,0,0.07);
    border: 1px solid rgba(255,255,255,0.55);
    margin-bottom: 1.8rem;
}

.calc-title {
    font-size: 1.55rem;
    font-weight: 800;
    color: #30303d;
    margin-bottom: 0.3rem;
}

.calc-subtitle {
    color: #666674;
    font-style: italic;
    margin-bottom: 1.2rem;
}

.stMetric {
    background: #fff8eb;
    border-radius: 18px;
    padding: 1rem;
    border: 1px solid #f0dfbd;
}

.stButton > button {
    border-radius: 16px;
    border: 1px solid #efe2c4;
    background: rgba(255,255,255,0.92);
    color: #30303d;
    font-weight: 700;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    transition: all 0.22s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    background: #fff1c9;
    border-color: #f0c96a;
    box-shadow: 0 12px 25px rgba(0,0,0,0.10);
}

.constants-card {
    background: rgba(255,255,255,0.82);
    border-radius: 22px;
    padding: 1.4rem 1.6rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    border-left: 6px solid #f0c96a;
}
</style>
""", unsafe_allow_html=True)


def save_to_local(filename, data):
    try:
        json_data = json.dumps(data, indent=4, ensure_ascii=False)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_data)

        return True

    except Exception as e:
        st.error(f"Fehler beim lokalen Speichern: {str(e)}")
        return False


def speichere_ins_logbuch(eintrag):
    st.session_state.logbuch_daten["konzentration"].append(eintrag)

    save_to_local(
        LOGBOOK_PATH,
        st.session_state.logbuch_daten["konzentration"]
    )

    if save_to_switchdrive(
        LOGBOOK_PATH,
        st.session_state.logbuch_daten["konzentration"]
    ):
        st.success("✅ Auf SwitchDrive und lokal gespeichert!")
    else:
        st.info("💾 Lokal gespeichert")


if "logbuch_daten" not in st.session_state:
    st.session_state.logbuch_daten = {
        "molmasse": [],
        "molformel": [],
        "konzentration": []
    }


st.markdown("""
<div class="hero-card">
    <h1>🧪 Konzentrationen & Teilchenzahl</h1>
    <p>
        Berechne wichtige Konzentrationen und Teilchenzahlen in der Chemie.
        Gib einfach deine Werte ein und erhalte sofort ein übersichtliches Ergebnis.
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="info-list">
    <b>Diese Seite hilft dir bei:</b>
    <ul>
        <li><b>Molarität</b> – Konzentration in mol/L</li>
        <li><b>Molalität</b> – Konzentration in mol/g</li>
        <li><b>Teilchenzahl</b> – Anzahl der Atome oder Moleküle</li>
    </ul>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="calc-card">', unsafe_allow_html=True)
st.markdown(
    '<div class="calc-title">1️⃣ Molarität: c [mol/L] = n / V</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="calc-subtitle">Berechne die Konzentration einer Lösung</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])

with col1:
    st.write("**Eingaben:**")

    n_molar = st.number_input(
        "Stoffmenge n [mol]",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="n_molar"
    )

    V_molar = st.number_input(
        "Volumen V [L]",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="V_molar"
    )

with col2:
    st.write("**Ergebnis:**")

    result_molar = berechne_molaritaet(n_molar, V_molar)

    if result_molar["status"] == "ok":
        c_molar = result_molar["value"]

        st.metric(
            result_molar["label"],
            f"{c_molar:.4f} mol/L"
        )

    else:
        c_molar = None
        st.info(result_molar["message"])

st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="calc-card">', unsafe_allow_html=True)
st.markdown(
    '<div class="calc-title">2️⃣ Molalität: β [mol/g] = n / m</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="calc-subtitle">Berechne die Molalität einer Lösung</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])

with col1:
    st.write("**Eingaben:**")

    n_molal = st.number_input(
        "Stoffmenge n [mol]",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="n_molal"
    )

    m_molal = st.number_input(
        "Masse m [g]",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="m_molal"
    )

with col2:
    st.write("**Ergebnis:**")

    result_molal = berechne_molalitaet(n_molal, m_molal)

    if result_molal["status"] == "ok":
        beta_molal = result_molal["value"]

        st.metric(
            result_molal["label"],
            f"{beta_molal:.4f} mol/g"
        )

    else:
        beta_molal = None
        st.info(result_molal["message"])

st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="calc-card">', unsafe_allow_html=True)
st.markdown(
    '<div class="calc-title">3️⃣ Teilchenzahl: N = n × 6.022 × 10²³</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="calc-subtitle">Berechne die Anzahl der Atome oder Moleküle</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])

with col1:
    st.write("**Eingaben:**")

    n_teilchen = st.number_input(
        "Stoffmenge n [mol]",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="n_teilchen"
    )

with col2:
    st.write("**Ergebnis:**")

    result_teilchen = berechne_teilchenzahl(
        n_teilchen,
        AVOGADRO
    )

    N = result_teilchen["value"]

    if N >= 1e9:
        st.metric(
            result_teilchen["label"],
            f"{N:.3e}"
        )
    else:
        st.metric(
            result_teilchen["label"],
            f"{N:,.0f}"
        )

st.markdown('</div>', unsafe_allow_html=True)


st.markdown("""
<div class="constants-card">
    <b>Wichtige Konstanten:</b>
    <ul>
        <li>🔬 <b>Avogadro-Konstante:</b> 6.022 × 10²³ Teilchen/mol</li>
        <li>💧 <b>Dichte von Wasser:</b> ca. 1 g/mL = 1 kg/L</li>
    </ul>
    <b>Tipp:</b> Molalität ist temperaturunabhängig, Molarität dagegen nicht.
</div>
""", unsafe_allow_html=True)


st.markdown("### 💾 Ergebnisse speichern")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button(
        "💾 Molarität ins Logbuch",
        key="save_molar",
        use_container_width=True
    ):
        if c_molar is not None:
            eintrag = {
                "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "Rechnung": "Molarität",
                "Eingaben": f"n={n_molar} mol, V={V_molar} L",
                "Ergebnis": f"c={c_molar:.4f} mol/L"
            }

            speichere_ins_logbuch(eintrag)

        else:
            st.warning("⚠️ Bitte erst Werte eingeben!")


with col2:
    if st.button(
        "💾 Molalität ins Logbuch",
        key="save_molal",
        use_container_width=True
    ):
        if beta_molal is not None:
            eintrag = {
                "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "Rechnung": "Molalität",
                "Eingaben": f"n={n_molal} mol, m={m_molal} g",
                "Ergebnis": f"β={beta_molal:.4f} mol/g"
            }

            speichere_ins_logbuch(eintrag)

        else:
            st.warning("⚠️ Bitte erst Werte eingeben!")


with col3:
    if st.button(
        "💾 Teilchenzahl ins Logbuch",
        key="save_teilchen",
        use_container_width=True
    ):
        eintrag = {
            "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "Rechnung": "Teilchenzahl",
            "Eingaben": f"n={n_teilchen} mol",
            "Ergebnis": f"N={N:.3e}"
        }

        speichere_ins_logbuch(eintrag)