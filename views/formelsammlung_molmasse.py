import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("⚛️ Interaktives Periodensystem - Alle 118 Elemente")

st.write("Klicke auf ein Element, um detaillierte Informationen zu sehen!")

# Vollständige Periodensystem-Daten mit allen 118 Elementen
elemente = [
    # Periode 1
    {"symbol": "H", "name": "Wasserstoff", "ordnungszahl": 1, "gruppe": 1, "periode": 1, "atommasse": 1.008, "kategorie": "Nichtmetalle", "elektronegativität": 2.20},
    {"symbol": "He", "name": "Helium", "ordnungszahl": 2, "gruppe": 18, "periode": 1, "atommasse": 4.003, "kategorie": "Edelgase", "elektronegativität": None},
    
    # ...existing code...
    # (alle 118 Elemente wie vorher)
    {"symbol": "Og", "name": "Oganesson", "ordnungszahl": 118, "gruppe": 18, "periode": 7, "atommasse": 294, "kategorie": "Edelgase", "elektronegativität": None},
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

# Initialisiere Session State für die Liste der ausgewählten Elemente
if "selected_elements_list" not in st.session_state:
    st.session_state.selected_elements_list = []

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
st.write("*Klicke auf ein Element, um es zur Berechnung hinzuzufügen:*")

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
                
                if st.button(f"➕", key=f"btn_{el['ordnungszahl']}", help=f"Klicke für {el['name']}"):
                    st.session_state.selected_elements_list.append(el)
                    st.rerun()

st.markdown("---")

# Zeige ausgewählte Elemente und deren Summe
st.subheader("📊 Ausgewählte Elemente und Molmasse")

if st.session_state.selected_elements_list:
    # Tabelle mit ausgewählten Elementen
    st.write("**Ausgewählte Elemente:**")
    
    table_data = []
    total_mass = 0
    
    for idx, el in enumerate(st.session_state.selected_elements_list):
        table_data.append({
            "Nr.": idx + 1,
            "Element": el["name"],
            "Symbol": el["symbol"],
            "Molmasse (g/mol)": el["atommasse"],
            "Löschen": f"🗑️ {idx}"
        })
        total_mass += el["atommasse"]
    
    # Anzeige als Tabelle
    df = pd.DataFrame(table_data)
    
    # Tabelle mit Lösch-Buttons
    col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
    
    for idx, row in enumerate(table_data):
        with col1:
            st.write(f"**{row['Nr.']}**")
        with col2:
            st.write(row["Element"])
        with col3:
            st.write(f"{row['Symbol']} - {row['Molmasse (g/mol)']} g/mol")
        with col4:
            if st.button("🗑️", key=f"delete_{idx}", help=f"Löschen"):
                st.session_state.selected_elements_list.pop(idx)
                st.rerun()
    
    # Summe anzeigen
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        st.metric("Gesamte Molmasse", f"{total_mass:.3f} g/mol")
    
    st.markdown("---")
    
    # Verlauf der Formel anzeigen
    st.subheader("🔬 Molekülformel")
    
    # Zähle die Atome
    element_counts = {}
    for el in st.session_state.selected_elements_list:
        symbol = el["symbol"]
        element_counts[symbol] = element_counts.get(symbol, 0) + 1
    
    # Erstelle die Formel-Anzeige
    formula_html = ""
    for symbol, count in element_counts.items():
        if count == 1:
            formula_html += f"<span style='font-size: 24px; font-weight: bold;'>{symbol}</span>"
        else:
            formula_html += f"<span style='font-size: 24px; font-weight: bold;'>{symbol}<sub style='font-size: 18px;'>{count}</sub></span>"
    
    st.markdown(f"<div style='padding: 20px; background-color: #f0f0f0; border-radius: 5px;'>{formula_html}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Button zum Löschen aller Elemente
    if st.button("🗑️ Alle Elemente löschen", use_container_width=True):
        st.session_state.selected_elements_list = []
        st.rerun()
else:
    st.info("👆 Klicke auf die ➕ Buttons, um Elemente zur Berechnung hinzuzufügen!")