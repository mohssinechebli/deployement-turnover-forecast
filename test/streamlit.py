import streamlit as st
import pandas as pd
import requests

# URL de l'API
URL_BASE = 'https://image-dev2-6iliokkj4q-uc.a.run.app/'

def envoyer_pour_prediction(donnees):
    """ Envoie les données à l'API et récupère les prédictions. """
    response = requests.post(f"{URL_BASE}/predire", json=donnees)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.title("MVP - Store x Departement Turnover Forecast")

    # Téléchargement de fichier par l'utilisateur
    fichier = st.file_uploader("Upload your csv data here", type='csv')
    if fichier is not None:
        # Chargement des données
        donnees = pd.read_csv(fichier).head(5)

        # Afficher les données chargées
        st.write("Overview of your data :")
        st.write(donnees)

        if st.button("Launch Forecast"):
            # Prédire chaque ligne des données chargées
            liste = []
            predictions = []
            for _, row in donnees.iterrows():
                donnees_api = row.to_dict()
                resultat = envoyer_pour_prediction(donnees_api)
                if resultat:
                    liste.append(resultat['resultats']["prediction"])
                    predictions.append({'prediction': resultat['resultats']})
                else:
                    predictions.append({'prediction': 'Erreur'})

            # Inserting the new column at index 1 (second position)
            donnees.insert(1, 'Forecasted Turnover', liste)
            # Affichage des résultats
            st.write("Forecasted Turnovers :")
            st.write(donnees)
        else:
            st.write("Back to 'Forecast' button to launch prediction pipeline ;)")

if __name__ == "__main__":
    main()