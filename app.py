import streamlit as st
import time
import plotly.graph_objects as go
import jeux
import competences
import streamlit.components.v1 as components
import toml

secrets = st.secrets["analytics"]

components.html(
    secrets["ga_snippet"],
    height=0,
    width=0
)

# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="CV – Takwa BEN RADHIA",
    page_icon="📄",
    layout="centered"
)

# =========================
# ANIMATED HEADER
# =========================
header_placeholder = st.empty()
header_text = "👩‍💻 Takwa BEN RADHIA – CV interactif"
display_text = ""

for letter in header_text:
    display_text += letter
    header_placeholder.markdown(
        f"<h2 style='font-size:28px; text-align:center;'>{display_text}</h2>",
        unsafe_allow_html=True
    )
    time.sleep(0.05)

# =========================
# TABS
# =========================
tabs = st.tabs([
    "Accueil", 
    "Formation", 
    "Stages / Expériences", 
    "Omiques",
    "Bioinfo Structurale",
    "IA",
    "Compétences",
    "Langues",
    "Jeux"
])

# =========================
# HOME TAB
# =========================
with tabs[0]:
    st.header("Bienvenue")
    st.markdown("""
Bonjour Madame/Monsieur !  

Je suis **Takwa BEN RADHIA**, ingénieure en bioinformatique.  
Je suis à la recherche d'un poste d'**ingénieur junior en bioinformatique**.  

Passionnée par l’analyse de données omiques, l’intelligence artificielle et la bioinformatique structurale, mon objectif principal est de contribuer à la recherche contre le cancer, tout en étant intéressée par la participation à des projets scientifiques variés et innovants.
    """)

# =========================
# EDUCATION TAB
# =========================
with tabs[1]:
    st.header("Formation")
    st.markdown("""
**HarvardX PH525.5x : Introduction to Bioconductor** (Novembre 2025)  
Formation en ligne suivie en auditeur libre.

**Master Bioinformatique – Université Paris Cité** (2023 – 2025)  
Thèmes abordés : Omiques, Bioinformatique structurale, Intelligence artificielle, Biostatistiques, Analyse de données.  
Programmation : Python, R (bases en Java, C et SQL).

**Licence Sciences de la Vie – Université Paris Cité** (2020 – 2023)  
Spécialisation en bioinformatique en L3.  
Thèmes abordés : Biologie moléculaire et génétique, Biologie cellulaire, Microbiologie, Enzymologie, Biologie végétale, Biologie évolutive, Neurosciences computationnelle, Escape Game moléculaire.
    """)

# =========================
# INTERNSHIPS / EXPERIENCE TAB
# =========================
with tabs[2]:
    st.header("Stages / Expériences")
    
    # 6-month internship
    with st.expander("Stage – Bioinformatique structurale (6 mois) | Janvier 2025 - Juillet 2025"):
        st.markdown("""
Utilisation de modèles de **diffusion en Deep Learning** pour générer des peptides capables de bloquer des **interactions protéines-protéines**.  
- Comparaison des performances de **RFdiffusion** et **ProteinGenerator**  
- Comparaison des modèles génératifs avec l'outil **PepIT**  
- Génération de peptides ciblant la protéine **STRAP** et étude de leur stabilité via **simulations de dynamique moléculaire**  

**Compétences acquises** : Deep Learning génératif, AlphaFold, Dynamique moléculaire, Utilisation de clusters de calcul, Gestion de projet, Rédaction scientifique, Autoformation.
        """)

    # 3-month internship
    with st.expander("Stage – Bioinformatique structurale (3 mois) | Mars 2024 - Juin 2024"):
        st.markdown("""
Étude d'un fragment de la protéine **SOS** en interaction avec la protéine **GRB2**.  
- Simulation du peptide en milieu liquide  
- Simulation avec contraintes RMN issues de données expérimentales  
- Rédaction d'un protocole pour appliquer ces contraintes à une simulation de dynamique moléculaire avec AMBER GPU  
[Protocole disponible sur GitHub](https://github.com/TakwaBR/protocole_AMBER.git)  

**Compétences acquises** : Dynamique moléculaire, Utilisation de GPU, Rédaction scientifique, Rédaction de protocoles.
        """)

    # Escape Game
    with st.expander("Escape Game – L2"):
        st.markdown("""
Maître de jeu de l'Escape Game **"Dosparition"**, conçu avec mes camarades.  
- Conception et organisation de l’Escape Game  
- Gestion des énigmes et coordination des participants  

**Compétences acquises** : Organisation de projet, Créativité, Travail d'équipe, Communication.
        """)

