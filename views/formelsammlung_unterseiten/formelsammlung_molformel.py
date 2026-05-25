import streamlit as st
from datetime import datetime

from utils.storage import save_to_switchdrive
from functions.molformel_rechner import berechne_molformel


# --- Titel ---

st.title("🧬 Die Molformel")

st.markdown("---")

st.header("Berechne Stoffmenge, Masse oder Molare Masse")

st.latex(
    r"n = \frac{m}{M} \quad | \quad m = M \cdot n \quad | \quad M = \frac{m}{n}"
)

st.markdown("---")


# --- Session State ---

if "logbuch_daten" not in st.session_state:
    st.session_state.logbuch_daten = {
        "molmasse": [],
        "molformel": [],
        "konzentration": []
    }


# --- Eingaben ---

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


# --- Berechnung ---

st.subheader("📊 Ergebnis")

result = berechne_molformel(n_input, m_input, M_input)

result_text = None
result_key = None
result_value = None

if result["status"] == "ok":

    result_key = result["result_key"]
    result_value = result["result_value"]

    result_text = f"{result_key} = {result_value:.4f}"

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


st.markdown("---")


# --- Speichern ---

if result_text is not None:

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "💾 Ergebnis ins Logbuch speichern",
            use_container_width=True,
            key="save_molformel"
        ):

            eintrag = {
                "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "Rechnung": "Molformel (n, m, M)",

                "Eingaben": (
                    f"n={n_input if n_input > 0 else '—'}, "
                    f"m={m_input if m_input > 0 else '—'}, "
                    f"M={M_input if M_input > 0 else '—'}"
                ),

                "Ergebnis": f"{result_key}={result_value:.4f}"
            }

            st.session_state.logbuch_daten["molformel"].append(eintrag)

            st.session_state.data_manager.save_user_data(
                st.session_state.logbuch_daten,
                "logbuch_daten.json"
            )

            if save_to_switchdrive(
                "logbuch_daten.json",
                st.session_state.logbuch_daten
            ):

                st.success(
                    f"✅ {result_key}={result_value:.4f} im Logbuch und auf SwitchDrive gespeichert!"
                )

            else:

                st.info(
                    f"💾 {result_key}={result_value:.4f} im Logbuch gespeichert, aber SwitchDrive konnte nicht aktualisiert werden."
                )