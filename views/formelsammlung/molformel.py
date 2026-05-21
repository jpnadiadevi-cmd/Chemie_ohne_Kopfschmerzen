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
# STREAMLIT HOMEPAGE STYLE
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* APP */
.stApp {
    background-color: #fffdf8;
    color: #30303d;
}

/* CONTAINER */
.block-container {
    max-width: 1200px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

/* TITLES */
h1 {
    font-size: 3.2rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.04em;
    color: #30303d !important;
    margin-bottom: 2rem !important;
}

h2 {
    font-size: 2.4rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.03em;
    color: #30303d !important;
}

/* LATEX */
[data-testid="stLatex"] {
    text-align: center;
    margin-top: 2rem;
    margin-bottom: 2rem;
    font-size: 1.3rem;
}

/* DIVIDER */
hr {
    border: none !important;
    border-top: 1px solid #dddddd !important;
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
}

/* LABELS */
label,
[data-testid="stWidgetLabel"] p {
    color: #30303d !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
}

/* INPUTS */
[data-testid="stNumberInput"] input {
    background-color: #f1f3f8 !important;
    border: none !important;
    border-radius: 10px !important;
    color: #30303d !important;
    font-size: 1.1rem !important;
    height: 3rem !important;
}

/* INPUT FOCUS */
[data-testid="stNumberInput"] input:focus {
    box-shadow: 0 0 0 2px rgba(245,191,79,0.35) !important;
}

/* PLUS / MINUS BUTTONS */
[data-testid="stNumberInput"] button {
    background-color: #f1f3f8 !important;
    border: none !important;
    color: #30303d !important;
    box-shadow: none !important;
}

[data-testid="stNumberInput"] button:hover {
    background-color: #fff8ea !important;
    color: #30303d !important;
}

/* METRIC */
[data-testid="stMetric"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
}

[data-testid="stMetricLabel"] {
    color: #30303d !important;
    font-weight: 500 !important;
    font-size: 1rem !important;
}

[data-testid="stMetricValue"] {
    color: #30303d !important;
    font-weight: 500 !important;
    font-size: 3rem !important;
}

/* BUTTONS */
.stButton > button {
    width: 100%;
    background: white !important;
    color: #30303d !important;
    border: 1px solid #e5e5e5 !important;
    border-radius: 14px !important;
    height: 3.3rem !important;
    font-size: 1.05rem !important;
    font-weight: 500 !important;
    transition: 0.2s;
}

.stButton > button:hover {
    border-color: #f5bf4f !important;
    background-color: #fff8ea !important;
    color: #30303d !important;
}

/* INFO BOX */
[data-testid="stAlert"] {
    background-color: #eaf3ff !important;
    border: none !important;
    border-radius: 12px !important;
    color: #0054a6 !important;
}

[data-testid="stAlert"] p {
    font-size: 1rem !important;
    font-weight: 500 !important;
}

/* ANCHOR LINKS AUSBLENDEN */
a.anchor-link {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🧬 Die Molformel")

st.markdown("---")
import streamlit as st

st.markdown("## Berechne Stoffmenge, Masse oder Molare Masse")

st.latex(r"n = \frac{m}{M} \quad | \quad m = M \cdot n \quad | \quad M = \frac{m}{n}")

st.markdown("---")

# ---------------------------------------------------
# INPUTS
# ---------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    n = st.number_input(
        "Stoffmenge n [mol]",
        value=0.0,
        format="%.4f"
    )

with col2:

    m = st.number_input(
        "Masse m [g]",
        value=0.0,
        format="%.4f"
    )

with col3:

    M = st.number_input(
        "Molare Masse M [g/mol]",
        value=0.0,
        format="%.4f"
    )

# ---------------------------------------------------
# BERECHNUNG
# ---------------------------------------------------

result = None
result_label = ""

filled = sum([
    n != 0,
    m != 0,
    M != 0
])

if filled == 2:

    if n == 0 and M != 0:
        result = m / M
        result_label = "Stoffmenge n [mol]"

    elif m == 0:
        result = M * n
        result_label = "Masse m [g]"

    elif M == 0 and n != 0:
        result = m / n
        result_label = "Molare Masse M [g/mol]"

# ---------------------------------------------------
# RESULT
# ---------------------------------------------------

st.markdown("---")

st.subheader("📊 Ergebnis")

if result is not None:

    st.metric(
        result_label,
        f"{result:.4f}"
    )

else:

    st.info("👉 Bitte gib zwei Werte ein, um den dritten zu berechnen.")

# ---------------------------------------------------
# SAVE BUTTON
# ---------------------------------------------------

st.markdown("---")

st.button("💾 Ergebnis ins Logbuch speichern")