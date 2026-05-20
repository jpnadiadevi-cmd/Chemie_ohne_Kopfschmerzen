import streamlit as st
from datetime import datetime

from utils.storage import save_to_switchdrive

st.title("📝 Protokoll")
st.markdown("---")
st.write("""
🧾 **Protokoll – sauber dokumentiert**

Willkommen im Protokoll.
Hier wird nicht experimentiert, sondern exakt festgehalten, was passiert ist.

Ein gutes Protokoll ist wie eine gute Reaktion:
klar, nachvollziehbar und ohne unnötige Nebenprodukte 😉
""")


# Protokolle laden
if "protokolle" not in st.session_state:
    st.session_state.protokolle = st.session_state.data_manager.load_user_data(
        "protokolle.json",
        initial_value={}
    )

data = st.session_state.protokolle


def save_protocols():
    # Lokal / Data Manager speichern
    st.session_state.data_manager.save_user_data(
        st.session_state.protokolle,
        "protokolle.json"
    )

    # Zusätzlich auf SwitchDrive speichern
    save_to_switchdrive(
        "protokolle.json",
        st.session_state.protokolle
    )


# Neues Experiment erstellen
col1, col2 = st.columns([4, 1])

with col2:
    if st.button("➕ Neues Experiment", use_container_width=True):
        st.session_state.show_new_experiment = True

if "show_new_experiment" not in st.session_state:
    st.session_state.show_new_experiment = False

if st.session_state.show_new_experiment:
    with st.form("new_experiment_form"):

        new_folder = st.text_input(
            "Name des Experiments",
            placeholder="z.B. Kjeldahl"
        )

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

                st.session_state.protokolle = data

                save_protocols()

                st.session_state.show_new_experiment = False

                st.success("✅ Experiment erstellt und auf SwitchDrive gespeichert!")

                st.rerun()


# Experimente anzeigen
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


# Protokoll öffnen
if (
    "selected_protocol" in st.session_state
    and st.session_state.selected_protocol in data
):

    selected = st.session_state.selected_protocol
    protocol = data[selected]

    col1, col2 = st.columns([5, 1])

    with col1:
        st.header(f"🧪 {selected}")

    with col2:
        if st.button("❌ Schließen", use_container_width=True):
            del st.session_state.selected_protocol
            st.rerun()

    st.markdown("---")

    protocol["titel"] = st.text_input(
        "📌 Titel",
        protocol.get("titel", ""),
        placeholder="Gib einen Titel ein"
    )

    protocol["ziel"] = st.text_area(
        "🔬 Ziel des Experiments",
        protocol.get("ziel", ""),
        height=100
    )

    protocol["material"] = st.text_area(
        "⚗️ Material & Chemikalien",
        protocol.get("material", ""),
        height=100
    )

    protocol["durchführung"] = st.text_area(
        "👩‍🔬 Durchführung",
        protocol.get("durchführung", ""),
        height=120
    )

    protocol["beobachtung"] = st.text_area(
        "👁️ Beobachtung",
        protocol.get("beobachtung", ""),
        height=120
    )

    protocol["auswertung"] = st.text_area(
        "📊 Auswertung",
        protocol.get("auswertung", ""),
        height=120
    )

    protocol["fazit"] = st.text_area(
        "💭 Fazit",
        protocol.get("fazit", ""),
        height=100
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "💾 Speichern",
            use_container_width=True,
            key="save_protocol"
        ):

            data[selected] = protocol
            st.session_state.protokolle = data

            save_protocols()

            st.success("✅ Protokoll auf SwitchDrive gespeichert!")

    with col2:

        if st.button(
            "🗑️ Löschen",
            use_container_width=True,
            key="delete_protocol"
        ):

            del data[selected]

            st.session_state.protokolle = data

            save_protocols()

            del st.session_state.selected_protocol

            st.warning("⚠️ Experiment gelöscht und auf SwitchDrive aktualisiert.")

            st.rerun()

    with col3:

        if st.button(
            "↩️ Zurück zu Übersicht",
            use_container_width=True,
            key="back_protocol"
        ):

            del st.session_state.selected_protocol
            st.rerun()