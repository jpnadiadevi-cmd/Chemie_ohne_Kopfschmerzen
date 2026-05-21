import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Molformel",
    page_icon="🧬",
    layout="wide"
)

# ---------------------------------------------------
# DESIGN WIE HOMEPAGE
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #fffdf8;
    color: #30303d;
}

.block-container {
    max-width: 1200px;
    padding-top: 2.2rem;
    padding-bottom: 4rem;
}

/* TITEL */
h1 {
    font-size: 3rem !important;
    font-weight: 800 !important;
    color: #30303d !important;
    letter-spacing: -0.04em;
    margin-bottom: 2.2rem !important;
}

h2, h3 {
    color: #30303d !important;
    font-weight: 800 !important;
    letter-spacing: -0.03em;
}

/* TRENNLINIEN */
hr {
    border: none;
    border-top: 1px solid #dedede;
    margin: 2.7rem 0 !important;
}

/* FORMEL */
[data-testid="stLatex"] {
    text-align: center;
    font-size: 1.25rem;
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
}

/* INPUT LABELS */
label {
    color: #30303d !important;
    font-weight: 500 !important;
}

/* NUMBER INPUT */
.stNumberInput input {
    background-color: #f1f3f8 !important;
    border: none !important;
    border-radius: 10px !important;
    color: #30303d !important;
    font-size: 1rem !important;
    padding: 0.8rem 1rem !important;
}

.stNumberInput input:focus {
    box-shadow: 0 0 0 2px rgba(245, 191, 79, 0.35) !important;
}

/* PLUS MINUS BUTTONS */
.stNumberInput button {
    background-color: #f1f3f8 !important;
    border: none !important;
    color: #30303d !important;
}

/* METRIC / RESULT */
[data-testid="stMetric"] {
    background: #fff8ea;
    border: 1px solid #f1d99d;
    border-radius: 16px;
    padding: 1.2rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.04);
}

[data-testid="stMetricLabel"] {
    color: #30303d !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"] {
    color: #30303d !important;
    font-weight: 800 !important;
}

/* INFO BOX */
[data-testid="stAlert"] {
    background-color: #eaf3ff !important;
    border: none !important;
    border-radius: 10px !important;
    color: #0054a6 !important;
}

[data-testid="stAlert"] p {
    font-size: 1rem !important;
    font-weight: 500 !important;
}

/* ABSCHNITTE */
.calc-title {
    font-size: 1.75rem;
    font-weight: 800;
    color: #30303d;
    letter-spacing: -0.03em;
    margin-bottom: 0.3rem;
}

.calc-subtitle {
    font-size: 1rem;
    color: #5e5e6d;
    margin-bottom: 1.5rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown("# 🧬 Die Molformel")
st.markdown("---")

st.markdown("## Berechne Stoffmenge, Masse oder Molare Masse")

st.latex(r"n = \frac{m}{M} \quad | \quad m = M \cdot n \quad | \quad M = \frac{m}{n}")

st.markdown("---")

# ---------------------------------------------------
# STOFFMENGE
# ---------------------------------------------------

st.markdown("""
<div class="calc-title">1️⃣ Stoffmenge berechnen</div>
<div class="calc-subtitle">Formel: n = m / M</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    m1 = st.number_input(
        "Masse m [g]",
        key="mol_m1",
        value=0.0,
        format="%.4f"
    )

    M1 = st.number_input(
        "Molare Masse M [g/mol]",
        key="mol_M1",
        value=0.0,
        format="%.4f"
    )

with col2:
    n1 = m1 / M1 if M1 != 0 else 0.0

    st.metric(
        "Stoffmenge n",
        f"{n1:.4f} mol"
    )

st.markdown("---")

# ---------------------------------------------------
# MASSE
# ---------------------------------------------------

st.markdown("""
<div class="calc-title">2️⃣ Masse berechnen</div>
<div class="calc-subtitle">Formel: m = M × n</div>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    M2 = st.number_input(
        "Molare Masse M [g/mol]",
        key="mol_M2",
        value=0.0,
        format="%.4f"
    )

    n2 = st.number_input(
        "Stoffmenge n [mol]",
        key="mol_n2",
        value=0.0,
        format="%.4f"
    )

with col4:
    m2 = M2 * n2

    st.metric(
        "Masse m",
        f"{m2:.4f} g"
    )

st.markdown("---")

# ---------------------------------------------------
# MOLARE MASSE
# ---------------------------------------------------

st.markdown("""
<div class="calc-title">3️⃣ Molare Masse berechnen</div>
<div class="calc-subtitle">Formel: M = m / n</div>
""", unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    m3 = st.number_input(
        "Masse m [g]",
        key="mol_m3",
        value=0.0,
        format="%.4f"
    )

    n3 = st.number_input(
        "Stoffmenge n [mol]",
        key="mol_n3",
        value=0.0,
        format="%.4f"
    )

with col6:
    M3 = m3 / n3 if n3 != 0 else 0.0

    st.metric(
        "Molare Masse M",
        f"{M3:.4f} g/mol"
    )

# ---------------------------------------------------
# INFO
# ---------------------------------------------------

st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)

st.info("👉 Zwei Werte eingeben, der dritte Wert wird automatisch berechnet.")