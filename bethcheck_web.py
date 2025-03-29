import streamlit as st

st.set_page_config(page_title="BethCheck", layout="wide")
st.image("https://i.imgur.com/0Hf2TxJ.png", width=160)
st.title("BethCheck - Classificazione Bethesda Citologia Tiroidea")

st.markdown("### Seleziona le caratteristiche del campione:")

# Adeguatezza
adeguatezza = st.multiselect("Adeguatezza", [
    "< di 6 gruppi con 10 cellule",
    "Campione acellulato",
    "Liquido cistico",
    "Campione ipercellulato",
    "Adeguato (≥6 gruppi con ≥10 cellule)",
    "Cellule mal valutabili / artefatti",
    "Solo sangue",
    "Solo gel ecografico",
    "Assenza di cellule target"
])

# Colloide
colloide = st.multiselect("Colloide", [
    "Assente", "Scarsa", "Moderata", "Abbondante (in zolle o acquosa)"
])

# Tireociti
thyrocytes = st.multiselect("Tireociti", [
    "nuclei piccoli (uguali a linfocita)",
    "nuclei tondeggianti",
    "nuclei ovalari",
    "nuclei chiarificati",
    "nuclei scuri, contorni regolari",
    "grooves focali",
    "grooves estesi",
    "pseudoinclusi 1",
    "pseudoinclusi >1",
    "nucleoli evidenti focali",
    "nucleoli evidenti estesi",
    "aspetto oncocitario",
    "plasmocitoidi",
    "cromatina sale e pepe",
    "binucleazione",
    "marcata monotonia associata ad atipia",
    "code citoplasmatiche"
])

# Architettura
architettura = st.multiselect("Architettura", [
    "macrofollicolare",
    "microfollicolare",
    "macro e microfollicolare",
    "honey-comb (> benigno)",
    "sovrapposizione nucleare (> maligno)",
    "papille",
    "lembi solidi",
    "aggregati irregolari",
    "cellule scoese"
])

# Psammoma
psammoma = st.radio("Corpi psammomatosi", ["presenti", "assenti"])

# Tipo di atipie
atipie = st.multiselect("Tipo di Atipie", [
    "poche cellule con nucleo aumentato",
    "atipia nucleare lieve",
    "atipia architetturale lieve",
    "atipie nucleari estese",
    "atipie architetturali estese"
])

# Suggerimento categoria
st.markdown("---")
if st.button("Suggerisci Categoria Bethesda"):
    categoria = "Valutazione non determinata"

    if "pseudoinclusi >1" in thyrocytes:
        categoria = "Categoria VI - Maligno (Papillare)"
    elif "grooves estesi" in thyrocytes and "nuclei chiarificati" in thyrocytes:
        categoria = "Categoria V - Sospetto Papillare"
    elif any(t in thyrocytes for t in ["plasmocitoidi", "cromatina sale e pepe", "code citoplasmatiche", "binucleazione"]):
        categoria = "Categoria VI - Maligno (Sospetto Midollare)"
    elif "papille" in architettura:
        categoria = "Categoria V - Sospetto Papillare"
    elif "microfollicolare" in architettura and not atipie:
        categoria = "Categoria IV - Neoplasia follicolare"
    elif "macrofollicolare" in architettura and "nuclei piccoli (uguali a linfocita)" in thyrocytes and "nuclei scuri, contorni regolari" in thyrocytes and "Abbondante (in zolle o acquosa)" in colloide and not atipie:
        categoria = "Categoria II - Benigno"
    elif any(a in atipie for a in ["poche cellule con nucleo aumentato", "atipia nucleare lieve", "atipia architetturale lieve"]):
        categoria = "Categoria III - AUS/FLUS"
    elif "liquido cistico" in [a.lower() for a in adeguatezza] and not atipie:
        categoria = "Categoria Ic - Inadeguato (cistico)"
    elif any(a in adeguatezza for a in ["< di 6 gruppi con 10 cellule", "Campione acellulato", "Solo sangue", "Solo gel ecografico", "Assenza di cellule target", "Cellule mal valutabili / artefatti"]) and not thyrocytes:
        categoria = "Categoria I - Non Diagnostico"

    st.success(f"**Categoria Bethesda suggerita:** {categoria}")
