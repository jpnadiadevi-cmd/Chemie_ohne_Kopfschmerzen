import streamlit as st

st.set_page_config(layout="wide")

st.title("⚛️ Interaktives Periodensystem - Alle 118 Elemente")

st.write("Klicke auf ein Element, um detaillierte Informationen zu sehen!")

# Vollständige Periodensystem-Daten mit allen 118 Elementen
elemente = [
    # Periode 1
    {"symbol": "H", "name": "Wasserstoff", "ordnungszahl": 1, "gruppe": 1, "periode": 1, "atommasse": 1.008, "kategorie": "Nichtmetalle", "elektronegativität": 2.20},
    {"symbol": "He", "name": "Helium", "ordnungszahl": 2, "gruppe": 18, "periode": 1, "atommasse": 4.003, "kategorie": "Edelgase", "elektronegativität": None},
    
    # Periode 2
    {"symbol": "Li", "name": "Lithium", "ordnungszahl": 3, "gruppe": 1, "periode": 2, "atommasse": 6.941, "kategorie": "Alkalimetalle", "elektronegativität": 0.98},
    # ... (rest of elements - copy from the working version)
]

# Farbschema für Kategorien
farben_kategorien = {
    "Alkalimetalle": "#FF9999",
    "Erdalkalimetalle": "#FFCC99",
    "Lanthanoide": "#FFBFFF",
    "Actinoide": "#FF99CC",
    "Übergangsmetalle": "#CCCCFF",
    "Halbmetalle": "#CCFFCC",
    "Nichtmetalle": "#FFFFCC",
    "Halogene": "#FFCCFF",
    "Edelgase": "#CCFFFF",
}

# Sortiere nach Ordnungszahl
elemente_sortiert = sorted(elemente, key=lambda x: x["ordnungszahl"])

# Periodensystem-Gitter (18 Spalten)
st.subheader("Periodensystem mit allen 118 Elementen")

# Kategorien-Legende
st.write("*Kategorien-Legende:*")
legend_cols = st.columns(len(farben_kategorien))
for idx, (kategorie, farbe) in enumerate(farben_kategorien.items()):
    with legend_cols[idx]:
        st.markdown(f"<div style='background-color: {farbe}; padding: 10px; border-radius: 5px; text-align: center; font-size: 12px;'>{kategorie}</div>", unsafe_allow_html=True)

st.markdown("---")

# Periodensystem als Grid anzeigen
st.write("*Klicke auf ein Element:*")

# Erstelle ein Dictionary für schnelle Positionierung
element_grid = {}
for el in elemente_sortiert:
    periode = el["periode"]
    gruppe = el["gruppe"]
    if periode not in element_grid:
        element_grid[periode] = {}
    element_grid[periode][gruppe] = el

# Zeige das Periodensystem
for periode in range(1, 8):
    cols = st.columns(18)
    if periode in element_grid:
        for gruppe, el in element_grid[periode].items():
            col_idx = gruppe - 1
            with cols[col_idx]:
                farbe = farben_kategorien.get(el["kategorie"], "#FFFFFF")
                button_style = f"""
                <button style='
                    width: 100%;
                    padding: 20px 5px;
                    background-color: {farbe};
                    border: 2px solid #333;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold;
                    font-size: 16px;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;
                '>{el["symbol"]}</button>
                """
                st.markdown(button_style, unsafe_allow_html=True)
                
                if st.button(f"🔍", key=f"btn_{el['ordnungszahl']}", help=f"Klicke für {el['name']}"):
                    st.session_state["selected_element"] = el

st.markdown("---")

# Detaillierte Informationen
if "selected_element" in st.session_state:
    el = st.session_state["selected_element"]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"⚛️ {el['name']} ({el['symbol']})")
        
        col_info1, col_info2 = st.columns(2)
        with col_info1:
            st.metric("Ordnungszahl", el["ordnungszahl"])
            st.metric("Atommasse", f"{el['atommasse']} u")
            st.metric("Periode", el["periode"])
        
        with col_info2:
            st.metric("Gruppe", el["gruppe"])
            st.metric("Kategorie", el["kategorie"])
            if el["elektronegativität"]:
                st.metric("Elektronegativität", f"{el['elektronegativität']:.2f}")
            else:
                st.metric("Elektronegativität", "N/A")
    
    with col2:
        farbe = farben_kategorien.get(el["kategorie"], "#FFFFFF")
        st.markdown(f"""
        <div style='
            background-color: {farbe};
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            border: 3px solid #333;
        '>{el['symbol']}</div>
        """, unsafe_allow_html=True)
    
    # Funktion zum Löschen
    if st.button("❌ Element abwählen"):
        del st.session_state["selected_element"]
        st.rerun()
else:
    st.info("👆 Klicke auf ein Element, um detaillierte Informationen zu sehen!")