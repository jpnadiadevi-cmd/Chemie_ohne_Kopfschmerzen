import streamlit as st
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
