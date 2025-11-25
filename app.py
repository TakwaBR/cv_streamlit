import streamlit as st
import time
import plotly.graph_objects as go
import jeux
import competences
import experiences
import projets

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
    "Projets",
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

Je suis **Takwa BEN RADHIA**, ingénieure en bioinformatique et je suis à la recherche d'un poste junior.  

Passionnée par l’analyse de données omiques, l’intelligence artificielle et la bioinformatique structurale, je souhaite mettre mes compétences au service de la recherche biomédicale. Mon objectif est de contribuer à la compréhension et à la lutte contre des maladies complexes, tel que le cancer, ainsi qu’au développement de nouvelles approches thérapeutiques.
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
    experiences.run()
    

# =========================
# OMICS PROJECTS TAB
# =========================
with tabs[3]:
    projets.run()

# =========================
# SKILLS TAB
# =========================
with tabs[4]:
    competences.run()

# =========================
# LANGUAGES TAB
# =========================
with tabs[5]:
    st.header("Langues")

    # Language levels
    languages = {
        "Français": "Courant",
        "Arabe": "Courant",
        "Anglais": "B2",
        "Espagnol": "A2"
    }

    # Mapping CEFR levels to numeric values for plotting
    level_mapping = {"A1": 1, "A2": 2, "B1": 3, "B2": 4, "C1": 5, "C2": 6, "Courant": 6.5}
    numeric_levels = [level_mapping[level] for level in languages.values()]

    # Plot language levels
    fig_languages = go.Figure(go.Bar(
        x=numeric_levels,
        y=list(languages.keys()),
        orientation='h',
        marker=dict(color='mediumpurple'),
        text=list(languages.values()),  # Show actual label
        textposition='inside'
    ))

    fig_languages.update_layout(
        title="Niveaux de langues",
        xaxis=dict(
            title="Niveau",
            tickvals=[1, 2, 3, 4, 5, 6, 6.5],
            ticktext=["A1", "A2", "B1", "B2", "C1", "C2", "Courant"]
        ),
        yaxis=dict(autorange="reversed"),
        height=300
    )

    st.plotly_chart(fig_languages, use_container_width=True)

# =========================
# GAMES TAB
# =========================
with tabs[6]:
    jeux.run()

# =========================
# FOOTER
# =========================
st.write("---")
st.write("📌 *CV interactif réalisé avec Streamlit. Dernière mise à jour : Novembre 2025.*")
