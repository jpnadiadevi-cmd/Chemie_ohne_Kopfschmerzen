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
# DESIGN
# ---------------------------------------------------

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        180deg,
        #fff8eb 0%,
        #fffdf8 45%,
        #ffffff 100%
    );
}

/* CONTENT */
.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1200px;
}

/* HERO */
.hero-box {

    background: rgba(255,255,255,0.88);

    border-radius: 30px;

    padding: 2rem;

    box-shadow:
        0 15px 40px rgba(0,0,0,0.08);

    margin-bottom: 3rem;
}

.hero-title {

    font-size: 3rem;

    font-weight: 800;

    color: #30303d;

    margin-bottom: 0.7rem;
}

.hero-text {

    font-size: 1.1rem;

    line-height: 1.8;

    color: #5e5e6d;
}

/* FORMULA BOX */
.formula-box {

    background: rgba(255,255,255,0.82);

    border-radius: 24px;

    padding: 2rem;

    box-shadow:
        0 8px 22px rgba(0,0,0,0.06);

    text-align: center;

    margin-bottom: 3rem;
}

/* CALC SECTION */
.calc-card {

    margin-bottom: 4rem;
}

.calc-title {

    font-size: 1.8rem;

    font-weight: 800;

    color: #30303d;

    margin-bottom: 0.4rem;
}

.calc-subtitle {

    color: #70707d;

    margin-bottom: 1.8rem;

    font-style: italic;
}

/* RESULT BOXES */
[data-testid="stMetric"] {

    background: #fff8ea;

    border: 1px solid #f3dfb6;

    padding: 1rem;

    border-radius: 22px;

    box-shadow:
        0 5px 15px rgba(0,0,0,0.04);
}

/* INFO BOX */
[data-testid="stAlert"] {

    background: #fff8ea !important;

    border: 1px solid #f3dfb6 !important;

    border-radius: 22px !important;

    padding: 1rem !important;

    box-shadow:
        0 5px 15px rgba(0,0,0,0.04) !important;
}

[data-testid="stAlert"] p {

    color: #30303d !important;

    font-size: 1.2rem !important;

    font-weight: 700 !important;
}

/* INPUTS */
.stNumberInput > div {

    border-radius: 14px;
}

/* DIVIDERS */
hr {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO
# ---------------------------------------------------

st.markdown("""
<div class="hero-box">

<div class="hero-title">
🧬 Die Molformel
</div>

<div class="hero-text">
Berechne Stoffmenge, Masse oder molare Masse schnell und übersichtlich.

Gib einfach zwei Werte ein — der dritte Wert wird automatisch berechnet.
</div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# FORMULAS
# ---------------------------------------------------

st.markdown("""
<div class="formula-box">
""", unsafe_allow_html=True)

st.markdown("""
# Berechne Stoffmenge, Masse oder Molare Masse
""")

st.latex(r"n = \frac{m}{M} \quad | \quad m = M \cdot n \quad | \quad M = \frac{m}{n}")

st.markdown("""
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# STOFFMENGE
# ---------------------------------------------------

st.markdown("""
<div class="calc-card">

<div class="calc-title">
1️⃣ Stoffmenge berechnen
</div>

<div class="calc-subtitle">
Formel: n = m / M
</div>

</div>
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
<div class="calc-card">

<div class="calc-title">
2️⃣ Masse berechnen
</div>

<div class="calc-subtitle">
Formel: m = M × n
</div>

</div>
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
<div class="calc-card">

<div class="calc-title">
3️⃣ Molare Masse berechnen
</div>

<div class="calc-subtitle">
Formel: M = m / n
</div>

</div>
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

