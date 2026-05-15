import streamlit as st
import pandas as pd

from utils.data_manager import DataManager
from utils.login_manager import LoginManager

data_manager = DataManager(       # initialize data manager
    fs_protocol='webdav',         # protocol for the filesystem, use webdav for switch drive
    fs_root_folder="BMLD_App_DB"  # folder on switch drive where the data is stored
    ) 
login_manager = LoginManager(data_manager) # handles user login and registration
login_manager.login_register()             # stops if not logged in
# --- END OF NEW CODE ---

# --- CODE UPDATE: load user data from data manager if not already present in session state --
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = data_manager.load_user_data(
        'data.csv',                     # The file on switch drive where the data is stored
        initial_value=pd.DataFrame(),   # Initial value if the file does not exist
        parse_dates=['timestamp']       # Parse timestamp as datetime
    )
# --- END OF CODE UPDATE ---

if "logbuch_daten" not in st.session_state:
    st.session_state.logbuch_daten = {
        "konzentration": [],
        "molformel": [],
        "molmasse": []
    }

if 'data_df' not in st.session_state:
    st.session_state['data_df'] = data_manager.load_user_data(
        'data.csv',
        initial_value=pd.DataFrame(),
        parse_dates=['timestamp']
    )

# Seitenkonfiguration
st.set_page_config(
    page_title="Meine App",
    page_icon=":material/home:"
)

# Seiten definieren
pg_home = st.Page(
    "views/home.py",
    title="Home",
    icon=":material/home:",
    default=True
)

pg_periodensystem = st.Page(
    "views/periodensystem.py",
    title="Periodensystem",
    icon=":material/table_chart:"
)

pg_formelsammlung = st.Page(
    "views/formelsammlung.py",
    title="Formelsammlung",
    icon=":material/menu_book:"
)

pg_formelsammlung_konzentrationen = st.Page(
    "views/formelsammlung_konzentrationen.py",
    title="Konzentrationen und Teilchen",
    icon=":material/water:"
)

pg_formelsammlung_molformel = st.Page(
    "views/formelsammlung_molformel.py",
    title="Die Molformel",
    icon=":material/bubble_chart:"
)

pg_formelsammlung_molmasse = st.Page(
    "views/formelsammlung_molmasse.py",
    title="Die molare Masse mit PSE",
    icon=":material/scale:"
)

pg_logbuch = st.Page(
    "views/logbuch.py",
    title="Logbuch",
    icon=":material/edit_note:"
)

pg_protokoll = st.Page(
    "views/protokoll.py",
    title="Protokoll",
    icon=":material/description:"
)

# Navigation
pg = st.navigation([
    pg_home,
    pg_periodensystem,
    pg_formelsammlung,
    pg_formelsammlung_konzentrationen,
    pg_formelsammlung_molformel,
    pg_formelsammlung_molmasse,
    pg_logbuch,
    pg_protokoll
])

# App starten
pg.run()