import streamlit as st

st.title("📓 Logbuch")
st.markdown("---")
st.write("""
🧪 **Logbuch – Chemie ohne Kopfschmerzen**

Willkommen im Logbuch!
Hier werden nicht nur Reaktionen festgehalten, sondern auch ausgelöst 😉

Dieses Logbuch ist stabiler als ein Edelgas
und zum Glück weniger explosiv als Natrium im Wasser 💥

Und denk daran:
👉 Wenn etwas schiefgeht, ist es einfach ein Experiment.

Bleib positiv – ausser du bist ein Elektron ⚡
""")         

import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os

st.set_page_config(layout="wide")


st.markdown("---")

# Datenspeicherung im Session State
if "logbuch_daten" not in st.session_state:
    st.session_state.logbuch_daten = {
        "molmasse": [],
        "molformel": [],
        "konzentration": []
    }

# Tabs für verschiedene Rechnung-Kategorien
tab1, tab2, tab3 = st.tabs(["🧬 Die Molformel", "⚛️ Molmasse mit PSE", "🧪 Konzentration & Teilchen"])

# ===== TAB 1: DIE MOLFORMEL =====
with tab1:
    st.subheader("Die Molformel – Logbuch")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.session_state.logbuch_daten["molformel"]:
            df_molformel = pd.DataFrame(st.session_state.logbuch_daten["molformel"])
            st.dataframe(df_molformel, use_container_width=True, hide_index=True)
        else:
            st.info("📝 Noch keine Einträge. Führe Berechnungen in 'Die Molformel' durch.")
    
    with col2:
        if st.button("🗑️ Löschen", key="delete_molformel"):
            st.session_state.logbuch_daten["molformel"] = []
            st.rerun()

# ===== TAB 2: MOLMASSE MIT PSE =====
with tab2:
    st.subheader("Molmasse mit PSE – Logbuch")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.session_state.logbuch_daten["molmasse"]:
            df_molmasse = pd.DataFrame(st.session_state.logbuch_daten["molmasse"])
            st.dataframe(df_molmasse, use_container_width=True, hide_index=True)
        else:
            st.info("📝 Noch keine Einträge. Führe Berechnungen in 'Molmasse berechnen' durch.")
    
    with col2:
        if st.button("🗑️ Löschen", key="delete_molmasse"):
            st.session_state.logbuch_daten["molmasse"] = []
            st.rerun()

# ===== TAB 3: KONZENTRATION & TEILCHEN =====
with tab3:
    st.subheader("Konzentration & Teilchen – Logbuch")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.session_state.logbuch_daten["konzentration"]:
            df_konzentration = pd.DataFrame(st.session_state.logbuch_daten["konzentration"])
            st.dataframe(df_konzentration, use_container_width=True, hide_index=True)
        else:
            st.info("📝 Noch keine Einträge. Führe Berechnungen in 'Konzentration & Teilchen' durch.")
    
    with col2:
        if st.button("🗑️ Löschen", key="delete_konzentration"):
            st.session_state.logbuch_daten["konzentration"] = []
            st.rerun()

st.markdown("---")

# Export-Funktionalität
st.subheader("📥 Daten exportieren")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Alle Daten als CSV exportieren"):
        combined_data = []
        for category, data in st.session_state.logbuch_daten.items():
            for entry in data:
                entry["Kategorie"] = category
                combined_data.append(entry)
        
        if combined_data:
            df_export = pd.DataFrame(combined_data)
            csv = df_export.to_csv(index=False)
            st.download_button(
                label="CSV herunterladen",
                data=csv,
                file_name=f"logbuch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        else:
            st.warning("⚠️ Keine Daten zum Exportieren vorhanden.")

st.markdown("---")

st.info("""
💡 **Hinweise zum Logbuch:**
- Alle Einträge werden mit Datum und Uhrzeit gespeichert
- Die Daten bleiben erhalten, solange die App läuft
- Mit dem Export-Button kannst du deine Ergebnisse als CSV herunterladen
- Jede Kategorie hat ihre eigene Tabelle
""")