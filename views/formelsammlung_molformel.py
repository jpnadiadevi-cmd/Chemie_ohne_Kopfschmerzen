import streamlit as st
from datetime import datetime

st.title("🧬 Die Molformel")

st.markdown("---")

st.header("Berechne Stoffmenge, Masse oder Molare Masse")
st.latex(r"n = \frac{m}{M} \quad | \quad m = M \cdot n \quad | \quad M = \frac{m}{n}")

st.markdown("---")

if "logbuch_daten" not in st.session_state:
    st.session_state.logbuch_daten = {
        "molmasse": [],
        "molformel": [],
        "konzentration": []
    }

col1, col2, col3 = st.columns(3)

with col1:
    n_input = st.number_input(
        "Stoffmenge n [mol]",
        value=0.0,
        format="%.4f",
        key="n_input"
    )

with col2:
    m_input = st.number_input(
        "Masse m [g]",
        value=0.0,
        format="%.4f",
        key="m_input"
    )

with col3:
    M_input = st.number_input(
        "Molare Masse M [g/mol]",
        value=0.0,
        format="%.4f",
        key="M_input"
    )

st.markdown("---")

eingegeben_count = sum([n_input > 0, m_input > 0, M_input > 0])

st.subheader("📊 Ergebnis")

result_text = None
result_key = None
result_value = None

if n_input > 0 and m_input > 0 and M_input == 0:
    M_result = m_input / n_input
    st.metric("Molare Masse M [g/mol]", f"{M_result:.4f}")
    result_text = f"M = {M_result:.4f}"
    result_key = "M"
    result_value = M_result

elif n_input > 0 and M_input > 0 and m_input == 0:
    m_result = M_input * n_input
    st.metric("Masse m [g]", f"{m_result:.4f}")
    result_text = f"m = {m_result:.4f}"
    result_key = "m"
    result_value = m_result

elif m_input > 0 and M_input > 0 and n_input == 0:
    n_result = m_input / M_input
    st.metric("Stoffmenge n [mol]", f"{n_result:.4f}")
    result_text = f"n = {n_result:.4f}"
    result_key = "n"
    result_value = n_result

elif eingegeben_count == 1:
    st.warning("⚠️ Bitte gib mindestens zwei Werte ein!")

elif eingegeben_count == 0:
    st.info("👆 Bitte gib zwei Werte ein, um den dritten zu berechnen.")

else:
    st.error("❌ Bitte gib nur zwei Werte ein!")

st.markdown("---")

if result_text is not None:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("💾 Ergebnis ins Logbuch speichern", use_container_width=True, key="save_molformel"):
            eintrag = {
                "Datum & Uhrzeit": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "Rechnung": "Molformel (n, m, M)",
                "Eingaben": f"n={n_input if n_input > 0 else '—'}, m={m_input if m_input > 0 else '—'}, M={M_input if M_input > 0 else '—'}",
                "Ergebnis": f"{result_key}={result_value:.4f}"
            }

            st.session_state.logbuch_daten["molformel"].append(eintrag)

            st.session_state.data_manager.save_user_data(
                st.session_state.logbuch_daten,
                "logbuch_daten.json"
            )

            st.success(
                f"✅ {result_key}={result_value:.4f} im Logbuch und auf SwitchDrive gespeichert!"
            )