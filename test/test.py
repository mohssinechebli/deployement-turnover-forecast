import requests
test_scope = "local"  #cloud or local

# URL de base de l'API
url_base_dict = {   "local":'http://127.0.0.1:8000',
                    "cloud":'https://image3servicename-6iliokkj4q-uc.a.run.app'}
url_base = url_base_dict[test_scope]

# Test du endpoint d'accueil
response = requests.get(f"{url_base}/")
print("Réponse du endpoint d'accueil:", response.text)

# Test du endpoint de prédiction
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
response = requests.post(f"{url_base}/predire", json=donnees_predire) 
print("Réponse du endpoint de prédiction:", response.text)