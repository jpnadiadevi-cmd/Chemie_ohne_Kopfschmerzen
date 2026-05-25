from datetime import datetime

import streamlit as st

from utils.storage import save_to_switchdrive
from functions.molformel_rechner import berechne_molformel


LOGBOOK_FILE = "logbuch_daten.json"


st.title("🧬 Die Molformel")
st.markdown("---")

st.header("Berechne Stoffmenge, Masse oder Molare Masse")

st.latex(
    r"n = \frac{m}{M} \quad | \quad m = M \cdot n \quad | \quad M = \frac{m}{n}"
)

st.markdown("---")


def initialisiere_session_state():
    if "logbuch_daten" not in st.session_state:
        st.session_state.logbuch_daten = {
            "molmasse": [],
            "molformel": [],
            "konzentration": []
        }


def zeige_eingaben():
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

    return n_input, m_input, M_input


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
            f"✅ {result_key}={result_value:.4f} im Logbuch und auf SwitchDrive gespeichert!"
        )
    else:
        st.info(
            f"💾 {result_key}={result_value:.4f} im Logbuch gespeichert, "
            "aber SwitchDrive konnte nicht aktualisiert werden."
        )


def zeige_ergebnis(n_input, m_input, M_input):
    st.subheader("📊 Ergebnis")

    result = berechne_molformel(n_input, m_input, M_input)

    if result["status"] == "ok":
        result_key = result["result_key"]
        result_value = result["result_value"]

        st.metric(
            result["label"],
            f"{result_value:.4f}"
        )

        return result_key, result_value

    if result["status"] == "warning":
        st.warning(result["message"])

    elif result["status"] == "info":
        st.info(result["message"])

    else:
        st.error(result["message"])

    return None, None


def zeige_speicherbutton(n_input, m_input, M_input, result_key, result_value):
    if result_key is None or result_value is None:
        return

    col1, _ = st.columns(2)

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

n_input, m_input, M_input = zeige_eingaben()

st.markdown("---")

result_key, result_value = zeige_ergebnis(
    n_input,
    m_input,
    M_input
)

st.markdown("---")

zeige_speicherbutton(
    n_input,
    m_input,
    M_input,
    result_key,
    result_value
)