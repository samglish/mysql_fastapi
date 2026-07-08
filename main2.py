# main.py
from fastapi import FastAPI

# Créer l'application FastAPI
app = FastAPI()

# Route GET sur la racine /
@app.get('/')
def accueil():
    return {'message': 'Bienvenue dans mon API !'}

# Route avec paramètre dans l'URL
@app.get('/bonjour/{nom}')
def saluer(nom: str):
    return {'message': f'Bonjour {nom} !'}

# Route avec paramètre de requête (?age=25)
@app.get('/etudiants')
def liste_etudiants(age: int = None, limit: int = 10):
    return {'age_filtre': age, 'limite': limit}