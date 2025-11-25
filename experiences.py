import streamlit as st

def run():
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


if __name__ == "__main__":
    run()