import streamlit as st

st.title("🧮 Mol-Rechner")

st.markdown("### Stoffmenge (n)")
st.latex(r"n = \frac{m}{M}")
col1, col2, col3 = st.columns(3)
with col1:
    m1 = st.number_input("m (g)", key="m1", value=0.0, format="%.4f")
with col2:
    M1 = st.number_input("M (g/mol)", key="M1", value=0.0, format="%.4f")
with col3:
    n1 = m1 / M1 if M1 else 0.0
    st.number_input("n (mol)", value=n1, format="%.4f", key="n1", disabled=True)

st.divider()

st.markdown("### Masse (m)")
st.latex(r"m = M \cdot n")
col4, col5, col6 = st.columns(3)
with col4:
    M2 = st.number_input("M (g/mol)", key="M2", value=0.0, format="%.4f")
with col5:
    n2 = st.number_input("n (mol)", key="n2", value=0.0, format="%.4f")
with col6:
    m2 = M2 * n2
    st.number_input("m (g)", value=m2, format="%.4f", key="m2", disabled=True)

st.divider()

st.markdown("### Molare Masse (M)")
st.latex(r"M = \frac{m}{n}")
col7, col8, col9 = st.columns(3)
with col7:
    m3 = st.number_input("m (g)", key="m3", value=0.0, format="%.4f")
with col8:
    n3 = st.number_input("n (mol)", key="n3", value=0.0, format="%.4f")
with col9:
    M3 = m3 / n3 if n3 else 0.0
    st.number_input("M (g/mol)", value=M3, format="%.4f", key="M3", disabled=True)
