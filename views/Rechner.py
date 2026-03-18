import streamlit as st
from utils.data_manager import DataManager  # --- NEW CODE: import data manager ---i
import pandas as pd  # --- NEW CODE: import pandas for data handling ---
st.title("Molare Masse Rechner (mit Verlauf)")

# Kleine Datenbank
periodensystem = {
    "H": 1.008,
    "C": 12.011,
    "O": 15.999,
    "N": 14.007,
    "Na": 22.990,
    "Cl": 35.45
}

# Session-State initialisieren
if "verbindung" not in st.session_state:
    st.session_state.verbindung = []

if "verlauf" not in st.session_state:
    st.session_state.verlauf = []

st.write("Wähle Elemente und deren Anzahl:")

elemente = list(periodensystem.keys())

# Auswahl
element = st.selectbox("Element", elemente)
anzahl = st.number_input("Anzahl Atome", min_value=1, value=1)

if st.button("Hinzufügen"):
    st.session_state.verbindung.append((element, anzahl))

# Anzeige aktuelle Verbindung
if st.session_state.verbindung:
    st.subheader("Deine Verbindung:")
    gesamtmasse = 0

    for el, an in st.session_state.verbindung:
        masse = periodensystem[el] * an
        gesamtmasse += masse
        st.write(f"{el}{an} → {masse:.3f} g/mol")

    st.success(f"Gesamt molare Masse: {gesamtmasse:.3f} g/mol")

    # Zurücksetzen + speichern
    if st.button("Zurücksetzen"):
        # Speichern im Verlauf
        st.session_state.verlauf.append(gesamtmasse)

        # Verbindung löschen
        st.session_state.verbindung = []
 # --- CODE UPDATE: save data to data manager ---
    data_manager = DataManager()
    data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
    # --- END OF CODE UPDATE ---
# Verlauf anzeigen
if st.session_state.verlauf:
    st.subheader("Verlauf (berechnete molare Massen):")
    for i, wert in enumerate(st.session_state.verlauf, 1):
        st.write(f"{i}. {wert:.3f} g/mol")

if st.button("Verlauf löschen"):
    st.session_state.verlauf = []