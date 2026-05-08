import streamlit as st

st.title("📝 Protokoll")

st.write("""
🧾 **Protokoll – sauber dokumentiert**

Willkommen im Protokoll.
Hier wird nicht experimentiert, sondern exakt festgehalten, was passiert ist.

🔬 **Ziel:**
Was wurde untersucht?

⚗️ **Durchführung:**
Wie wurde gearbeitet?

📊 **Beobachtung:**
Was ist passiert?

🧠 **Auswertung:**
Was bedeutet das Ergebnis?

👉 Ein gutes Protokoll ist wie eine gute Reaktion:
klar, nachvollziehbar und ohne unnötige Nebenprodukte 😉

Bleib präzise – Chemie verzeiht keine Ungenauigkeit.
""")

import streamlit as st
import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("protokolle.json")


def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


st.title("📝 Protokoll")

st.write("Dokumentiere deine Experimente.")

st.divider()

data = load_data()

# Neues Experiment erstellen
with st.expander("➕ Neues Experiment erstellen"):

    new_folder = st.text_input(
        "Name des Experiments",
        placeholder="z.B. Kjedahl"
    )

    if st.button("Ordner erstellen", use_container_width=True):

        if new_folder.strip() == "":
            st.warning("Bitte Namen eingeben.")

        elif new_folder in data:
            st.warning("Ordner existiert bereits.")

        else:
            data[new_folder] = {
                "erstellt": datetime.now().strftime("%d.%m.%Y"),
                "titel": new_folder,
                "ziel": "",
                "material": "",
                "durchführung": "",
                "beobachtung": "",
                "auswertung": "",
                "fazit": ""
            }

            save_data(data)

            st.success("Ordner erstellt.")

            st.rerun()


st.subheader("📂 Meine Experimente")

if not data:
    st.info("Noch keine Experimente vorhanden.")

else:

    folders = list(data.keys())

    cols = st.columns(3)

    for index, folder in enumerate(folders):

        with cols[index % 3]:

            st.markdown(
    f"""
    <div style="
        border:1px solid #f5b8cf;
        border-radius:18px;
        padding:20px;
        background-color:#ffeef5;
        text-align:center;
        min-height:150px;
        box-shadow:0px 2px 8px rgba(0,0,0,0.05);
    ">

        🩷

        <div style="
            color:#c85a87;
            font-size:28px;
            font-weight:bold;
            margin-top:15px;
        ">
            {folder}
        </div>

        <div style="
            font-size:13px;
            color:#8a8a8a;
            margin-top:10px;
        ">
            Erstellt am:
            {data[folder].get("erstellt", "")}
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

# Gewähltes Protokoll öffnen
if "selected_protocol" in st.session_state:

    selected = st.session_state["selected_protocol"]

    protocol = data[selected]

    st.divider()

    st.header(f"🧪 {selected}")

    protocol["titel"] = st.text_input(
        "Titel",
        protocol.get("titel", "")
    )

    protocol["ziel"] = st.text_area(
        "Ziel des Experiments",
        protocol.get("ziel", ""),
        height=100
    )

    protocol["material"] = st.text_area(
        "Material / Chemikalien",
        protocol.get("material", ""),
        height=120
    )

    protocol["durchführung"] = st.text_area(
        "Durchführung",
        protocol.get("durchführung", ""),
        height=160
    )

    protocol["beobachtung"] = st.text_area(
        "Beobachtung",
        protocol.get("beobachtung", ""),
        height=160
    )

    protocol["auswertung"] = st.text_area(
        "Auswertung",
        protocol.get("auswertung", ""),
        height=160
    )

    protocol["fazit"] = st.text_area(
        "Fazit",
        protocol.get("fazit", ""),
        height=120
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("💾 Speichern", use_container_width=True):

            data[selected] = protocol

            save_data(data)

            st.success("Protokoll gespeichert.")

    with col2:
        if st.button("🗑️ Löschen", use_container_width=True):

            del data[selected]

            save_data(data)

            del st.session_state["selected_protocol"]

            st.warning("Ordner gelöscht.")

            st.rerun()

    with col3:
        if st.button("❌ Schliessen", use_container_width=True):

            del st.session_state["selected_protocol"]

            st.rerun()