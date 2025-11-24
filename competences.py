import streamlit as st

# =========================
# # FUNCTION TO DISPLAY SKILLS
# =========================
def run():
    st.header("Compétences")

    # Tableau HTML pour afficher les compétences
    st.markdown("""
        <style>
        table.cv-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
            font-size: 15px;
        }
        .cv-table th {
            background-color: #f2f2f2;
            color: #000;
            padding: 10px;
            text-align: left;
            border-bottom: 2px solid #ddd;
        }
        .cv-table td {
            padding: 10px;
            vertical-align: top;
            border-bottom: 1px solid #eee;
        }
        </style>

        <table class="cv-table">
        <tr>
            <th>Catégorie</th>
            <th>Compétences</th>
        </tr>

        <tr>
            <td><b>Outils omiques</b></td>
            <td>FastQC, Trimmomatic, HISAT2, StringTie, DIABLO</td>
        </tr>

        <tr>
            <td><b>Outils en bioinformatique structurale</b></td>
            <td>PyMOL, VMD, Autodock, Vina, PyDock, AMBER, Gromacs</td>
        </tr>

        <tr>
            <td><b>Outils d’analyse de données</b></td>
            <td>Méthodes non supervisées (ACP, K-means, HCA)<br>
                Méthodes supervisées (réseaux de neurones, régressions linéaire et logistique, CART)
            </td>
        </tr>

        <tr>
            <td><b>Langages de programmation</b></td>
            <td>Python, Bash, R et SQL, C, Java (notions)</td>
        </tr>

        <tr>
            <td><b>Environnements / gestion de projets scientifiques</b></td>
            <td>Conda, Github, cluster de calcul (SLURM)</td>
        </tr>

        <tr>
            <td><b>Outils bureautiques</b></td>
            <td>Suite Office, LibreOffice</td>
        </tr>

        <tr>
            <td><b>Compétences transversales</b></td>
            <td>Travail en équipe, gestion de projet, créativité, pluridisciplinarité</td>
        </tr>

        </table>
        """, unsafe_allow_html=True)


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    run()
