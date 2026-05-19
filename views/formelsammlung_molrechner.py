import streamlit as st
from datetime import datetime

st.title("🧮 Mol-Rechner")
st.markdown("---")

if "logbuch_daten" not in st.session_state:
    st.session_state.logbuch_daten = {
        "molmasse": [],
        "molformel": [],
        "konzentration": []
    }

# Abschnitt 1: Stoffmenge
st.header("Stoffmenge (n)")
st.latex(r"n = \frac{m}{M}")

col1, col2 = st.columns(2)

with col1:
    m1 = st.number_input("Masse m [g]", key="mol_m1", value=0.0, format="%.4f")
    M1 = st.number_input("Molare Masse M [g/mol]", key="mol_M1", value=0.0, format="%.4f")

with col2:
    n1 = m1 / M1 if M1 != 0 else 0.0
    st.text_input("Stoffmenge n [mol]", value=f"{n1:.4f}", disabled=True)

if st.button("💾 Stoffmenge speichern", key="save_n"):
    if M1 > 0:
        eintrag = {
            "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "Rechnung": "Stoffmenge n = m / M",
            "Eingaben": f"m={m1} g, M={M1} g/mol",
            "Ergebnis": f"n={n1:.4f} mol"
        }

        st.session_state.logbuch_daten["molformel"].append(eintrag)

        st.session_state.data_manager.save_user_data(
            st.session_state.logbuch_daten,
            "logbuch_daten.json"
        )

        st.success("✅ Stoffmenge im Logbuch und auf SwitchDrive gespeichert!")
    else:
        st.warning("⚠️ Bitte eine molare Masse > 0 eingeben.")

st.markdown("---")

# Abschnitt 2: Masse
st.header("Masse (m)")
st.latex(r"m = M \cdot n")

col3, col4 = st.columns(2)

with col3:
    M2 = st.number_input("Molare Masse M [g/mol]", key="mol_M2", value=0.0, format="%.4f")
    n2 = st.number_input("Stoffmenge n [mol]", key="mol_n2", value=0.0, format="%.4f")

with col4:
    m2 = M2 * n2
    st.text_input("Masse m [g]", value=f"{m2:.4f}", disabled=True)

if st.button("💾 Masse speichern", key="save_m"):
    eintrag = {
        "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "Rechnung": "Masse m = M · n",
        "Eingaben": f"M={M2} g/mol, n={n2} mol",
        "Ergebnis": f"m={m2:.4f} g"
    }

    st.session_state.logbuch_daten["molformel"].append(eintrag)

    st.session_state.data_manager.save_user_data(
        st.session_state.logbuch_daten,
        "logbuch_daten.json"
    )

    st.success("✅ Masse im Logbuch und auf SwitchDrive gespeichert!")

st.markdown("---")

# Abschnitt 3: Molare Masse
st.header("Molare Masse (M)")
st.latex(r"M = \frac{m}{n}")

col5, col6 = st.columns(2)

with col5:
    m3 = st.number_input("Masse m [g]", key="mol_m3", value=0.0, format="%.4f")
    n3 = st.number_input("Stoffmenge n [mol]", key="mol_n3", value=0.0, format="%.4f")

with col6:
    M3 = m3 / n3 if n3 != 0 else 0.0
    st.text_input("Molare Masse M [g/mol]", value=f"{M3:.4f}", disabled=True)

if st.button("💾 Molare Masse speichern", key="save_M"):
    if n3 > 0:
        eintrag = {
            "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "Rechnung": "Molare Masse M = m / n",
            "Eingaben": f"m={m3} g, n={n3} mol",
            "Ergebnis": f"M={M3:.4f} g/mol"
        }

        st.session_state.logbuch_daten["molformel"].append(eintrag)

        st.session_state.data_manager.save_user_data(
            st.session_state.logbuch_daten,
            "logbuch_daten.json"
        )

        st.success("✅ Molare Masse im Logbuch und auf SwitchDrive gespeichert!")
    else:
        st.warning("⚠️ Bitte eine Stoffmenge > 0 eingeben.")

st.info("Zwei Werte eingeben, der dritte wird berechnet.")