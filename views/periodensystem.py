import streamlit as st
from data.pse_data import elemente, farben_kategorien

st.set_page_config(
    page_title="Periodensystem",
    page_icon="⚛️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fff8eb 0%, #fffdf8 45%, #ffffff 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero-title {
    background: rgba(255,255,255,0.82);
    border-radius: 26px;
    padding: 1.6rem 2rem;
    box-shadow: 0 12px 35px rgba(0,0,0,0.07);
    border: 1px solid rgba(255,255,255,0.5);
    margin-bottom: 1.5rem;
}

.hero-title h1 {
    margin: 0;
    font-size: 2.4rem;
    color: #30303d;
}

.hero-title p {
    margin-top: 0.7rem;
    font-size: 1.05rem;
    color: #5b5b68;
}

.section-title {
    font-size: 1.7rem;
    font-weight: 750;
    color: #30303d;
    margin-top: 1.4rem;
    margin-bottom: 0.7rem;
}

.legend-box {
    padding: 0.7rem 0.8rem;
    border-radius: 14px;
    text-align: center;
    font-size: 0.85rem;
    font-weight: 650;
    border: 1px solid rgba(0,0,0,0.25);
    box-shadow: 0 5px 14px rgba(0,0,0,0.05);
}

.element-card {
    width: 100%;
    min-height: 58px;
    padding: 14px 4px;
    border-radius: 12px;
    text-align: center;
    font-weight: 800;
    font-size: 1rem;
    border: 1.5px solid rgba(0,0,0,0.65);
    box-shadow: 0 5px 12px rgba(0,0,0,0.08);
    transition: all 0.2s ease;
}

.element-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 9px 20px rgba(0,0,0,0.13);
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #e2d7c1;
    background: white;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    background: #fff1c9;
    border-color: #f0c96a;
}

.detail-card {
    background: rgba(255,255,255,0.85);
    border-radius: 24px;
    padding: 1.5rem;
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
    border: 1px solid rgba(255,255,255,0.5);
    margin-top: 1rem;
}

.big-symbol {
    padding: 2rem;
    border-radius: 22px;
    text-align: center;
    font-size: 4rem;
    font-weight: 900;
    border: 2px solid rgba(0,0,0,0.6);
    box-shadow: 0 12px 25px rgba(0,0,0,0.12);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-title">
    <h1>⚛️ Interaktives Periodensystem</h1>
    <p>Alle 118 Elemente übersichtlich dargestellt. Klicke auf ein Element, um Details wie Atommasse, Gruppe, Periode und Elektronegativität zu sehen.</p>
</div>
""", unsafe_allow_html=True)

elemente_sortiert = sorted(elemente, key=lambda x: x["ordnungszahl"])

st.markdown('<div class="section-title">Periodensystem mit allen 118 Elementen</div>', unsafe_allow_html=True)
st.write("**Kategorien-Legende:**")

legend_cols = st.columns(len(farben_kategorien))

for idx, (kategorie, farbe) in enumerate(farben_kategorien.items()):
    with legend_cols[idx]:
        st.markdown(
            f"""
            <div class="legend-box" style="background-color:{farbe};">
                {kategorie}
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")
st.write("**Klicke auf ein Element:**")

element_grid = {}

for el in elemente_sortiert:
    periode = el["periode"]
    gruppe = el["gruppe"]

    if periode not in element_grid:
        element_grid[periode] = {}

    element_grid[periode][gruppe] = el

for periode in range(1, 8):
    cols = st.columns(18)

    if periode in element_grid:
        for gruppe, el in element_grid[periode].items():
            col_idx = gruppe - 1

            with cols[col_idx]:
                farbe = farben_kategorien.get(el["kategorie"], "#FFFFFF")

                st.markdown(
                    f"""
                    <div class="element-card" style="background-color:{farbe};">
                        {el["symbol"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    "🔍",
                    key=f"btn_{el['ordnungszahl']}",
                    help=f"Klicke für {el['name']}"
                ):
                    st.session_state["selected_element"] = el

st.markdown("---")

if "selected_element" in st.session_state:
    el = st.session_state["selected_element"]
    farbe = farben_kategorien.get(el["kategorie"], "#FFFFFF")

    st.markdown('<div class="detail-card">', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader(f"⚛️ {el['name']} ({el['symbol']})")

        col_info1, col_info2 = st.columns(2)

        with col_info1:
            st.metric("Ordnungszahl", el["ordnungszahl"])
            st.metric("Atommasse", f"{el['atommasse']} u")
            st.metric("Periode", el["periode"])

        with col_info2:
            st.metric("Gruppe", el["gruppe"])
            st.metric("Kategorie", el["kategorie"])

            if el["elektronegativität"] is not None:
                st.metric("Elektronegativität", f"{el['elektronegativität']:.2f}")
            else:
                st.metric("Elektronegativität", "N/A")

    with col2:
        st.markdown(
            f"""
            <div class="big-symbol" style="background-color:{farbe};">
                {el['symbol']}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("❌ Element abwählen"):
        del st.session_state["selected_element"]
        st.rerun()

else:
    st.info("👆 Klicke auf ein Element, um detaillierte Informationen zu sehen!")