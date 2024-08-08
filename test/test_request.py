import requests

# URL de base de l'API
url_base = 'http://127.0.0.1:8000'

# Test du endpoint d'accueil
response = requests.get(f"{url_base}/")
print("Réponse du endpoint d'accueil:", response.text)

# Données d'exemple pour la prédiction
donnees_predire = {
            "but_num_business_unit":100,
            "dpt_num_department":112,
            "but_postcode":75000,
            "but_latitude":43.34,
            "but_longitude":34.83,
            "but_region_idr_region":23,
            "zod_idr_zone_dgr":10,
            "day_id":2017-11-25
}
# Test du endpoint de prédiction
response = requests.post(f"{url_base}/predire", json=donnees_predire)  # Removed the trailing slash
print("Réponse du endpoint de prédiction:", response.text)