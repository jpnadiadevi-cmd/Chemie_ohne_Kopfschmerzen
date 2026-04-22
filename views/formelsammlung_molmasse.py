[11:34, 21.4.2026] Nadia 🐣: import streamlit as st

st.set_page_config(layout="wide")

st.title("⚛️ Interaktives Periodensystem - Alle 118 Elemente")

st.write("Klicke auf ein Element, um detaillierte Informationen zu sehen!")

# Vollständige Periodensystem-Daten mit allen 118 Elementen
elemente = [
    # Periode 1
    {"symbol": "H", "name": "Wasserstoff", "ordnungszahl": 1, "gruppe": 1, "periode": 1, "atommasse": 1.008, "kategorie": "Nichtmetalle", "elektronegativität": 2.20},
    {"symbol": "He", "name": "Helium", "ordnungszahl": 2, "gruppe": 18, "periode": 1, "atommasse": 4.003, "kategorie": "Edelgase", "elektronegativität": None},
    
    # Periode 2
    {"symbol": "Li", "name": "Lithium", "ordnungszahl": 3, "gruppe": 1, "periode": 2, "atommasse": 6.941, "kategorie": …
[11:36, 21.4.2026] Nadja BMLD: import streamlit as st
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# DataManager und Login initialisieren
data_manager = DataManager(
    fs_protocol='webdav',
    fs_root_folder="Chemie_Informatik2"
)

login_manager = LoginManager(data_manager)
login_manager.login_register()

# Seitenkonfiguration
st.set_page_config(
    page_title="Meine App",
    page_icon=":material/home:"
)

# Seiten definieren
pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_rechner = st.Page("views/Rechner.py", title="Rechner", icon=":material/science:")

pg = st.navigation([pg_home, pg_rechner])
pg.run()
[11:39, 21.4.2026] Nadia 🐣: Molare Masse Rechner mit PSE

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
    {"symbol": "Be", "name": "Beryllium", "ordnungszahl": 4, "gruppe": 2, "periode": 2, "atommasse": 9.012, "kategorie": "Erdalkalimetalle", "elektronegativität": 1.57},
    {"symbol": "B", "name": "Bor", "ordnungszahl": 5, "gruppe": 13, "periode": 2, "atommasse": 10.811, "kategorie": "Halbmetalle", "elektronegativität": 2.04},
    {"symbol": "C", "name": "Kohlenstoff", "ordnungszahl": 6, "gruppe": 14, "periode": 2, "atommasse": 12.011, "kategorie": "Nichtmetalle", "elektronegativität": 2.55},
    {"symbol": "N", "name": "Stickstoff", "ordnungszahl": 7, "gruppe": 15, "periode": 2, "atommasse": 14.007, "kategorie": "Nichtmetalle", "elektronegativität": 3.04},
    {"symbol": "O", "name": "Sauerstoff", "ordnungszahl": 8, "gruppe": 16, "periode": 2, "atommasse": 15.999, "kategorie": "Nichtmetalle", "elektronegativität": 3.44},
    {"symbol": "F", "name": "Fluor", "ordnungszahl": 9, "gruppe": 17, "periode": 2, "atommasse": 18.998, "kategorie": "Halogene", "elektronegativität": 3.98},
    {"symbol": "Ne", "name": "Neon", "ordnungszahl": 10, "gruppe": 18, "periode": 2, "atommasse": 20.180, "kategorie": "Edelgase", "elektronegativität": None},
    
    # Periode 3
    {"symbol": "Na", "name": "Natrium", "ordnungszahl": 11, "gruppe": 1, "periode": 3, "atommasse": 22.990, "kategorie": "Alkalimetalle", "elektronegativität": 0.93},
    {"symbol": "Mg", "name": "Magnesium", "ordnungszahl": 12, "gruppe": 2, "periode": 3, "atommasse": 24.305, "kategorie": "Erdalkalimetalle", "elektronegativität": 1.31},
    {"symbol": "Al", "name": "Aluminium", "ordnungszahl": 13, "gruppe": 13, "periode": 3, "atommasse": 26.982, "kategorie": "Übergangsmetalle", "elektronegativität": 1.61},
    {"symbol": "Si", "name": "Silizium", "ordnungszahl": 14, "gruppe": 14, "periode": 3, "atommasse": 28.086, "kategorie": "Halbmetalle", "elektronegativität": 1.90},
    {"symbol": "P", "name": "Phosphor", "ordnungszahl": 15, "gruppe": 15, "periode": 3, "atommasse": 30.974, "kategorie": "Nichtmetalle", "elektronegativität": 2.19},
    {"symbol": "S", "name": "Schwefel", "ordnungszahl": 16, "gruppe": 16, "periode": 3, "atommasse": 32.065, "kategorie": "Nichtmetalle", "elektronegativität": 2.58},
    {"symbol": "Cl", "name": "Chlor", "ordnungszahl": 17, "gruppe": 17, "periode": 3, "atommasse": 35.453, "kategorie": "Halogene", "elektronegativität": 3.16},
    {"symbol": "Ar", "name": "Argon", "ordnungszahl": 18, "gruppe": 18, "periode": 3, "atommasse": 39.948, "kategorie": "Edelgase", "elektronegativität": None},
    
    # Periode 4
    {"symbol": "K", "name": "Kalium", "ordnungszahl": 19, "gruppe": 1, "periode": 4, "atommasse": 39.098, "kategorie": "Alkalimetalle", "elektronegativität": 0.82},
    {"symbol": "Ca", "name": "Calcium", "ordnungszahl": 20, "gruppe": 2, "periode": 4, "atommasse": 40.078, "kategorie": "Erdalkalimetalle", "elektronegativität": 1.00},
    {"symbol": "Sc", "name": "Scandium", "ordnungszahl": 21, "gruppe": 3, "periode": 4, "atommasse": 44.956, "kategorie": "Übergangsmetalle", "elektronegativität": 1.36},
    {"symbol": "Ti", "name": "Titan", "ordnungszahl": 22, "gruppe": 4, "periode": 4, "atommasse": 47.867, "kategorie": "Übergangsmetalle", "elektronegativität": 1.54},
    {"symbol": "V", "name": "Vanadium", "ordnungszahl": 23, "gruppe": 5, "periode": 4, "atommasse": 50.942, "kategorie": "Übergangsmetalle", "elektronegativität": 1.63},
    {"symbol": "Cr", "name": "Chrom", "ordnungszahl": 24, "gruppe": 6, "periode": 4, "atommasse": 51.996, "kategorie": "Übergangsmetalle", "elektronegativität": 1.66},
    {"symbol": "Mn", "name": "Mangan", "ordnungszahl": 25, "gruppe": 7, "periode": 4, "atommasse": 54.938, "kategorie": "Übergangsmetalle", "elektronegativität": 1.55},
    {"symbol": "Fe", "name": "Eisen", "ordnungszahl": 26, "gruppe": 8, "periode": 4, "atommasse": 55.845, "kategorie": "Übergangsmetalle", "elektronegativität": 1.83},
    {"symbol": "Co", "name": "Cobalt", "ordnungszahl": 27, "gruppe": 9, "periode": 4, "atommasse": 58.933, "kategorie": "Übergangsmetalle", "elektronegativität": 1.88},
    {"symbol": "Ni", "name": "Nickel", "ordnungszahl": 28, "gruppe": 10, "periode": 4, "atommasse": 58.693, "kategorie": "Übergangsmetalle", "elektronegativität": 1.91},
    {"symbol": "Cu", "name": "Kupfer", "ordnungszahl": 29, "gruppe": 11, "periode": 4, "atommasse": 63.546, "kategorie": "Übergangsmetalle", "elektronegativität": 1.90},
    {"symbol": "Zn", "name": "Zink", "ordnungszahl": 30, "gruppe": 12, "periode": 4, "atommasse": 65.380, "kategorie": "Übergangsmetalle", "elektronegativität": 1.65},
    {"symbol": "Ga", "name": "Gallium", "ordnungszahl": 31, "gruppe": 13, "periode": 4, "atommasse": 69.723, "kategorie": "Übergangsmetalle", "elektronegativität": 1.81},
    {"symbol": "Ge", "name": "Germanium", "ordnungszahl": 32, "gruppe": 14, "periode": 4, "atommasse": 72.640, "kategorie": "Halbmetalle", "elektronegativität": 2.01},
    {"symbol": "As", "name": "Arsen", "ordnungszahl": 33, "gruppe": 15, "periode": 4, "atommasse": 74.922, "kategorie": "Halbmetalle", "elektronegativität": 2.18},
    {"symbol": "Se", "name": "Selen", "ordnungszahl": 34, "gruppe": 16, "periode": 4, "atommasse": 78.971, "kategorie": "Nichtmetalle", "elektronegativität": 2.55},
    {"symbol": "Br", "name": "Brom", "ordnungszahl": 35, "gruppe": 17, "periode": 4, "atommasse": 79.904, "kategorie": "Halogene", "elektronegativität": 2.96},
    {"symbol": "Kr", "name": "Krypton", "ordnungszahl": 36, "gruppe": 18, "periode": 4, "atommasse": 83.798, "kategorie": "Edelgase", "elektronegativität": None},
    
    # Periode 5
    {"symbol": "Rb", "name": "Rubidium", "ordnungszahl": 37, "gruppe": 1, "periode": 5, "atommasse": 85.468, "kategorie": "Alkalimetalle", "elektronegativität": 0.82},
    {"symbol": "Sr", "name": "Strontium", "ordnungszahl": 38, "gruppe": 2, "periode": 5, "atommasse": 87.62, "kategorie": "Erdalkalimetalle", "elektronegativität": 0.95},
    {"symbol": "Y", "name": "Yttrium", "ordnungszahl": 39, "gruppe": 3, "periode": 5, "atommasse": 88.906, "kategorie": "Übergangsmetalle", "elektronegativität": 1.22},
    {"symbol": "Zr", "name": "Zirkonium", "ordnungszahl": 40, "gruppe": 4, "periode": 5, "atommasse": 91.224, "kategorie": "Übergangsmetalle", "elektronegativität": 1.33},
    {"symbol": "Nb", "name": "Niobium", "ordnungszahl": 41, "gruppe": 5, "periode": 5, "atommasse": 92.906, "kategorie": "Übergangsmetalle", "elektronegativität": 1.60},
    {"symbol": "Mo", "name": "Molybdän", "ordnungszahl": 42, "gruppe": 6, "periode": 5, "atommasse": 95.95, "kategorie": "Übergangsmetalle", "elektronegativität": 2.16},
    {"symbol": "Tc", "name": "Technetium", "ordnungszahl": 43, "gruppe": 7, "periode": 5, "atommasse": 98, "kategorie": "Übergangsmetalle", "elektronegativität": 1.90},
    {"symbol": "Ru", "name": "Ruthenium", "ordnungszahl": 44, "gruppe": 8, "periode": 5, "atommasse": 101.07, "kategorie": "Übergangsmetalle", "elektronegativität": 2.20},
    {"symbol": "Rh", "name": "Rhodium", "ordnungszahl": 45, "gruppe": 9, "periode": 5, "atommasse": 102.906, "kategorie": "Übergangsmetalle", "elektronegativität": 2.28},
    {"symbol": "Pd", "name": "Palladium", "ordnungszahl": 46, "gruppe": 10, "periode": 5, "atommasse": 106.42, "kategorie": "Übergangsmetalle", "elektronegativität": 2.20},
    {"symbol": "Ag", "name": "Silber", "ordnungszahl": 47, "gruppe": 11, "periode": 5, "atommasse": 107.868, "kategorie": "Übergangsmetalle", "elektronegativität": 1.93},
    {"symbol": "Cd", "name": "Cadmium", "ordnungszahl": 48, "gruppe": 12, "periode": 5, "atommasse": 112.411, "kategorie": "Übergansmetalle", "elektronegativität": 1.69},
    {"symbol": "In", "name": "Indium", "ordnungszahl": 49, "gruppe": 13, "periode": 5, "atommasse": 114.818, "kategorie": "Übergansmetalle", "elektronegativität": 1.78},
    {"symbol": "Sn", "name": "Zinn", "ordnungszahl": 50, "gruppe": 14, "periode": 5, "atommasse": 118.711, "kategorie": "Übergansmetalle", "elektronegativität": 1.96},
    {"symbol": "Sb", "name": "Antimon", "ordnungszahl": 51, "gruppe": 15, "periode": 5, "atommasse": 121.760, "kategorie": "Halbmetalle", "elektronegativität": 2.05},
    {"symbol": "Te", "name": "Tellur", "ordnungszahl": 52, "gruppe": 16, "periode": 5, "atommasse": 127.60, "kategorie": "Halbmetalle", "elektronegativität": 2.10},
    {"symbol": "I", "name": "Iod", "ordnungszahl": 53, "gruppe": 17, "periode": 5, "atommasse": 126.904, "kategorie": "Halogene", "elektronegativität": 2.66},
    {"symbol": "Xe", "name": "Xenon", "ordnungszahl": 54, "gruppe": 18, "periode": 5, "atommasse": 131.293, "kategorie": "Edelgase", "elektronegativität": None},
    
    # Periode 6
    {"symbol": "Cs", "name": "Caesium", "ordnungszahl": 55, "gruppe": 1, "periode": 6, "atommasse": 132.905, "kategorie": "Alkalimetalle", "elektronegativität": 0.79},
    {"symbol": "Ba", "name": "Barium", "ordnungszahl": 56, "gruppe": 2, "periode": 6, "atommasse": 137.327, "kategorie": "Erdalkalimetalle", "elektronegativität": 0.89},
    {"symbol": "La", "name": "Lanthan", "ordnungszahl": 57, "gruppe": 3, "periode": 6, "atommasse": 138.906, "kategorie": "Lanthanoide", "elektronegativität": 1.10},
    {"symbol": "Ce", "name": "Cer", "ordnungszahl": 58, "gruppe": 3, "periode": 6, "atommasse": 140.116, "kategorie": "Lanthanoide", "elektronegativität": 1.12},
    {"symbol": "Pr", "name": "Praseodym", "ordnungszahl": 59, "gruppe": 3, "periode": 6, "atommasse": 140.908, "kategorie": "Lanthanoide", "elektronegativität": 1.13},
    {"symbol": "Nd", "name": "Neodym", "ordnungszahl": 60, "gruppe": 3, "periode": 6, "atommasse": 144.242, "kategorie": "Lanthanoide", "elektronegativität": 1.14},
    {"symbol": "Pm", "name": "Promethium", "ordnungszahl": 61, "gruppe": 3, "periode": 6, "atommasse": 145, "kategorie": "Lanthanoide", "elektronegativität": None},
    {"symbol": "Sm", "name": "Samarium", "ordnungszahl": 62, "gruppe": 3, "periode": 6, "atommasse": 150.36, "kategorie": "Lanthanoide", "elektronegativität": 1.17},
    {"symbol": "Eu", "name": "Europium", "ordnungszahl": 63, "gruppe": 3, "periode": 6, "atommasse": 151.964, "kategorie": "Lanthanoide", "elektronegativität": None},
    {"symbol": "Gd", "name": "Gadolinium", "ordnungszahl": 64, "gruppe": 3, "periode": 6, "atommasse": 157.25, "kategorie": "Lanthanoide", "elektronegativität": 1.20},
    {"symbol": "Tb", "name": "Terbium", "ordnungszahl": 65, "gruppe": 3, "periode": 6, "atommasse": 158.925, "kategorie": "Lanthanoide", "elektronegativität": None},
    {"symbol": "Dy", "name": "Dysprosium", "ordnungszahl": 66, "gruppe": 3, "periode": 6, "atommasse": 162.500, "kategorie": "Lanthanoide", "elektronegativität": 1.22},
    {"symbol": "Ho", "name": "Holmium", "ordnungszahl": 67, "gruppe": 3, "periode": 6, "atommasse": 164.930, "kategorie": "Lanthanoide", "elektronegativität": 1.23},
    {"symbol": "Er", "name": "Erbium", "ordnungszahl": 68, "gruppe": 3, "periode": 6, "atommasse": 167.259, "kategorie": "Lanthanoide", "elektronegativität": 1.24},
    {"symbol": "Tm", "name": "Thulium", "ordnungszahl": 69, "gruppe": 3, "periode": 6, "atommasse": 168.934, "kategorie": "Lanthanoide", "elektronegativität": 1.25},
    {"symbol": "Yb", "name": "Ytterbium", "ordnungszahl": 70, "gruppe": 3, "periode": 6, "atommasse": 173.04, "kategorie": "Lanthanoide", "elektronegativität": None},
    {"symbol": "Lu", "name": "Lutetium", "ordnungszahl": 71, "gruppe": 3, "periode": 6, "atommasse": 174.967, "kategorie": "Lanthanoide", "elektronegativität": 1.27},
    {"symbol": "Hf", "name": "Hafnium", "ordnungszahl": 72, "gruppe": 4, "periode": 6, "atommasse": 178.49, "kategorie": "Übergansmetalle", "elektronegativität": 1.30},
    {"symbol": "Ta", "name": "Tantal", "ordnungszahl": 73, "gruppe": 5, "periode": 6, "atommasse": 180.948, "kategorie": "Übergansmetalle", "elektronegativität": 1.50},
    {"symbol": "W", "name": "Wolfram", "ordnungszahl": 74, "gruppe": 6, "periode": 6, "atommasse": 183.84, "kategorie": "Übergansmetalle", "elektronegativität": 2.36},
    {"symbol": "Re", "name": "Rhenium", "ordnungszahl": 75, "gruppe": 7, "periode": 6, "atommasse": 186.207, "kategorie": "Übergansmetalle", "elektronegativität": 1.90},
    {"symbol": "Os", "name": "Osmium", "ordnungszahl": 76, "gruppe": 8, "periode": 6, "atommasse": 190.23, "kategorie": "Übergansmetalle", "elektronegativität": 2.20},
    {"symbol": "Ir", "name": "Iridium", "ordnungszahl": 77, "gruppe": 9, "periode": 6, "atommasse": 192.217, "kategorie": "Übergansmetalle", "elektronegativität": 2.20},
    {"symbol": "Pt", "name": "Platin", "ordnungszahl": 78, "gruppe": 10, "periode": 6, "atommasse": 195.084, "kategorie": "Übergansmetalle", "elektronegativität": 2.28},
    {"symbol": "Au", "name": "Gold", "ordnungszahl": 79, "gruppe": 11, "periode": 6, "atommasse": 196.967, "kategorie": "Übergansmetalle", "elektronegativität": 2.54},
    {"symbol": "Hg", "name": "Quecksilber", "ordnungszahl": 80, "gruppe": 12, "periode": 6, "atommasse": 200.592, "kategorie": "Übergansmetalle", "elektronegativität": 2.00},
    {"symbol": "Tl", "name": "Thallium", "ordnungszahl": 81, "gruppe": 13, "periode": 6, "atommasse": 204.383, "kategorie": "Übergansmetalle", "elektronegativität": 1.62},
    {"symbol": "Pb", "name": "Blei", "ordnungszahl": 82, "gruppe": 14, "periode": 6, "atommasse": 207.2, "kategorie": "Übergansmetalle", "elektronegativität": 2.33},
    {"symbol": "Bi", "name": "Bismut", "ordnungszahl": 83, "gruppe": 15, "periode": 6, "atommasse": 208.980, "kategorie": "Übergansmetalle", "elektronegativität": 2.02},
    {"symbol": "Po", "name": "Polonium", "ordnungszahl": 84, "gruppe": 16, "periode": 6, "atommasse": 209, "kategorie": "Halbmetalle", "elektronegativität": 2.00},
    {"symbol": "At", "name": "Astat", "ordnungszahl": 85, "gruppe": 17, "periode": 6, "atommasse": 210, "kategorie": "Halogene", "elektronegativität": 2.20},
    {"symbol": "Rn", "name": "Radon", "ordnungszahl": 86, "gruppe": 18, "periode": 6, "atommasse": 222, "kategorie": "Edelgase", "elektronegativität": None},
    
    # Periode 7
    {"symbol": "Fr", "name": "Francium", "ordnungszahl": 87, "gruppe": 1, "periode": 7, "atommasse": 223, "kategorie": "Alkalimetalle", "elektronegativität": 0.7},
    {"symbol": "Ra", "name": "Radium", "ordnungszahl": 88, "gruppe": 2, "periode": 7, "atommasse": 226, "kategorie": "Erdalkalimetalle", "elektronegativität": 0.9},
    {"symbol": "Ac", "name": "Actinium", "ordnungszahl": 89, "gruppe": 3, "periode": 7, "atommasse": 227, "kategorie": "Actinoide", "elektronegativität": 1.1},
    {"symbol": "Th", "name": "Thorium", "ordnungszahl": 90, "gruppe": 3, "periode": 7, "atommasse": 232.038, "kategorie": "Actinoide", "elektronegativität": 1.3},
    {"symbol": "Pa", "name": "Protactinium", "ordnungszahl": 91, "gruppe": 3, "periode": 7, "atommasse": 231.036, "kategorie": "Actinoide", "elektronegativität": 1.5},
    {"symbol": "U", "name": "Uran", "ordnungszahl": 92, "gruppe": 3, "periode": 7, "atommasse": 238.029, "kategorie": "Actinoide", "elektronegativität": 1.38},
    {"symbol": "Np", "name": "Neptunium", "ordnungszahl": 93, "gruppe": 3, "periode": 7, "atommasse": 237, "kategorie": "Actinoide", "elektronegativität": 1.36},
    {"symbol": "Pu", "name": "Plutonium", "ordnungszahl": 94, "gruppe": 3, "periode": 7, "atommasse": 244, "kategorie": "Actinoide", "elektronegativität": 1.28},
    {"symbol": "Am", "name": "Americium", "ordnungszahl": 95, "gruppe": 3, "periode": 7, "atommasse": 243, "kategorie": "Actinoide", "elektronegativität": 1.30},
    {"symbol": "Cm", "name": "Curium", "ordnungszahl": 96, "gruppe": 3, "periode": 7, "atommasse": 247, "kategorie": "Actinoide", "elektronegativität": 1.30},
    {"symbol": "Bk", "name": "Berkelium", "ordnungszahl": 97, "gruppe": 3, "periode": 7, "atommasse": 247, "kategorie": "Actinoide", "elektronegativität": 1.30},
    {"symbol": "Cf", "name": "Californium", "ordnungszahl": 98, "gruppe": 3, "periode": 7, "atommasse": 251, "kategorie": "Actinoide", "elektronegativität": 1.30},
    {"symbol": "Es", "name": "Einsteinium", "ordnungszahl": 99, "gruppe": 3, "periode": 7, "atommasse": 252, "kategorie": "Actinoide", "elektronegativität": 1.30},
    {"symbol": "Fm", "name": "Fermium", "ordnungszahl": 100, "gruppe": 3, "periode": 7, "atommasse": 257, "kategorie": "Actinoide", "elektronegativität": 1.30},
    {"symbol": "Md", "name": "Mendelevium", "ordnungszahl": 101, "gruppe": 3, "periode": 7, "atommasse": 258, "kategorie": "Actinoide", "elektronegativität": 1.30},
    {"symbol": "No", "name": "Nobelium", "ordnungszahl": 102, "gruppe": 3, "periode": 7, "atommasse": 259, "kategorie": "Actinoide", "elektronegativität": 1.30},
    {"symbol": "Lr", "name": "Lawrencium", "ordnungszahl": 103, "gruppe": 3, "periode": 7, "atommasse": 262, "kategorie": "Actinoide", "elektronegativität": None},
    {"symbol": "Rf", "name": "Rutherfordium", "ordnungszahl": 104, "gruppe": 4, "periode": 7, "atommasse": 267, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Db", "name": "Dubnium", "ordnungszahl": 105, "gruppe": 5, "periode": 7, "atommasse": 270, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Sg", "name": "Seaborgium", "ordnungszahl": 106, "gruppe": 6, "periode": 7, "atommasse": 271, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Bh", "name": "Bohrium", "ordnungszahl": 107, "gruppe": 7, "periode": 7, "atommasse": 270, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Hs", "name": "Hassium", "ordnungszahl": 108, "gruppe": 8, "periode": 7, "atommasse": 277, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Mt", "name": "Meitnerium", "ordnungszahl": 109, "gruppe": 9, "periode": 7, "atommasse": 278, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Ds", "name": "Darmstadium", "ordnungszahl": 110, "gruppe": 10, "periode": 7, "atommasse": 281, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Rg", "name": "Roentgenium", "ordnungszahl": 111, "gruppe": 11, "periode": 7, "atommasse": 280, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Cn", "name": "Copernicium", "ordnungszahl": 112, "gruppe": 12, "periode": 7, "atommasse": 285, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Nh", "name": "Nihonium", "ordnungszahl": 113, "gruppe": 13, "periode": 7, "atommasse": 286, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Fl", "name": "Flerovium", "ordnungszahl": 114, "gruppe": 14, "periode": 7, "atommasse": 289, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Mc", "name": "Moscovium", "ordnungszahl": 115, "gruppe": 15, "periode": 7, "atommasse": 290, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Lv", "name": "Livermorium", "ordnungszahl": 116, "gruppe": 16, "periode": 7, "atommasse": 293, "kategorie": "Übergansmetalle", "elektronegativität": None},
    {"symbol": "Ts", "name": "Tennessium", "ordnungszahl": 117, "gruppe": 17, "periode": 7, "atommasse": 294, "kategorie": "Halogene", "elektronegativität": None},
    {"symbol": "Og", "name": "Oganesson", "ordnungszahl": 118, "gruppe": 18, "periode": 7, "atommasse": 294, "kategorie": "Edelgase", "elektronegativität": None},
]

# Farbschema für Kategorien
farben_kategorien = {
    "Alkalimetalle": "#FF9999",
    "Erdalkalimetalle": "#FFCC99",
    "Lanthanoide": "#FFBFFF",
    "Actinoide": "#FF99CC",
    "Übergansmetalle": "#CCCCFF",
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