import json
import requests
import streamlit as st
from urllib.parse import quote


def save_to_switchdrive(filename, data):
    """Speichert Daten auf SwitchDrive als JSON"""

    try:
        username = st.secrets["webdav"]["username"]
        password = st.secrets["webdav"]["password"]

        json_data = json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        )

        json_bytes = json_data.encode("utf-8")

        # GEMEINSAMER ORDNER
        remote_path = f"Chemie_Informatik2/{filename}"

        upload_url = (
            f"https://{quote(username, safe='')}:{quote(password, safe='')}"
            f"@drive.switch.ch/remote.php/webdav/{remote_path}"
        )

        response = requests.put(
            upload_url,
            data=json_bytes,
            headers={"Content-Type": "application/json"},
            verify=True
        )

        if response.status_code in [200, 201, 204]:
            return True
        else:
            st.error(f"SwitchDrive Fehler: {response.status_code}")
            return False

    except Exception as e:
        st.error(f"Fehler beim Upload: {str(e)}")
        return False