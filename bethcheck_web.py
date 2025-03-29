import streamlit as st

# Impostiamo il titolo della pagina e l'immagine del logo
st.set_page_config(page_title="BethCheck", layout="wide")
st.image("Logo.png", width=300)

# Stile personalizzato per migliorare l'aspetto
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #8e44ad; 
            color: white;
            font-size: 16px;
            padding: 12px 20px;
            border-radius: 12px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #732d91;
        }
        .stMultiSelect>div>div>div>div>div {
            background-color: #f4e6f9 !important;
            border-radius: 8px;
            color: black !important;
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
            background-color: #f4e6f9;
        }
        .stRadio>div>div>div>div>div>div {
            background-color: #f4e6f9;
            border-radius: 8px;
            padding: 10px;
        }
        .stMarkdown {
            font-size: 18px;
            color: #4b0082;
            font-weight: bold;
        }
        .result-box {
            background-color: #f3e6ff;
            padding: 20px;
            border-radius: 15px;
            border: 4px solid #b266ff;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #4B0082;
            margin-top: 40px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        }
        .result-box b {
            color: #732d91;
        }
    </style>
""", unsafe_allow_html=True)

# Titolo dell'app
st.title("BethCheck - Classificazione Bethesda Citologia Tiroidea")

# Sezione per la selezione delle caratteristiche del campione
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

# Funzione di reset
def reset_fields():
    st.session_state.adeguatezza = []
    st.session_state.colloide = []
    st.session_state.thyrocytes = []
    st.session_state.architettura = []
    st.session_state.atipie = []
    st.session_state.psammoma = "assenti"

    st.experimental_rerun()

# Bottone per suggerire la categoria
st.markdown("---")
col1, col2 = st.columns([1, 1])
with col1:
    suggerisci = st.button("Suggerisci Categoria Bethesda")
with col2:
    reset = st.button("Resetta Campi", on_click=reset_fields)

# Funzione per determinare la categoria
if suggerisci:
    categoria = "Valutazione non determinata"
    descrizione = "Nessuna categoria determinata"
    raccomandazione = "Nessuna raccomandazione"
    
    # Liste lower-case per confronti robusti
    adeguatezza_lower = [a.lower() for a in adeguatezza]
    colloide_lower = [c.lower() for c in colloide]
    thyrocytes_lower = [t.lower() for t in thyrocytes]
    architettura_lower = [a.lower() for a in architettura]
    atipie_lower = [a.lower() for a in atipie]
    psammoma_lower = psammoma.lower()

    # Categoria I - Non diagnostico
    if ("< di 6 gruppi con 10 cellule" in adeguatezza_lower or 
        "liquido cistico" in adeguatezza_lower or 
        "campione acellulato" in adeguatezza_lower or 
        "solo materiale ematico" in adeguatezza_lower or 
        "solo gel per ecografia" in adeguatezza_lower or 
        "assenza di cellule target" in adeguatezza_lower):
        
        if any(char in thyrocytes_lower for char in [
            "chiarificazione nucleare", "grooves", "pseudoinclusi", 
            "nucleoli evidenti", "aspetto oncocitario", "plasmocitoidi", 
            "cromatina sale e pepe", "binucleazione", "marcata monotonia", 
            "macro e microfollicolare", "microfollicolare", "honey-comb", 
            "sovrapposizione nucleare", "papille", "lembi solidi", 
            "aggregati irregolari", "cellule scoese", "corpi psammomatosi"]):
            categoria = "Categoria II - Non Inadeguato"
            descrizione = "Non inadeguato: sono presenti caratteristiche atipiche"
            raccomandazione = "Ripetere FNAC sotto guida ecografica"
        else:
            categoria = "Categoria I - Inadeguato"
            descrizione = "Categoria I: Inadeguato. Campione insufficiente per diagnosi."
            raccomandazione = "Ripetere FNAC sotto guida ecografica"

    # Categoria II - Benigno
    elif "macrofollicolare" in architettura_lower or "micro e macrofollicolare" in architettura_lower:
        if "nuclei piccoli (uguali a linfocita)" in thyrocytes_lower or "nuclei tondeggianti" in thyrocytes_lower or "nuclei scuri, contorni regolari" in thyrocytes_lower:
            categoria = "Categoria II - Benigno"
            descrizione = "Categoria II: Benigno. ROM:0–3%."
            raccomandazione = "Follow-up clinico e ecografico"

    # Categoria IV - Neoplasia follicolare
    elif "aspetto oncocitario" in thyrocytes_lower:
        categoria = "Categoria IV - Neoplasia follicolare"
        descrizione = "Categoria IV: Neoplasia follicolare. ROM: 50%."
        raccomandazione = "Test molecolari, Lobectomia chirurgica"

    # Altre categorie (esempio per categoria V e VI)
    # Categoria V - Sospetto per malignità
    elif "grooves" in thyrocytes_lower or "pseudoinclusi" in thyrocytes_lower:
        categoria = "Categoria V - Sospetto per malignità"
        descrizione = "Categoria V: Sospetto per malignità. ROM: 81%."
        raccomandazione = "Rimozione chirurgica (resezione)"

    # Categoria VI - Maligno
    elif "papille" in architettura_lower:
        categoria = "Categoria VI - Maligno"
        descrizione = "Categoria VI: Maligno. ROM: 98%."
        raccomandazione = "Rimozione chirurgica totale"

    # Visualizzazione dei risultati
    st.markdown(f"""
    <div class="result-box">
        ✅ Categoria Bethesda suggerita: {categoria} <br><br>
        <b>Descrizione:</b> {descrizione} <br>
        <b>Raccomandazione:</b> {raccomandazione}
    </div>
    """, unsafe_allow_html=True)

