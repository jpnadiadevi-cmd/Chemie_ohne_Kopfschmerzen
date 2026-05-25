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


st.title("⚛️ Interaktives Periodensystem - Molmasse berechnen")
st.markdown("---")

st.write("""
🧪 **Interaktives PSE – molare Masse clever berechnen**

Willkommen beim interaktiven Periodensystem!
Hier werden Elemente nicht nur angeklickt, sondern direkt zur molaren Masse zusammengestellt 😉

Keine Sorge:
Dieses PSE ist übersichtlicher als ein Labortisch vor der Prüfung
und deutlich hilfreicher als reines Auswendiglernen 😄

👉 Hinter jeder Formel steckt mehr als nur Chemie – manchmal auch ein wenig Geduld.
""")


def initialisiere_session_state():
    if "selected_elements_list" not in st.session_state:
        st.session_state.selected_elements_list = []

    if "logbuch_daten" not in st.session_state:
        st.session_state.logbuch_daten = {
            "molmasse": [],
            "molformel": [],
            "konzentration": []
        }


def zeige_legende():
    st.write("**Kategorien-Legende:**")

    legend_cols = st.columns(len(farben_kategorien))

    for idx, (kategorie, farbe) in enumerate(farben_kategorien.items()):
        with legend_cols[idx]:
            st.markdown(
                f"""
                <div style='
                    background-color: {farbe};
                    padding: 10px;
                    border-radius: 5px;
                    text-align: center;
                    font-size: 12px;
                    border: 1px solid #333;
                '>
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
        <div style='
            width: 100%;
            padding: 12px 4px;
            background-color: {farbe};
            border: 2px solid #333;
            border-radius: 5px;
            text-align: center;
            font-weight: bold;
            font-size: 16px;
            min-height: 45px;
        '>
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
    st.subheader("Periodensystem mit allen 118 Elementen")

    zeige_legende()

    st.markdown("---")
    st.write("**Klicke auf ein Element, um es zur Berechnung hinzuzufügen:**")

    element_grid = erstelle_element_grid()

    for periode in range(1, 8):
        cols = st.columns(18)

        if periode not in element_grid:
            continue

        for gruppe, element in element_grid[periode].items():
            with cols[gruppe - 1]:
                zeige_element(element)


def zeige_ausgewaehlte_elemente():
    if not st.session_state.selected_elements_list:
        st.info(
            "👆 Klicke auf die ➕ Buttons, um Elemente zur Berechnung hinzuzufügen!"
        )
        return

    st.markdown("---")
    st.subheader("📊 Ausgewählte Elemente und Molmasse")

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


def zeige_molekuelformel():
    st.markdown("---")
    st.subheader("🔬 Molekülformel")

    element_counts = erstelle_element_counts(
        st.session_state.selected_elements_list
    )

    formula_html = erstelle_formel_html(element_counts)

    st.markdown(
        f"""
        <div style='
            padding: 20px;
            background-color: #f0f0f0;
            border-radius: 5px;
        '>
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
                [
                    element["symbol"]
                    for element in st.session_state.selected_elements_list
                ]
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

    if save_to_switchdrive(
        LOGBOOK_FILE,
        st.session_state.logbuch_daten
    ):
        st.success(
            "✅ Eintrag ins Logbuch und auf SwitchDrive gespeichert!"
        )

    else:
        st.info(
            "💾 Eintrag im Logbuch gespeichert, "
            "aber SwitchDrive konnte nicht aktualisiert werden."
        )


def zeige_buttons(total_mass):
    st.markdown("---")

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

zeige_periodensystem()

zeige_ausgewaehlte_elemente()