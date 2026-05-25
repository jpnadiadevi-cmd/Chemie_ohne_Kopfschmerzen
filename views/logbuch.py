from datetime import datetime
from zoneinfo import ZoneInfo

import streamlit as st

from functions.logbuch_manager import (
    hole_dataframe,
    sammle_exportdaten,
    erstelle_export_dataframe,
    leere_kategorie
)


st.set_page_config(
    page_title="Logbuch",
    page_icon="📓",
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

    .info-list, .logbook-card, .export-card, .hint-card {
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

    .stDownloadButton > button {
        border-radius: 16px;
        border: 1px solid #efe2c4;
        background: rgba(255,255,255,0.92);
        color: #30303d;
        font-weight: 700;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        transition: all 0.22s ease;
    }

    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        background: #fff1c9;
        border-color: #f0c96a;
        box-shadow: 0 12px 25px rgba(0,0,0,0.10);
    }
    </style>
    """, unsafe_allow_html=True)


def initialisiere_session_state():

    if "logbuch_daten" not in st.session_state:

        st.session_state.logbuch_daten = {
            "molmasse": [],
            "molformel": [],
            "konzentration": []
        }


def zeige_kopfbereich():

    st.markdown("""
    <div class="hero-card">
        <h1>📓 Logbuch</h1>
        <p>
            Sammle deine gespeicherten Ergebnisse aus Molformel, Molmasse und
            Konzentrationsberechnungen an einem übersichtlichen Ort.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-list">
        <b>Dieses Logbuch hilft dir bei:</b>
        <ul>
            <li><b>Übersicht</b> – alle gespeicherten Rechnungen geordnet nach Kategorie</li>
            <li><b>Kontrolle</b> – Eingaben, Ergebnisse und Zeitpunkte nachvollziehen</li>
            <li><b>Export</b> – Daten als CSV-Datei herunterladen</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


def zeige_logbuch_tabelle(kategorie, leertext):

    daten = st.session_state.logbuch_daten[kategorie]

    col1, col2 = st.columns([4, 1])

    with col1:

        if daten:

            dataframe = hole_dataframe(daten)

            st.dataframe(
                dataframe,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(leertext)

    with col2:

        if st.button(
            "🗑️ Löschen",
            key=f"delete_{kategorie}",
            use_container_width=True
        ):

            st.session_state.logbuch_daten = (
                leere_kategorie(
                    st.session_state.logbuch_daten,
                    kategorie
                )
            )

            st.rerun()


def zeige_logbuch_tabs():

    st.markdown(
        '<div class="logbook-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card-title">📋 Deine gespeicherten Ergebnisse</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card-subtitle">Wähle eine Kategorie aus, um die passenden Einträge anzuzeigen</div>',
        unsafe_allow_html=True
    )

    tab1, tab2, tab3 = st.tabs([
        "🧬 Die Molformel",
        "⚛️ Molmasse mit PSE",
        "🧪 Konzentration & Teilchen"
    ])

    with tab1:

        st.subheader("Die Molformel – Logbuch")

        zeige_logbuch_tabelle(
            "molformel",
            "📝 Noch keine Einträge. Führe Berechnungen in 'Die Molformel' durch."
        )

    with tab2:

        st.subheader("Molmasse mit PSE – Logbuch")

        zeige_logbuch_tabelle(
            "molmasse",
            "📝 Noch keine Einträge. Führe Berechnungen in 'Molmasse berechnen' durch."
        )

    with tab3:

        st.subheader("Konzentration & Teilchen – Logbuch")

        zeige_logbuch_tabelle(
            "konzentration",
            "📝 Noch keine Einträge. Führe Berechnungen in 'Konzentration & Teilchen' durch."
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


def zeige_exportbereich():

    st.markdown(
        '<div class="export-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card-title">📥 Daten exportieren</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card-subtitle">Lade alle gespeicherten Logbuchdaten als CSV-Datei herunter</div>',
        unsafe_allow_html=True
    )

    exportdaten = sammle_exportdaten(
        st.session_state.logbuch_daten
    )

    if exportdaten:

        df_export = erstelle_export_dataframe(
            exportdaten
        )

        csv = df_export.to_csv(index=False)

        st.download_button(
            label="📊 CSV herunterladen",
            data=csv,
            file_name=f"logbuch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )

    else:

        st.warning(
            "⚠️ Keine Daten zum Exportieren vorhanden."
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


def zeige_hinweise():

    st.markdown("""
    <div class="hint-card">
        <b>💡 Hinweise zum Logbuch:</b>
        <ul>
            <li>Alle Einträge werden mit Datum und Uhrzeit gespeichert.</li>
            <li>Jede Kategorie besitzt eine eigene Tabelle.</li>
            <li>Mit dem Export-Button kannst du deine Ergebnisse als CSV herunterladen.</li>
            <li>Einzelne Kategorien können über den Löschen-Button geleert werden.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


initialisiere_session_state()

lade_css()

zeige_kopfbereich()

zeige_logbuch_tabs()

zeige_exportbereich()

zeige_hinweise()