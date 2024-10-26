# deployement-turnover-forecast
This repository contains the code and resources for forecasting the 8-week turnover at the store-department level. The goal is to assist store managers in making data-driven mid-term economic decisions.

# Les étapes pour réaliser le deployement-decathlon-turnover-forecast

# 1. Réaliser EDA
- Le code pour construire, entraîner et sauvegarder les résultats d'EDA se trouve dans model/eda.ipynb

# 1. Reprendre le modèle de machine Learning
- Le code pour construire, entraîner et sauvegarder le modèle se trouve dans model

# 2. Créer une API pour le modèle (Fast API)

- Implémenter l'application dans `main.py`
- Utiliser test/test_request.py pour tester l'appel à l'API en local

# 3. Configurer Google Cloud 
- Créer un nouveau projet
- Activer l'API Cloud Run et l'API Cloud Build et Artifact Registory API

## Installer et initialiser Google Cloud SDK
- [Installer Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- configuer le PATH
- Initialiser avec gcloud init


# 4 Créer le fichier requirements.txt
- pip freeze > requirements.txt

# 5. Conteneurisation:  Dockerfile, requirements.txt, .dockerignore
- Créer les fichier Dockerfile, et .dockerignore

# 6. Construction et déploiement dans le Cloud

- Commencez par créer un reppo dans l'artefact registry
- Bien noter les noms de ces variables

PROJECT_ID="decathlon-turnover-forecast" 
REGION="us-central1"           
REPO_NAME="repodecathlonturnoverforecast"    
IMAGE_NAME="image-docker-to"    
IMAGE_TAG="v0"        

#### Construire et soumettre l'image à Google Artifact Registry

- template : gcloud builds submit --tag ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG}

- command : gcloud builds submit --tag us-central1-docker.pkg.dev/decathlon-turnover-forecast/repodecathlonturnoverforecast/image-dev2:v0


#### Déployer l'image sur Google Cloud Run
##### Use UI in GCP Console or Use this command

- template : gcloud run deploy --image ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG} --platform managed --region ${REGION}

# 7 Test
- Tester le code avec `test/test.py` en utilisant le lien disponible après le déploiement

