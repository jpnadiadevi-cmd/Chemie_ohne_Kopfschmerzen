import json
from datetime import datetime
from zoneinfo import ZoneInfo

import streamlit as st

from utils.storage import save_to_switchdrive
from functions.konzentration_rechner import (
    berechne_molaritaet,
    berechne_molalitaet,
    berechne_teilchenzahl
)

AVOGADRO = 6.022e23

LOGBUCH_DATEI = "logbuch_daten.json"

st.set_page_config(
    page_title="Konzentrationen & Teilchenzahl",
    page_icon="🧪",
    layout="wide"
)


def lade_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #fff8eb 0%, #fffdf8 45%, #ffffff 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero-card, .info-list, .calc-card, .constants-card {
        background: rgba(255,255,255,0.85);
        border-radius: 24px;
        padding: 1.5rem 1.7rem;
        box-shadow: 0 10px 28px rgba(0,0,0,0.07);
        margin-bottom: 1.8rem;
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
        border-left: 6px solid #f0c96a;
    }
    </style>
    """, unsafe_allow_html=True)


def save_to_local(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True

    except Exception as error:
        st.error(f"Fehler beim lokalen Speichern: {error}")
        return False


def speichere_ins_logbuch(eintrag):

    # Konzentrationseintrag anhängen
    st.session_state.logbuch_daten["konzentration"].append(eintrag)

    # GANZES Logbuch speichern
    save_to_local(
        LOGBUCH_DATEI,
        st.session_state.logbuch_daten
    )

    # GANZES Logbuch auf SwitchDrive speichern
    if save_to_switchdrive(
        LOGBUCH_DATEI,
        st.session_state.logbuch_daten
    ):
        st.success("✅ Im Logbuch gespeichert!")
    else:
        st.info("💾 Lokal gespeichert")


def erstelle_logbuch_eintrag(rechnung, eingaben, ergebnis):
    return {
        "Datum & Uhrzeit": datetime.now(ZoneInfo("Europe/Zurich")).strftime("%d.%m.%Y %H:%M:%S"),
        "Rechnung": rechnung,
        "Eingaben": eingaben,
        "Ergebnis": ergebnis
    }


def zeige_kopfbereich():
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


def starte_rechnerkarte(titel, untertitel):
    st.markdown('<div class="calc-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="calc-title">{titel}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="calc-subtitle">{untertitel}</div>', unsafe_allow_html=True)


def beende_rechnerkarte():
    st.markdown('</div>', unsafe_allow_html=True)


def zeige_molaritaet():

    starte_rechnerkarte(
        "1️⃣ Molarität: c [mol/L] = n / V",
        "Berechne die Konzentration einer Lösung"
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

        v_molar = st.number_input(
            "Volumen V [L]",
            min_value=0.0,
            value=0.0,
            step=0.01,
            key="V_molar"
        )

    with col2:

        st.write("**Ergebnis:**")

        result = berechne_molaritaet(n_molar, v_molar)

        if result["status"] == "ok":
            c_molar = result["value"]
            st.metric(result["label"], f"{c_molar:.4f} mol/L")
        else:
            c_molar = None
            st.info(result["message"])

    beende_rechnerkarte()

    return n_molar, v_molar, c_molar


def zeige_molalitaet():

    starte_rechnerkarte(
        "2️⃣ Molalität: β [mol/g] = n / m",
        "Berechne die Molalität einer Lösung"
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

        result = berechne_molalitaet(n_molal, m_molal)

        if result["status"] == "ok":
            beta_molal = result["value"]
            st.metric(result["label"], f"{beta_molal:.4f} mol/g")
        else:
            beta_molal = None
            st.info(result["message"])

    beende_rechnerkarte()

    return n_molal, m_molal, beta_molal


def zeige_teilchenzahl():

    starte_rechnerkarte(
        "3️⃣ Teilchenzahl: N = n × 6.022 × 10²³",
        "Berechne die Anzahl der Atome oder Moleküle"
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

        result = berechne_teilchenzahl(n_teilchen, AVOGADRO)

        teilchenzahl = result["value"]

        if teilchenzahl >= 1e9:
            st.metric(result["label"], f"{teilchenzahl:.3e}")
        else:
            st.metric(result["label"], f"{teilchenzahl:,.0f}")

    beende_rechnerkarte()

    return n_teilchen, teilchenzahl


def zeige_konstanten():

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


def zeige_speicherbuttons(
    n_molar,
    v_molar,
    c_molar,
    n_molal,
    m_molal,
    beta_molal,
    n_teilchen,
    teilchenzahl
):

    st.markdown("### 💾 Ergebnisse speichern")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("💾 Molarität ins Logbuch", use_container_width=True):

            if c_molar is None:
                st.warning("⚠️ Bitte erst Werte eingeben!")
                return

            eintrag = erstelle_logbuch_eintrag(
                "Molarität",
                f"n={n_molar} mol, V={v_molar} L",
                f"c={c_molar:.4f} mol/L"
            )

            speichere_ins_logbuch(eintrag)

    with col2:

        if st.button("💾 Molalität ins Logbuch", use_container_width=True):

            if beta_molal is None:
                st.warning("⚠️ Bitte erst Werte eingeben!")
                return

            eintrag = erstelle_logbuch_eintrag(
                "Molalität",
                f"n={n_molal} mol, m={m_molal} g",
                f"β={beta_molal:.4f} mol/g"
            )

            speichere_ins_logbuch(eintrag)

    with col3:

        if st.button("💾 Teilchenzahl ins Logbuch", use_container_width=True):

            eintrag = erstelle_logbuch_eintrag(
                "Teilchenzahl",
                f"n={n_teilchen} mol",
                f"N={teilchenzahl:.3e}"
            )

            speichere_ins_logbuch(eintrag)


if "logbuch_daten" not in st.session_state:

    st.session_state.logbuch_daten = {
        "molmasse": [],
        "molformel": [],
        "konzentration": []
    }


lade_css()

zeige_kopfbereich()

n_molar, v_molar, c_molar = zeige_molaritaet()

n_molal, m_molal, beta_molal = zeige_molalitaet()

n_teilchen, teilchenzahl = zeige_teilchenzahl()

zeige_konstanten()

zeige_speicherbuttons(
    n_molar,
    v_molar,
    c_molar,
    n_molal,
    m_molal,
    beta_molal,
    n_teilchen,
    teilchenzahl
)