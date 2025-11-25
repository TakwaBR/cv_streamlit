import streamlit as st

def run():
    st.header("Projets")

    # =========================
    # OMICS PROJECTS
    # =========================
    with st.expander("Projets Omiques"):
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

    with st.expander("Projets Bioinformatique Structurale"):
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

    with st.expander("Projets Intelligence Artificielle"):
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


if __name__ == "__main__":
    run()