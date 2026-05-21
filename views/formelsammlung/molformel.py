import streamlit as st

st.set_page_config(
    page_title="Molformel",
    page_icon="🧬",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fff8eb 0%, #fffdf8 45%, #ffffff 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1200px;
}

.hero-card {
    background: rgba(255,255,255,0.88);
    border-radius: 28px;
    padding: 2rem;
    box-shadow: 0 15px 40px rgba(0,0,0,0.08);
    margin-bottom: 2.5rem;
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

.formula-card {
    background: rgba(255,255,255,0.82);
    border-radius: 24px;
    padding: 1.6rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    border-left: 7px solid #f0c96a;
    text-align: center;
    margin-bottom: 2.5rem;
}

.formula-title {
    font-size: 1.9rem;
    font-weight: 800;
    color: #30303d;
    margin-bottom: 1rem;
}

.calc-title {
    font-size: 1.6rem;
    font-weight: 800;
    color: #30303d;
    margin-top: 2rem;
    margin-bottom: 0.4rem;
}

.calc-subtitle {
    color: #70707d;
    font-style: italic;
    margin-bottom: 1.2rem;
}

[data-testid="stMetric"] {
    background: #fff8ea;
    border: 1px solid #f3dfb6;
    padding: 1rem;
    border-radius: 22px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.04);
}

[data-testid="stAlert"] {
    background: #fff8ea !important;
    border: 1px solid #f3dfb6 !important;
    border-radius: 22px !important;
    padding: 1rem !important;
    box-shadow: 0 5px 15px rgba(0,0,0,0.04) !important;
}

[data-testid="stAlert"] p {
    color: #30303d !important;
    font-size: 1.2rem !important;
    font-weight: 700 !important;
}

.stNumberInput > div {
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-card">
    <div class="hero-title">🧬 Die Molformel</div>
    <div class="hero-text">
        Berechne Stoffmenge, Masse oder molare Masse schnell und übersichtlich.
        Gib einfach zwei Werte ein — der dritte Wert wird automatisch berechnet.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="formula-card">
    <div class="formula-title">Berechnungen mit der Molformel</div>
</div>
""", unsafe_allow_html=True)

st.latex(r"n = \frac{m}{M} \quad | \quad m = M \cdot n \quad | \quad M = \frac{m}{n}")

# ---------------------------------------------------
# STOFFMENGE
# ---------------------------------------------------

st.markdown('<div class="calc-title">1️⃣ Stoffmenge berechnen: n = m / M</div>', unsafe_allow_html=True)
st.markdown('<div class="calc-subtitle">Berechne die Stoffmenge aus Masse und molarer Masse</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    m1 = st.number_input("Masse m [g]", key="mol_m1", value=0.0, format="%.4f")
    M1 = st.number_input("Molare Masse M [g/mol]", key="mol_M1", value=0.0, format="%.4f")

with col2:
    n1 = m1 / M1 if M1 != 0 else 0.0
    st.metric("Stoffmenge n", f"{n1:.4f} mol")

# ---------------------------------------------------
# MASSE
# ---------------------------------------------------

st.markdown('<div class="calc-title">2️⃣ Masse berechnen: m = M × n</div>', unsafe_allow_html=True)
st.markdown('<div class="calc-subtitle">Berechne die Masse aus molarer Masse und Stoffmenge</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    M2 = st.number_input("Molare Masse M [g/mol]", key="mol_M2", value=0.0, format="%.4f")
    n2 = st.number_input("Stoffmenge n [mol]", key="mol_n2", value=0.0, format="%.4f")

with col4:
    m2 = M2 * n2
    st.metric("Masse m", f"{m2:.4f} g")

# ---------------------------------------------------
# MOLARE MASSE
# ---------------------------------------------------

st.markdown('<div class="calc-title">3️⃣ Molare Masse berechnen: M = m / n</div>', unsafe_allow_html=True)
st.markdown('<div class="calc-subtitle">Berechne die molare Masse aus Masse und Stoffmenge</div>', unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    m3 = st.number_input("Masse m [g]", key="mol_m3", value=0.0, format="%.4f")
    n3 = st.number_input("Stoffmenge n [mol]", key="mol_n3", value=0.0, format="%.4f")

with col6:
    M3 = m3 / n3 if n3 != 0 else 0.0
    st.metric("Molare Masse M", f"{M3:.4f} g/mol")

st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)

st.info("👉 Zwei Werte eingeben, der dritte wird automatisch berechnet.")

