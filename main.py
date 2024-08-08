from pydantic import BaseModel  # Utilisé pour la validation des données
import pandas as pd  # Utilisé pour la manipulation de données
import joblib  # Utilisé pour charger le modèle sauvegardé
from flask import Flask, request, jsonify  # Flask est un micro-framework pour les applications web
from sklearn.base import BaseEstimator, TransformerMixin
from datetime import datetime

class CustomPreprocressing(BaseEstimator, TransformerMixin):
    """
    This class includes all the steps for the preprocessing
    """
    def __init__(self, cat_cols):
        """
        Initialize the class / Can be empty
        """
        self.cat_cols = cat_cols

    def fit(self, X, y=None):
        """
        This method is only created so that the pipeline containing this transformer does not raise an error
        """
        return self

    def transform(self, data):
        """
        Inputs :
          -- data : DataFrame, DataFrame contening all the data needed for the model
        Outputs :
          -- DataFrame, DataFrame prepared for modeling

        """
        data["day_id"] = pd.to_datetime(data["day_id"])
        data["day_id_week"] = data.day_id.dt.isocalendar().week
        data["day_id_month"] = data["day_id"].dt.month
        data["day_id_year"] = data["day_id"].dt.year
        data[self.cat_cols] = data[self.cat_cols].apply(lambda x: x.astype(str))
        return data
    
# Définition du schéma des données d'entrée avec Pydantic
# Cela garantit que les données reçues correspondent aux attentes du modèle
class DonneesEntree(BaseModel):
    but_num_business_unit: int  # store's ID
    dpt_num_department: int  # department's ID
    but_postcode: int  # postal code
    but_latitude: float  # store's latitude
    but_longitude: float  # store's longitude
    but_region_idr_region: int  # region's number
    zod_idr_zone_dgr: int  # zone's number
    day_id : datetime # date

# Charger le modèle
modele = joblib.load('turnover_forecasting_model.pkl')

# Création de l'instance de l'application Flask
app = Flask(__name__)

# Définition de la route racine qui retourne un message de bienvenue
@app.route("/", methods=["GET"])
def accueil():
    """ Endpoint racine qui fournit un message de bienvenue. """
    return jsonify({"message": "Welcome to API for forecasting-decathlon-turnover"})


# Définition de la route pour les prédictions de diabète
@app.route("/predire", methods=["POST"])
def predire():
    """
    Endpoint pour les prédictions en utilisant le modèle chargé.
    Les données d'entrée sont validées et transformées en DataFrame pour le traitement par le modèle.
    """
    if not request.json:
        return jsonify({"erreur": "Aucun JSON fourni"}), 400
    try:
        # Extraction et validation des données d'entrée en utilisant Pydantic
        donnees = DonneesEntree(**request.json)
        donnees_df = pd.DataFrame([donnees.dict()])  # Conversion en DataFrame
        donnees_df["day_id"] = pd.to_datetime(donnees_df["day_id"])
        donnees_df["day_id_week"] = donnees_df.day_id.dt.isocalendar().week
        donnees_df["day_id_month"] = donnees_df["day_id"].dt.month
        donnees_df["day_id_year"] = donnees_df["day_id"].dt.year
        
        # Utilisation du modèle pour prédire et obtenir les probabilités
        predictions = modele.predict(donnees_df)
        
        # Compilation des résultats dans un dictionnaire
        resultats = donnees.dict()
        resultats['prediction'] = int(predictions[0])

        # Renvoie les résultats sous forme de JSON
        return jsonify({"resultats": resultats})
    except Exception as e:
        # Gestion des erreurs et renvoi d'une réponse d'erreur
        return jsonify({"erreur": str(e)}), 400
 
# Point d'entrée pour exécuter l'application
if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Lancement de l'application sur le port 8000 avec le mode debug activé

