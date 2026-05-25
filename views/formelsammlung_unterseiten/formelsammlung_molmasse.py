from datetime import datetime

import streamlit as st

from data.pse_data import elemente, farben_kategorien
from utils.storage import save_to_switchdrive
from functions.molmasse_rechner import (
    berechne_gesamtmasse,
    erstelle_element_counts,
    erstelle_formel_string,
    erstelle_formel_html
)


LOGBOOK_FILE = "logbuch_daten.json"


st.set_page_config(
    page_title="Molmasse berechnen",
    page_icon="⚛️",
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

    .info-list, .calc-card, .result-card {
        background: rgba(255,255,255,0.88);
        border-radius: 24px;
        padding: 1.5rem 1.7rem;
        box-shadow: 0 10px 28px rgba(0,0,0,0.07);
        border: 1px solid rgba(255,255,255,0.55);
        margin-bottom: 1.8rem;
    }

    .calc-title {
        font-size: 1.55rem;
        font-weight: 800;
        color: #30303d;
        margin-bottom: 0.3rem;
    }

    .calc-subtitle {
        color: #666674;
        font-style: italic;
        margin-bottom: 1.2rem;
    }

    .legend-box {
        padding: 10px;
        border-radius: 12px;
        text-align: center;
        font-size: 12px;
        font-weight: 700;
        border: 1px solid rgba(0,0,0,0.25);
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        min-height: 42px;
    }

    .element-box {
        width: 100%;
        padding: 12px 4px;
        border: 2px solid rgba(0,0,0,0.35);
        border-radius: 12px;
        text-align: center;
        font-weight: 800;
        font-size: 16px;
        min-height: 48px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }

    .formula-card {
        background: #fff8eb;
        border-radius: 18px;
        padding: 1.3rem;
        border: 1px solid #f0dfbd;
        text-align: center;
        font-size: 1.35rem;
        font-weight: 700;
        margin-top: 1rem;
    }

    .stMetric {
        background: #fff8eb;
        border-radius: 18px;
        padding: 1rem;
        border: 1px solid #f0dfbd;
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
    </style>
    """, unsafe_allow_html=True)


def initialisiere_session_state():
    if "selected_elements_list" not in st.session_state:
        st.session_state.selected_elements_list = []

    if "logbuch_daten" not in st.session_state:
        st.session_state.logbuch_daten = {
            "molmasse": [],
            "molformel": [],
            "konzentration": []
        }


def zeige_kopfbereich():
    st.markdown("""
    <div class="hero-card">
        <h1>⚛️ Interaktives Periodensystem</h1>
        <p>
            Berechne die molare Masse deiner Verbindung direkt über das Periodensystem.
            Wähle einfach die Elemente aus und deine Molekülformel sowie die Gesamtmasse
            werden automatisch berechnet.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-list">
        <b>Diese Seite hilft dir bei:</b>
        <ul>
            <li><b>Elemente auswählen</b> – direkt aus dem Periodensystem</li>
            <li><b>Molekülformel erstellen</b> – automatisch aus deinen ausgewählten Elementen</li>
            <li><b>Molmasse berechnen</b> – Ergebnis in g/mol</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


def zeige_legende():
    st.write("**Kategorien-Legende:**")

    legend_cols = st.columns(len(farben_kategorien))

    for idx, (kategorie, farbe) in enumerate(farben_kategorien.items()):
        with legend_cols[idx]:
            st.markdown(
                f"""
                <div class="legend-box" style="background-color: {farbe};">
                    {kategorie}
                </div>
                """,
                unsafe_allow_html=True
            )


def erstelle_element_grid():
    grid = {}

    for element in sorted(elemente, key=lambda x: x["ordnungszahl"]):
        periode = element["periode"]
        gruppe = element["gruppe"]

        if periode not in grid:
            grid[periode] = {}

        grid[periode][gruppe] = element

    return grid


def zeige_element(element):
    farbe = farben_kategorien.get(element["kategorie"], "#FFFFFF")

    st.markdown(
        f"""
        <div class="element-box" style="background-color: {farbe};">
            {element["symbol"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "➕",
        key=f"btn_molmasse_{element['ordnungszahl']}",
        help=f"{element['name']} hinzufügen"
    ):
        st.session_state.selected_elements_list.append(element)
        st.rerun()


def zeige_periodensystem():
    st.markdown('<div class="calc-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="calc-title">🧪 Periodensystem mit allen 118 Elementen</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="calc-subtitle">Klicke auf ein Element, um es zur Berechnung hinzuzufügen</div>',
        unsafe_allow_html=True
    )

    zeige_legende()

    st.markdown("---")

    element_grid = erstelle_element_grid()

    for periode in range(1, 8):
        cols = st.columns(18)

        if periode not in element_grid:
            continue

        for gruppe, element in element_grid[periode].items():
            with cols[gruppe - 1]:
                zeige_element(element)

    st.markdown('</div>', unsafe_allow_html=True)


def zeige_ausgewaehlte_elemente():
    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="calc-title">📊 Ausgewählte Elemente und Molmasse</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.selected_elements_list:
        st.info(
            "👆 Klicke auf die ➕ Buttons, um Elemente zur Berechnung hinzuzufügen!"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        return

    total_mass = berechne_gesamtmasse(
        st.session_state.selected_elements_list
    )

    st.write("**Ausgewählte Elemente:**")

    header_cols = st.columns([1, 2, 2, 1])
    headers = ["Nr.", "Element", "Molmasse", "Löschen"]

    for col, header in zip(header_cols, headers):
        with col:
            st.write(f"**{header}**")

    for idx, element in enumerate(st.session_state.selected_elements_list):
        col1, col2, col3, col4 = st.columns([1, 2, 2, 1])

        with col1:
            st.write(idx + 1)

        with col2:
            st.write(element["name"])

        with col3:
            st.write(f"{element['symbol']} - {element['atommasse']} g/mol")

        with col4:
            if st.button(
                "🗑️",
                key=f"delete_molmasse_{idx}",
                help="Löschen"
            ):
                st.session_state.selected_elements_list.pop(idx)
                st.rerun()

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col2:
        st.metric("Gesamte Molmasse", f"{total_mass:.3f} g/mol")

    zeige_molekuelformel()
    zeige_buttons(total_mass)

    st.markdown('</div>', unsafe_allow_html=True)


def zeige_molekuelformel():
    st.markdown("---")

    st.markdown(
        '<div class="calc-title">🔬 Molekülformel</div>',
        unsafe_allow_html=True
    )

    element_counts = erstelle_element_counts(
        st.session_state.selected_elements_list
    )

    formula_html = erstelle_formel_html(element_counts)

    st.markdown(
        f"""
        <div class="formula-card">
            {formula_html}
        </div>
        """,
        unsafe_allow_html=True
    )


def erstelle_logbuch_eintrag(total_mass):
    element_counts = erstelle_element_counts(
        st.session_state.selected_elements_list
    )

    formula_str = erstelle_formel_string(element_counts)

    return {
        "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "Rechnung": "Molmasse mit PSE",
        "Eingaben": (
            "Elemente: "
            + ", ".join(
                element["symbol"]
                for element in st.session_state.selected_elements_list
            )
        ),
        "Formel": formula_str,
        "Ergebnis": f"{total_mass:.3f} g/mol"
    }


def speichere_logbuch(eintrag):
    st.session_state.logbuch_daten["molmasse"].append(eintrag)

    st.session_state.data_manager.save_user_data(
        st.session_state.logbuch_daten,
        LOGBOOK_FILE
    )

    if save_to_switchdrive(LOGBOOK_FILE, st.session_state.logbuch_daten):
        st.success(
            "✅ Eintrag ins Logbuch gespeichert!"
        )
    else:
        st.info(
            "💾 Eintrag im Logbuch gespeichert, "
            "aber SwitchDrive konnte nicht aktualisiert werden."
        )


def zeige_buttons(total_mass):
    st.markdown("---")

    st.markdown("### 💾 Ergebnis speichern")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "💾 Ergebnis ins Logbuch speichern",
            use_container_width=True,
            key="save_molmasse"
        ):
            eintrag = erstelle_logbuch_eintrag(total_mass)
            speichere_logbuch(eintrag)

    with col2:
        if st.button(
            "🗑️ Alle Elemente löschen",
            use_container_width=True
        ):
            st.session_state.selected_elements_list = []
            st.rerun()


initialisiere_session_state()
lade_css()
zeige_kopfbereich()
zeige_periodensystem()
zeige_ausgewaehlte_elemente()