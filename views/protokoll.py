import streamlit as st
import json
from pathlib import Path
from datetime import datetime

st.set_page_config(layout="wide")

st.title("📝 Protokoll")

st.write("""
🧾 **Protokoll – sauber dokumentiert**

Willkommen im Protokoll.
Hier wird nicht experimentiert, sondern exakt festgehalten, was passiert ist.

Ein gutes Protokoll ist wie eine gute Reaktion:
klar, nachvollziehbar und ohne unnötige Nebenprodukte 😉
""")

st.markdown("---")

DATA_FILE = Path("protokolle.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

data = load_data()

# Neues Experiment erstellen

with col2:
    if st.button("➕ Neues Experiment", use_container_width=True):
        st.session_state.show_new_experiment = True

if "show_new_experiment" not in st.session_state:
    st.session_state.show_new_experiment = False

if st.session_state.show_new_experiment:
    with st.form("new_experiment_form"):
        new_folder = st.text_input("Name des Experiments", placeholder="z.B. Kjedahl")
        submitted = st.form_submit_button("Erstellen")
        
        if submitted:
            if new_folder.strip() == "":
                st.warning("Bitte Namen eingeben.")
            elif new_folder in data:
                st.warning("Ordner existiert bereits.")
            else:
                data[new_folder] = {
                    "erstellt": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                    "titel": new_folder,
                    "ziel": "",
                    "material": "",
                    "durchführung": "",
                    "beobachtung": "",
                    "auswertung": "",
                    "fazit": ""
                }
                save_data(data)
                st.session_state.show_new_experiment = False
                st.success("✅ Experiment erstellt!")
                st.rerun()

st.markdown("---")

# Meine Experimente anzeigen
st.subheader("📂 Meine Experimente")

if not data:
    st.info("Noch keine Experimente vorhanden.")
else:
    folders = list(data.keys())
    cols = st.columns(4)
    
    for index, folder in enumerate(folders):
        with cols[index % 4]:
            if st.button(
                f"💗\n\n{folder}\n\n{data[folder].get('erstellt', '')}",
                use_container_width=True,
                key=f"folder_{folder}"
            ):
                st.session_state.selected_protocol = folder
                st.rerun()

st.markdown("---")

# Gewähltes Protokoll öffnen und bearbeiten
if "selected_protocol" in st.session_state and st.session_state.selected_protocol in data:
    selected = st.session_state.selected_protocol
    protocol = data[selected]
    
    # Header mit Schließen-Button
    col1, col2 = st.columns([5, 1])
    
    with col1:
        st.header(f"🧪 {selected}")
    
    with col2:
        if st.button("❌ Schließen", use_container_width=True):
            del st.session_state.selected_protocol
            st.rerun()
    
    st.markdown("---")
    
    # Eingabefelder
    protocol["titel"] = st.text_input(
        "📌 Titel",
        protocol.get("titel", ""),
        placeholder="Gib einen Titel ein"
    )
    
    protocol["ziel"] = st.text_area(
        "🔬 Ziel des Experiments",
        protocol.get("ziel", ""),
        height=100,
        placeholder="Was ist das Ziel dieses Experiments?"
    )
    
    protocol["material"] = st.text_area(
        "⚗️ Material & Chemikalien",
        protocol.get("material", ""),
        height=100,
        placeholder="Welche Materialien und Chemikalien werden benötigt?"
    )
    
    protocol["durchführung"] = st.text_area(
        "👩‍🔬 Durchführung",
        protocol.get("durchführung", ""),
        height=120,
        placeholder="Wie wurde das Experiment durchgeführt?"
    )
    
    protocol["beobachtung"] = st.text_area(
        "👁️ Beobachtung",
        protocol.get("beobachtung", ""),
        height=120,
        placeholder="Was hast du beobachtet?"
    )
    
    protocol["auswertung"] = st.text_area(
        "📊 Auswertung",
        protocol.get("auswertung", ""),
        height=120,
        placeholder="Wie interpretierst du die Ergebnisse?"
    )
    
    protocol["fazit"] = st.text_area(
        "💭 Fazit",
        protocol.get("fazit", ""),
        height=100,
        placeholder="Welche Schlussfolgerungen ziehst du?"
    )
    
    st.markdown("---")
    
    # Buttons zum Speichern und Löschen
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💾 Speichern", use_container_width=True, key="save_protocol"):
            data[selected] = protocol
            save_data(data)
            st.success("✅ Protokoll gespeichert!")
    
    with col2:
        if st.button("🗑️ Löschen", use_container_width=True, key="delete_protocol"):
            del data[selected]
            save_data(data)
            del st.session_state.selected_protocol
            st.warning("⚠️ Experiment gelöscht.")
            st.rerun()
    
    with col3:
        if st.button("↩️ Zurück zu Übersicht", use_container_width=True, key="back_protocol"):
            del st.session_state.selected_protocol
            st.rerun()