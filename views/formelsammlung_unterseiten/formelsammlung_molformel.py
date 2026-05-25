from datetime import datetime

import streamlit as st

from utils.storage import save_to_switchdrive
from functions.molformel_rechner import berechne_molformel


LOGBOOK_FILE = "logbuch_daten.json"


st.set_page_config(
    page_title="Die Molformel",
    page_icon="🧬",
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

    .formula-card {
        background: #fff8eb;
        border-radius: 18px;
        padding: 1.2rem;
        border: 1px solid #f0dfbd;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 1.5rem;
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
    </style>
    """, unsafe_allow_html=True)


def initialisiere_session_state():
    if "logbuch_daten" not in st.session_state:
        st.session_state.logbuch_daten = {
            "molmasse": [],
            "molformel": [],
            "konzentration": []
        }


def zeige_kopfbereich():
    st.markdown("""
    <div class="hero-card">
        <h1>🧬 Die Molformel</h1>
        <p>
            Berechne die Stoffmenge, Masse oder molare Masse.
            Gib zwei Werte ein und der fehlende dritte Wert wird automatisch berechnet.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-list">
        <b>Diese Seite hilft dir bei:</b>
        <ul>
            <li><b>Stoffmenge n</b> – Einheit mol</li>
            <li><b>Masse m</b> – Einheit g</li>
            <li><b>Molare Masse M</b> – Einheit g/mol</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


def zeige_formelkarte():
    st.markdown("""
    <div class="formula-card">
        <b>Formeln:</b><br><br>
        n = m / M &nbsp;&nbsp; | &nbsp;&nbsp;
        m = M · n &nbsp;&nbsp; | &nbsp;&nbsp;
        M = m / n
    </div>
    """, unsafe_allow_html=True)


def formatiere_eingabe(wert):
    return wert if wert > 0 else "—"


def erstelle_logbuch_eintrag(n_input, m_input, M_input, result_key, result_value):
    return {
        "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "Rechnung": "Molformel (n, m, M)",
        "Eingaben": (
            f"n={formatiere_eingabe(n_input)}, "
            f"m={formatiere_eingabe(m_input)}, "
            f"M={formatiere_eingabe(M_input)}"
        ),
        "Ergebnis": f"{result_key}={result_value:.4f}"
    }


def speichere_ins_logbuch(eintrag, result_key, result_value):
    st.session_state.logbuch_daten["molformel"].append(eintrag)

    st.session_state.data_manager.save_user_data(
        st.session_state.logbuch_daten,
        LOGBOOK_FILE
    )

    if save_to_switchdrive(LOGBOOK_FILE, st.session_state.logbuch_daten):
        st.success(
            f"✅ {result_key}={result_value:.4f} im Logbuch gespeichert!"
        )
    else:
        st.info(
            f"💾 {result_key}={result_value:.4f} im Logbuch gespeichert, "
            "aber SwitchDrive konnte nicht aktualisiert werden."
        )


def zeige_molformel_rechner():
    st.markdown('<div class="calc-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="calc-title">🧮 Molformel berechnen</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="calc-subtitle">Berechne n, m oder M mithilfe von zwei bekannten Werten</div>',
        unsafe_allow_html=True
    )

    zeige_formelkarte()

    col1, col2, col3 = st.columns(3)

    with col1:
        n_input = st.number_input(
            "Stoffmenge n [mol]",
            value=0.0,
            format="%.4f",
            key="n_input"
        )

    with col2:
        m_input = st.number_input(
            "Masse m [g]",
            value=0.0,
            format="%.4f",
            key="m_input"
        )

    with col3:
        M_input = st.number_input(
            "Molare Masse M [g/mol]",
            value=0.0,
            format="%.4f",
            key="M_input"
        )

    st.markdown("---")
    st.write("**Ergebnis:**")

    result = berechne_molformel(n_input, m_input, M_input)

    result_key = None
    result_value = None

    if result["status"] == "ok":
        result_key = result["result_key"]
        result_value = result["result_value"]

        st.metric(
            result["label"],
            f"{result_value:.4f}"
        )

    elif result["status"] == "warning":
        st.warning(result["message"])

    elif result["status"] == "info":
        st.info(result["message"])

    else:
        st.error(result["message"])

    st.markdown('</div>', unsafe_allow_html=True)

    return n_input, m_input, M_input, result_key, result_value


def zeige_speicherbereich(n_input, m_input, M_input, result_key, result_value):
    if result_key is None or result_value is None:
        return

    st.markdown("### 💾 Ergebnis speichern")

    col1, col2 = st.columns([1, 2])

    with col1:
        if st.button(
            "💾 Ergebnis ins Logbuch speichern",
            use_container_width=True,
            key="save_molformel"
        ):
            eintrag = erstelle_logbuch_eintrag(
                n_input,
                m_input,
                M_input,
                result_key,
                result_value
            )

            speichere_ins_logbuch(
                eintrag,
                result_key,
                result_value
            )


initialisiere_session_state()
lade_css()
zeige_kopfbereich()

n_input, m_input, M_input, result_key, result_value = zeige_molformel_rechner()

zeige_speicherbereich(
    n_input,
    m_input,
    M_input,
    result_key,
    result_value
)