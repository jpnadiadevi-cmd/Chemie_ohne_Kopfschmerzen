import streamlit as st
from datetime import datetime
import json

from utils.storage import save_to_switchdrive


st.set_page_config(layout="wide")

st.title("🧪 Konzentrationen & Teilchenzahl")
st.markdown("---")

st.write("""
Berechne wichtige Konzentrationen und Teilchenzahlen in der Chemie!

Diese Seite hilft dir bei:
- **Molarität** (Konzentration in mol/L)
- **Molalität** (Konzentration in mol/g)
- **Teilchenzahl** (Anzahl der Atome/Moleküle)

Gib einfach die Werte ein und erhalte sofort das Ergebnis! 🔬
""")

st.markdown("---")


def save_to_local(filename, data):
    """Speichert Daten lokal als JSON"""
    try:
        json_data = json.dumps(data, indent=4, ensure_ascii=False)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_data)

        return True

    except Exception as e:
        st.error(f"Fehler beim lokalen Speichern: {str(e)}")
        return False


if "logbuch_daten" not in st.session_state:
    st.session_state.logbuch_daten = {
        "molmasse": [],
        "molformel": [],
        "konzentration": []
    }


AVOGADRO = 6.022e23


def speichere_ins_logbuch(eintrag):
    st.session_state.logbuch_daten["konzentration"].append(eintrag)

    save_to_local(
        "konzentration_logbuch.json",
        st.session_state.logbuch_daten["konzentration"]
    )

    if save_to_switchdrive(
        "konzentration_logbuch.json",
        st.session_state.logbuch_daten["konzentration"]
    ):
        st.success("✅ Auf SwitchDrive und lokal gespeichert!")
    else:
        st.info("💾 Lokal gespeichert")


st.subheader("1️⃣ Molarität: c [mol/L] = n / V")
st.write("*Berechne die Konzentration einer Lösung*")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.write("**Eingaben:**")
    n_molar = st.number_input(
        "Stoffmenge n [mol]",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="n_molar"
    )

    V_molar = st.number_input(
        "Volumen V [L]",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="V_molar"
    )

with col2:
    st.write("")

with col3:
    st.write("**Ergebnis:**")
    if V_molar > 0:
        c_molar = n_molar / V_molar
        st.metric("Molarität c", f"{c_molar:.4f} mol/L")
    else:
        st.info("ℹ️ Bitte gib ein Volumen > 0 ein")

st.markdown("---")


st.subheader("2️⃣ Molalität: β [mol/g] = n / m")
st.write("*Berechne die Molalität einer Lösung*")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.write("**Eingaben:**")
    n_molal = st.number_input(
        "Stoffmenge n [mol]",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="n_molal"
    )

    m_molal = st.number_input(
        "Masse m [g]",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="m_molal"
    )

with col2:
    st.write("")

with col3:
    st.write("**Ergebnis:**")
    if m_molal > 0:
        beta_molal = n_molal / m_molal
        st.metric("Molalität β", f"{beta_molal:.4f} mol/g")
    else:
        st.info("ℹ️ Bitte gib eine Masse > 0 ein")

st.markdown("---")


st.subheader("3️⃣ Teilchenzahl: N = n × 6.022 × 10²³")
st.write("*Berechne die Anzahl der Atome/Moleküle*")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.write("**Eingaben:**")
    n_teilchen = st.number_input(
        "Stoffmenge n [mol]",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="n_teilchen"
    )

with col2:
    st.write("")

with col3:
    st.write("**Ergebnis:**")
    N = n_teilchen * AVOGADRO

    if N >= 1e9:
        st.metric("Teilchenzahl N", f"{N:.3e}")
    else:
        st.metric("Teilchenzahl N", f"{N:,.0f}")

st.markdown("---")

st.write("""
**Wichtige Konstanten:**
- 🔬 **Avogadro-Konstante**: 6.022 × 10²³ (Teilchen/mol)
- 💧 **Dichte von Wasser**: ≈ 1 g/mL = 1 kg/L

**Tipp:** Molalität ist temperaturunabhängig, Molarität dagegen nicht!
""")

st.markdown("---")


col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💾 Molarität ins Logbuch", key="save_molar"):
        if V_molar > 0:
            eintrag = {
                "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "Rechnung": "Molarität",
                "Eingaben": f"n={n_molar} mol, V={V_molar} L",
                "Ergebnis": f"c={n_molar / V_molar:.4f} mol/L"
            }

            speichere_ins_logbuch(eintrag)

        else:
            st.warning("⚠️ Bitte erst Werte eingeben!")


with col2:
    if st.button("💾 Molalität ins Logbuch", key="save_molal"):
        if m_molal > 0:
            eintrag = {
                "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "Rechnung": "Molalität",
                "Eingaben": f"n={n_molal} mol, m={m_molal} g",
                "Ergebnis": f"β={n_molal / m_molal:.4f} mol/g"
            }

            speichere_ins_logbuch(eintrag)

        else:
            st.warning("⚠️ Bitte erst Werte eingeben!")


with col3:
    if st.button("💾 Teilchenzahl ins Logbuch", key="save_teilchen"):
        eintrag = {
            "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "Rechnung": "Teilchenzahl",
            "Eingaben": f"n={n_teilchen} mol",
            "Ergebnis": f"N={n_teilchen * AVOGADRO:.3e}"
        }

        speichere_ins_logbuch(eintrag)