import requests
URL_BASE = "https://mon-api-ecole.onrender.com/"
def test_route_racine():
	reponse = requests.get(f"{URL_BASE}/")
	assert reponse.status_code == 200
	print("Route racine OK :", reponse.json())
def test_lister_etudiants():
	reponse = requests.get(f"{URL_BASE}/etudiants")
	assert reponse.status_code == 200
	print("Nombre d'étudiants :", len(reponse.json()))
def test_creer_etudiant():
		nouvel_etudiant = {
		"nom": "Sow",
		"prenom": "Aissatou",
		"email": "aissatou.sow@email.com",
		"age": 20
	}
	reponse = requests.post(f"{URL_BASE}/etudiants", json=nouvel_etudiant)
	assert reponse.status_code == 201
	print("Étudiant créé :", reponse.json())
if __name__ == "__main__":
	test_route_racine()
	test_lister_etudiants()
	test_creer_etudiant()
	print("Tous les tests sont passés avec succès.")
