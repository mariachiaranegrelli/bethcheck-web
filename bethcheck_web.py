import streamlit as st

st.set_page_config(page_title="BethCheck", layout="wide")

st.image("https://i.imgur.com/0Hf2TxJ.png", width=160)
st.title("BethCheck - Classificazione Bethesda Citologia Tiroidea")

st.markdown("### Seleziona le caratteristiche del campione:")

# Checklist sezioni
adeguatezza = st.multiselect("Adeguatezza", [
    "< 6 gruppi con 10 cellule",
    "Campione acellulato",
    "Liquido cistico",
    "Campione ipercellulato",
    "Adeguato"
])

colloide = st.multiselect("Colloide", [
    "Assente", "Scarsa", "Moderata", "Abbondante"
])

tireociti = st.multiselect("Tireociti", [
    "Nuclei chiarificati",
    "Grooves",
    "Pseudoinclusi",
    "Nucleoli evidenti",
    "Plasmocitoidi",
    "Cromatina sale e pepe",
    "Binucleazione",
    "Code citoplasmatiche"
])

architettura = st.multiselect("Architettura", [
    "Microfollicolare",
    "Macrofollicolare",
    "Papille",
    "Aggregati irregolari"
])

psammoma = st.radio("Corpi psammomatosi", ["Assenti", "Presenti"])
atipie = st.multiselect("Tipo di atipie", [
    "Atipia nucleare lieve",
    "Atipie nucleari estese",
    "Atipie architetturali estese"
])

# Logica base
st.markdown("---")
if st.button("Suggerisci Categoria Bethesda"):
    if "Pseudoinclusi" in tireociti and "Papille" in architettura:
        categoria = "Categoria VI - Maligno (Papillare)"
    elif "Microfollicolare" in architettura and not atipie:
        categoria = "Categoria IV - Neoplasia follicolare"
    elif "Liquido cistico" in adeguatezza and not atipie:
        categoria = "Categoria Ic - Inadeguato (cistico)"
    elif "Adeguato" in adeguatezza and "Abbondante" in colloide and not atipie:
        categoria = "Categoria II - Benigno"
    elif atipie:
        categoria = "Categoria III - AUS/FLUS"
    elif "Campione acellulato" in adeguatezza:
        categoria = "Categoria I - Non Diagnostico"
    else:
        categoria = "Valutazione non determinata"

    st.success(f"**Categoria Bethesda suggerita:** {categoria}")
