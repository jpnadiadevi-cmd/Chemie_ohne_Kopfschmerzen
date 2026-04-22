import streamlit as st

st.title("🧮 Mol-Rechner")
st.markdown("---")

# Abschnitt 1: Stoffmenge (n = m / M)
st.header("Stoffmenge (n)")
st.latex(r"n = \frac{m}{M}")
col1, col2 = st.columns(2)
with col1:
    m1 = st.number_input("Masse m [g]", key="mol_m1", value=0.0, format="%.4f")
    M1 = st.number_input("Molare Masse M [g/mol]", key="mol_M1", value=0.0, format="%.4f")
with col2:
    n1 = m1 / M1 if M1 != 0 else 0.0
    st.text_input("Stoffmenge n [mol]", value=f"{n1:.4f}", disabled=True)

st.markdown("---")

# Abschnitt 2: Masse (m = M * n)
st.header("Masse (m)")
st.latex(r"m = M \cdot n")
col3, col4 = st.columns(2)
with col3:
    M2 = st.number_input("Molare Masse M [g/mol]", key="mol_M2", value=0.0, format="%.4f")
    n2 = st.number_input("Stoffmenge n [mol]", key="mol_n2", value=0.0, format="%.4f")
with col4:
    m2 = M2 * n2
    st.text_input("Masse m [g]", value=f"{m2:.4f}", disabled=True)

st.markdown("---")

# Abschnitt 3: Molare Masse (M = m / n)
st.header("Molare Masse (M)")
st.latex(r"M = \frac{m}{n}")
col5, col6 = st.columns(2)
with col5:
    m3 = st.number_input("Masse m [g]", key="mol_m3", value=0.0, format="%.4f")
    n3 = st.number_input("Stoffmenge n [mol]", key="mol_n3", value=0.0, format="%.4f")
with col6:
    M3 = m3 / n3 if n3 != 0 else 0.0
    st.text_input("Molare Masse M [g/mol]", value=f"{M3:.4f}", disabled=True)

st.info("Zwei Werte eingeben, der dritte wird berechnet.")
