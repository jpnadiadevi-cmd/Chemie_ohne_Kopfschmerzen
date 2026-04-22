import streamlit as st
import pandas as pd

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

# Element hinzufügen
if st.button("Hinzufügen"):
    st.session_state.verbindung.append((element, anzahl))

# Anzeige aktuelle Verbindung
if st.session_state.verbindung:
    st.subheader("Deine Verbindung:")
    gesamtmasse = 0
    daten = []

    for el, an in st.session_state.verbindung:
        einzelmasse = periodensystem[el]
        gesamt = einzelmasse * an
        gesamtmasse += gesamt

        daten.append({
            "Element": el,
            "Anzahl": an,
            "Atommasse (g/mol)": einzelmasse,
            "Beitrag (g/mol)": gesamt
        })

    df = pd.DataFrame(daten)

    st.table(df)
    st.success(f"Gesamt molare Masse: {gesamtmasse:.3f} g/mol")

    # Zurücksetzen + speichern im Verlauf
    if st.button("Zurücksetzen"):
        st.session_state.verlauf.append(gesamtmasse)
        st.session_state.verbindung = []

# Verlauf anzeigen
if st.session_state.verlauf:
    st.subheader("Verlauf (berechnete molare Massen):")
    for i, wert in enumerate(st.session_state.verlauf, 1):
        st.write(f"{i}. {wert:.3f} g/mol")

# Verlauf löschen
if st.button("Verlauf löschen"):
    st.session_state.verlauf = []