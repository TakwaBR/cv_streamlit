import streamlit as st

# =========================
# FUNCTION TO DISPLAY SKILLS
# =========================
def run():
    st.header("Compétences")

    # HTML table for displaying skills
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
            <th>Category</th>
            <th>Skills</th>
        </tr>

        <tr>
            <td><b>Omics tools</b></td>
            <td>FastQC, Trimmomatic, HISAT2, StringTie, DIABLO</td>
        </tr>

        <tr>
            <td><b>Structural bioinformatics tools</b></td>
            <td>PyMOL, VMD, Autodock, Vina, PyDock, AMBER, Gromacs</td>
        </tr>

        <tr>
            <td><b>Data analysis tools</b></td>
            <td>Unsupervised methods (PCA, K-means, HCA)<br>
                Supervised methods (neural networks, linear and logistic regressions, CART)
            </td>
        </tr>

        <tr>
            <td><b>Programming languages</b></td>
            <td>Python, Bash, R and SQL, C, Java (basics)</td>
        </tr>

        <tr>
            <td><b>Project management / scientific environments</b></td>
            <td>Conda, Github, computing cluster (SLURM)</td>
        </tr>

        <tr>
            <td><b>Office tools</b></td>
            <td>Microsoft Office, LibreOffice</td>
        </tr>

        <tr>
            <td><b>Soft skills</b></td>
            <td>Teamwork, project management, creativity, interdisciplinary work</td>
        </tr>

        </table>
        """, unsafe_allow_html=True)


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    run()
