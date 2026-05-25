from datetime import datetime
from zoneinfo import ZoneInfo

import streamlit as st

from utils.storage import save_to_switchdrive

from functions.protokoll_manager import (
    erstelle_neues_protokoll,
    experiment_name_ungueltig,
    experiment_existiert,
    loesche_protokoll
)


st.set_page_config(
    page_title="Protokoll",
    page_icon="📝",
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

    .info-list, .protocol-card, .experiment-card {
        background: rgba(255,255,255,0.88);
        border-radius: 24px;
        padding: 1.5rem 1.7rem;
        box-shadow: 0 10px 28px rgba(0,0,0,0.07);
        border: 1px solid rgba(255,255,255,0.55);
        margin-bottom: 1.8rem;
    }

    .card-title {
        font-size: 1.55rem;
        font-weight: 800;
        color: #30303d;
        margin-bottom: 0.3rem;
    }

    .card-subtitle {
        color: #666674;
        font-style: italic;
        margin-bottom: 1.2rem;
    }

    .folder-card {
        background: #fff8eb;
        border-radius: 18px;
        padding: 1rem;
        border: 1px solid #f0dfbd;
        text-align: center;
        min-height: 120px;
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

    textarea {
        border-radius: 14px !important;
    }
    </style>
    """, unsafe_allow_html=True)


def initialisiere_session_state():

    if "protokolle" not in st.session_state:

        st.session_state.protokolle = (
            st.session_state.data_manager.load_user_data(
                "protokolle.json",
                initial_value={}
            )
        )

    if "show_new_experiment" not in st.session_state:
        st.session_state.show_new_experiment = False


def save_protocols():

    st.session_state.data_manager.save_user_data(
        st.session_state.protokolle,
        "protokolle.json"
    )

    save_to_switchdrive(
        "protokolle.json",
        st.session_state.protokolle
    )


def zeige_kopfbereich():

    st.markdown("""
    <div class="hero-card">
        <h1>📝 Protokoll</h1>
        <p>
            Dokumentiere deine chemischen Experimente übersichtlich und strukturiert.
            Halte Ziel, Durchführung, Beobachtungen und Auswertung sauber fest.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-list">
        <b>Diese Seite hilft dir bei:</b>
        <ul>
            <li><b>Experimenten</b> – eigene Versuche anlegen und verwalten</li>
            <li><b>Dokumentation</b> – Beobachtungen und Ergebnisse speichern</li>
            <li><b>Organisation</b> – alle Protokolle an einem Ort sammeln</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


def zeige_neues_experiment_button():

    col1, col2 = st.columns([4, 1])

    with col2:

        if st.button(
            "➕ Neues Experiment",
            use_container_width=True
        ):
            st.session_state.show_new_experiment = True


def zeige_experiment_formular():

    if not st.session_state.show_new_experiment:
        return

    st.markdown('<div class="protocol-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">🩷 Neues Experiment erstellen</div>',
        unsafe_allow_html=True
    )

    with st.form("new_experiment_form"):

        new_folder = st.text_input(
            "Name des Experiments",
            placeholder="z.B. Kjeldahl"
        )

        submitted = st.form_submit_button("Erstellen")

        if submitted:

            daten = st.session_state.protokolle

            if experiment_name_ungueltig(new_folder):

                st.warning("⚠️ Bitte Namen eingeben.")

            elif experiment_existiert(new_folder, daten):

                st.warning("⚠️ Experiment existiert bereits.")

            else:

                daten[new_folder] = (
                    erstelle_neues_protokoll(new_folder)
                )

                st.session_state.protokolle = daten

                save_protocols()

                st.session_state.show_new_experiment = False

                st.success(
                    "✅ Experiment erstellt und auf SwitchDrive gespeichert!"
                )

                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


def zeige_experimente():

    daten = st.session_state.protokolle

    st.markdown('<div class="protocol-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">📂 Meine Experimente</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card-subtitle">Wähle ein Experiment aus, um das Protokoll zu bearbeiten</div>',
        unsafe_allow_html=True
    )

    if not daten:

        st.info("📝 Noch keine Experimente vorhanden.")

        st.markdown('</div>', unsafe_allow_html=True)

        return

    folders = list(daten.keys())

    cols = st.columns(4)

    for index, folder in enumerate(folders):

        with cols[index % 4]:

            if st.button(
                f"🧪\n\n{folder}\n\n{daten[folder].get('erstellt', '')}",
                use_container_width=True,
                key=f"folder_{folder}"
            ):

                st.session_state.selected_protocol = folder

                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


def zeige_protokoll():

    daten = st.session_state.protokolle

    if (
        "selected_protocol" not in st.session_state
        or st.session_state.selected_protocol not in daten
    ):
        return

    selected = st.session_state.selected_protocol

    protocol = daten[selected]

    st.markdown('<div class="experiment-card">', unsafe_allow_html=True)

    col1, col2 = st.columns([5, 1])

    with col1:

        st.markdown(
            f'<div class="card-title">🩷 {selected}</div>',
            unsafe_allow_html=True
        )

    with col2:

        if st.button(
            "❌ Schließen",
            use_container_width=True
        ):

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

            daten[selected] = protocol

            st.session_state.protokolle = daten

            save_protocols()

            st.success(
                "✅ Protokoll gespeichert!"
            )

    with col2:

        if st.button(
            "🗑️ Löschen",
            use_container_width=True,
            key="delete_protocol"
        ):

            daten = loesche_protokoll(
                daten,
                selected
            )

            st.session_state.protokolle = daten

            save_protocols()

            del st.session_state.selected_protocol

            st.warning(
                "⚠️ Experiment gelöscht und SwitchDrive aktualisiert."
            )

            st.rerun()

    with col3:

        if st.button(
            "↩️ Zurück zur Übersicht",
            use_container_width=True,
            key="back_protocol"
        ):

            del st.session_state.selected_protocol

            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


lade_css()

initialisiere_session_state()

zeige_kopfbereich()

zeige_neues_experiment_button()

zeige_experiment_formular()

zeige_experimente()

zeige_protokoll()