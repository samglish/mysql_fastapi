# test_api.py
import requests
import pytest
URL_BASE = "https://mon-api-ecole.onrender.com"
def test_route_racine():
	reponse = requests.get(f"{URL_BASE}/")
	assert reponse.status_code == 200
def test_lister_etudiants_retourne_une_liste():
	reponse = requests.get(f"{URL_BASE}/etudiants")
	assert isinstance(reponse.json(), list)
def test_etudiant_introuvable_retourne_404():
	reponse = requests.get(f"{URL_BASE}/etudiants/999999")
	assert reponse.status_code == 404
