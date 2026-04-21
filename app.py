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

# Seitenkonfiguration (nur einmal!)
st.set_page_config(
    page_title="Meine App",
    page_icon=":material/home:"
)

# 👉 HIER kommt dein Code rein
# Seiten definieren
pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_rechner = st.Page("views/Rechner.py", title="Rechner", icon=":material/science:")

pg_periodensystem = st.Page("views/periodensystem.py", title="Periodensystem", icon=":material/table_chart:")
pg_formelsammlung = st.Page("views/formelsammlung.py", title="Formelsammlung", icon=":material/menu_book:")
pg_logbuch = st.Page("views/logbuch.py", title="Logbuch", icon=":material/edit_note:")
pg_protokoll = st.Page("views/protokoll.py", title="Protokoll", icon=":material/description:")

pg = st.navigation([
    pg_home,
    pg_rechner,
    pg_periodensystem,
    pg_formelsammlung,
    pg_logbuch,
    pg_protokoll
])

pg.run()