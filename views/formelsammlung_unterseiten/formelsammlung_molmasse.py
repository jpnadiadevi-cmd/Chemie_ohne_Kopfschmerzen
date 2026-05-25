import streamlit as st
from datetime import datetime

from data.pse_data import elemente, farben_kategorien
from utils.storage import save_to_switchdrive
from functions.molmasse_rechner import (
    berechne_gesamtmasse,
    erstelle_element_counts,
    erstelle_formel_string,
    erstelle_formel_html
)


st.title("⚛️ Interaktives Periodensystem - Molmasse berechnen")
st.markdown("---")

st.write("""
🧪 **Interaktives PSE – molare Masse clever berechnen**

Willkommen beim interaktiven Periodensystem!
Hier werden Elemente nicht nur angeklickt, sondern direkt zur molaren Masse zusammengestellt 😉

Keine Sorge:
Dieses PSE ist übersichtlicher als ein Labortisch vor der Prüfung
und deutlich hilfreicher als reines Auswendiglernen 😄

Und denk daran:
👉 Hinter jeder Formel steckt mehr als nur Chemie – manchmal auch ein wenig Geduld.

Bleib neugierig – und rechne Element für Element ⚛️
""")


if "selected_elements_list" not in st.session_state:
    st.session_state.selected_elements_list = []

if "logbuch_daten" not in st.session_state:
    st.session_state.logbuch_daten = {
        "molmasse": [],
        "molformel": [],
        "konzentration": []
    }


elemente_sortiert = sorted(elemente, key=lambda x: x["ordnungszahl"])

st.subheader("Periodensystem mit allen 118 Elementen")

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


st.markdown("---")
st.write("**Klicke auf ein Element, um es zur Berechnung hinzuzufügen:**")


element_grid = {}

for el in elemente_sortiert:
    periode = el["periode"]
    gruppe = el["gruppe"]

    if periode not in element_grid:
        element_grid[periode] = {}

    element_grid[periode][gruppe] = el


for periode in range(1, 8):
    cols = st.columns(18)

    if periode in element_grid:
        for gruppe, el in element_grid[periode].items():
            col_idx = gruppe - 1

            with cols[col_idx]:
                farbe = farben_kategorien.get(el["kategorie"], "#FFFFFF")

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
                        {el["symbol"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    "➕",
                    key=f"btn_molmasse_{el['ordnungszahl']}",
                    help=f"{el['name']} hinzufügen"
                ):
                    st.session_state.selected_elements_list.append(el)
                    st.rerun()


st.markdown("---")
st.subheader("📊 Ausgewählte Elemente und Molmasse")


if st.session_state.selected_elements_list:
    st.write("**Ausgewählte Elemente:**")

    total_mass = berechne_gesamtmasse(
        st.session_state.selected_elements_list
    )

    col1, col2, col3, col4 = st.columns([1, 2, 2, 1])

    with col1:
        st.write("**Nr.**")
    with col2:
        st.write("**Element**")
    with col3:
        st.write("**Molmasse**")
    with col4:
        st.write("**Löschen**")

    for idx, el in enumerate(st.session_state.selected_elements_list):
        col1, col2, col3, col4 = st.columns([1, 2, 2, 1])

        with col1:
            st.write(idx + 1)

        with col2:
            st.write(el["name"])

        with col3:
            st.write(f"{el['symbol']} - {el['atommasse']} g/mol")

        with col4:
            if st.button(
                "🗑️",
                key=f"delete_molmasse_{idx}",
                help="Löschen"
            ):
                st.session_state.selected_elements_list.pop(idx)
                st.rerun()

    st.markdown("---")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        st.metric("Gesamte Molmasse", f"{total_mass:.3f} g/mol")

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

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "💾 Ergebnis ins Logbuch speichern",
            use_container_width=True,
            key="save_molmasse"
        ):
            formula_str = erstelle_formel_string(element_counts)

            eintrag = {
                "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "Rechnung": "Molmasse mit PSE",
                "Eingaben": (
                    f"Elemente: {', '.join([el['symbol'] for el in st.session_state.selected_elements_list])}"
                ),
                "Formel": formula_str,
                "Ergebnis": f"{total_mass:.3f} g/mol"
            }

            st.session_state.logbuch_daten["molmasse"].append(eintrag)

            st.session_state.data_manager.save_user_data(
                st.session_state.logbuch_daten,
                "logbuch_daten.json"
            )

            if save_to_switchdrive(
                "logbuch_daten.json",
                st.session_state.logbuch_daten
            ):
                st.success("✅ Eintrag ins Logbuch und auf SwitchDrive gespeichert!")

            else:
                st.info(
                    "💾 Eintrag im Logbuch gespeichert, aber SwitchDrive konnte nicht aktualisiert werden."
                )

    with col2:
        if st.button("🗑️ Alle Elemente löschen", use_container_width=True):
            st.session_state.selected_elements_list = []
            st.rerun()

else:
    st.info("👆 Klicke auf die ➕ Buttons, um Elemente zur Berechnung hinzuzufügen!")