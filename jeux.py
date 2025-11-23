import streamlit as st
import random

# =============================
#         MAIN GAME MODULE
# =============================

def run():
    st.header("🎮 Espace Jeux – Pour souffler un peu entre 2 CV !")

    # Dropdown to select the mini-game
    game_choice = st.selectbox(
        "Choisis ton mini-jeu :",
        ["-- Sélectionner --", "Pierre-Feuille-Ciseaux", "Nombre Secret"]
    )

    # =============================
    #    1) Pierre-Feuille-Ciseaux
    # =============================
    if game_choice == "Pierre-Feuille-Ciseaux":
        st.subheader("✊ ✋ ✌️ Pierre-Feuille-Ciseaux !")
        player_choice = st.radio("Ton choix :", ["Pierre", "Feuille", "Ciseaux"])
        if st.button("Jouer", key="pfc_jouer"):
            computer_choice = random.choice(["Pierre", "Feuille", "Ciseaux"])
            st.write(f"🤖 L’ordinateur a choisi : **{computer_choice}**")
            if player_choice == computer_choice:
                st.info("Égalité !")
            elif (
                (player_choice == "Pierre" and computer_choice == "Ciseaux") or
                (player_choice == "Feuille" and computer_choice == "Pierre") or
                (player_choice == "Ciseaux" and computer_choice == "Feuille")
            ):
                st.success("🎉 Tu as gagné !")
            else:
                st.error("😢 Tu as perdu...")

    # =============================
    #       2) Nombre Secret
    # =============================
    if game_choice == "Nombre Secret":
        st.subheader("🔢 Le Jeu du Nombre Secret")

        # Initialize secret number and attempts
        if "secret_number" not in st.session_state:
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0

        # Input field for the player's guess
        player_guess = st.number_input(
            "Devine un nombre entre 1 et 100 :",
            1, 100, step=1,
            key="number_input"
        )

        # Button to test the guess
        if st.button("Tester", key="number_check"):
            st.session_state.attempts += 1
            if player_guess < st.session_state.secret_number:
                st.warning("🔼 Trop petit !")
            elif player_guess > st.session_state.secret_number:
                st.warning("🔽 Trop grand !")
            else:
                st.success(f"🎉 Bravo ! Tu as deviné le nombre en {st.session_state.attempts} coups !")
                # Button to reset the game
                if st.button("Rejouer", key="number_reset"):
                    st.session_state.secret_number = random.randint(1, 100)
                    st.session_state.attempts = 0

# =============================
#           MAIN
# =============================
if __name__ == "__main__":
    run()