# =========================
# OMICS PROJECTS TAB
# =========================
with tabs[3]:
    st.header("Projets Omiques")

    with st.expander("Projet Multi-omiques | M2"):
        st.markdown("""
Analyse multi-omiques appliquée au diabète de type II (mRNA, protéines, cytokines), réalisées à partir de prélèvements collectés chez des patients sur deux saisons.  
- Visualisation des données protéiques et cytokiniques pour étudier les différences d’expression (**ACP** et **sACP**)  
- Analyse intégrative des trois jeux de données avec **DIABLO** (mixOmics)  

**Compétences acquises** : Analyse omique, Analyse multi-omique, Méthodes d'intégration (DIABLO), Visualisation de données.
        """)

    with st.expander("Projet Transcriptomique | M1"):
        st.markdown("""
Analyse RNA-seq de **biopsies de peau** après application ou non d’une crème.  
- Évaluation de la qualité des reads avec **FastQC** et nettoyage avec **Trimmomatic**  
- Alignement sur le génome **hg38** avec **HISAT2**, quantification avec **StringTie**  
- Identification des gènes différentiellement exprimés et visualisation via **volcano plot**  

**Compétences acquises** : Analyse RNA-seq, Pipeline bioinformatique (FastQC, Trimmomatic, HISAT2, StringTie), Analyse différentielle, Visualisation.
        """)

# =========================
# STRUCTURAL BIOINFORMATICS PROJECTS TAB
# =========================
with tabs[4]:
    st.header("Projets Bioinformatique Structurale")

    # Ribulosamine 3-kinase project
    with st.expander("Étude de la protéine ribulosamine 3-kinase | M2"):
        st.markdown("""
Modélisation, **dynamique moléculaire** et **docking** sur la protéine ribulosamine 3-kinase.  
- Modélisation avec AlphaFold, RosettaFold, MODELLER, I-TASSER, ESMFold  
- Simulation dynamique et analyse des conformations  
- Docking protéine-protéine (HADDOCK, ClusPro) et protéine-ligand (AutoDock, HADDOCK)  

**Compétences acquises** : Modélisation, Dynamique moléculaire, Docking, Analyse d’interactions.
        """)

    # p63 homology modeling
    with st.expander("Prédiction de la structure de la protéine p63 par homologie | M1"):
        st.markdown("""
Modélisation par homologie de la protéine **p63**  
- Identification des domaines connus et recherche des régions manquantes via **BLAST**  
- Construction du modèle 3D avec **MODELLER**  
- Évaluation : carte de Ramachandran, estimation énergétique, structures secondaires  

**Compétences acquises** : Modélisation par homologie, Alignement de séquences, Évaluation structurale.
        """)

# =========================
# AI PROJECTS TAB
# =========================
with tabs[5]:
    st.header("Projets IA")

    # Kaggle competition
    with st.expander('Compétition Kaggle – "RSNA Breast Cancer Detection" | M2'):
        st.markdown("""
Participation en groupe à la compétition Kaggle pour détection du cancer du sein.  
- Analyse et prétraitement des images  
- Conception et entraînement d’un modèle CNN  
- Évaluation : courbe ROC, accuracy, loss  
- Validation croisée (k-fold)  

**Compétences acquises** : Deep Learning, CNN, Évaluation, Travail en équipe.
        """)

    # Image classification project
    with st.expander("Projet de classification d'images | M2"):
        st.markdown("""
Classification d’images bruitées avec Deep Learning  
- Conception et entraînement de modèles DNN et CNN  
- Validation croisée (k-fold)  

**Compétences acquises** : Deep Learning, DNN, CNN, Classification, Évaluation.
        """)

# =========================
# SKILLS TAB
# =========================
with tabs[6]:
    competences.run()

# =========================
# LANGUAGES TAB
# =========================
with tabs[7]:
    st.header("Langues")

    # Language levels
    languages = {
        "Français": 100,
        "Arabe": 90,
        "Anglais": 70,
        "Espagnol": 30
    }

    # Plot language levels
    fig_languages = go.Figure(go.Bar(
        x=list(languages.values()),
        y=list(languages.keys()),
        orientation='h',
        marker=dict(color='mediumpurple')
    ))

    fig_languages.update_layout(
        title="Niveaux de langues",
        xaxis=dict(title="Niveau (%)"),
        yaxis=dict(autorange="reversed"),
        height=300
    )

    st.plotly_chart(fig_languages, use_container_width=True)

# =========================
# GAMES TAB
# =========================
with tabs[8]:
    jeux.run()

# =========================
# FOOTER
# =========================
st.write("---")
st.write("📌 *CV interactif réalisé avec Streamlit. Dernière mise à jour : Novembre 2025.*")
