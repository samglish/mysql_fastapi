# app_frontend.py
import tkinter as tk
from tkinter import messagebox, ttk
import requests

URL_BASE = "https://mon-api-ecole.onrender.com"
# Pour tester en local, remplacer par : "http://127.0.0.1:8000"


class ApplicationEcole(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des étudiants — Client FastAPI")
        self.geometry("600x450")

        self.creer_formulaire()
        self.creer_tableau()
        self.charger_etudiants()

    def creer_formulaire(self):
        cadre = tk.Frame(self, padx=10, pady=10)
        cadre.pack(fill="x")

        tk.Label(cadre, text="Nom").grid(row=0, column=0)
        tk.Label(cadre, text="Prénom").grid(row=0, column=1)
        tk.Label(cadre, text="Email").grid(row=0, column=2)
        tk.Label(cadre, text="Âge").grid(row=0, column=3)

        self.champ_nom = tk.Entry(cadre, width=12)
        self.champ_prenom = tk.Entry(cadre, width=12)
        self.champ_email = tk.Entry(cadre, width=18)
        self.champ_age = tk.Entry(cadre, width=6)

        self.champ_nom.grid(row=1, column=0, padx=3)
        self.champ_prenom.grid(row=1, column=1, padx=3)
        self.champ_email.grid(row=1, column=2, padx=3)
        self.champ_age.grid(row=1, column=3, padx=3)

        bouton_ajouter = tk.Button(
            cadre, text="Ajouter l'étudiant", command=self.ajouter_etudiant
        )
        bouton_ajouter.grid(row=1, column=4, padx=10)

    def creer_tableau(self):
        colonnes = ("id", "nom", "prenom", "email", "age")
        self.tableau = ttk.Treeview(self, columns=colonnes, show="headings")

        for colonne in colonnes:
            self.tableau.heading(colonne, text=colonne.capitalize())
            self.tableau.column(colonne, width=100)

        self.tableau.pack(fill="both", expand=True, padx=10, pady=10)

        bouton_supprimer = tk.Button(
            self, text="Supprimer la sélection", command=self.supprimer_etudiant
        )
        bouton_supprimer.pack(pady=5)

        bouton_actualiser = tk.Button(
            self, text="Actualiser la liste", command=self.charger_etudiants
        )
        bouton_actualiser.pack(pady=5)

    def charger_etudiants(self):
        # Vide le tableau avant de le remplir à nouveau
        for ligne in self.tableau.get_children():
            self.tableau.delete(ligne)

        try:
            reponse = requests.get(f"{URL_BASE}/etudiants")
            reponse.raise_for_status()
            etudiants = reponse.json()

            for etudiant in etudiants:
                self.tableau.insert("", "end", values=(
                    etudiant["id"],
                    etudiant["nom"],
                    etudiant["prenom"],
                    etudiant["email"],
                    etudiant.get("age", "")
                ))
        except requests.exceptions.RequestException as erreur:
            messagebox.showerror("Erreur de connexion", str(erreur))

    def ajouter_etudiant(self):
        donnees = {
            "nom": self.champ_nom.get(),
            "prenom": self.champ_prenom.get(),
            "email": self.champ_email.get(),
            "age": int(self.champ_age.get()) if self.champ_age.get() else None
        }

        if not donnees["nom"] or not donnees["prenom"] or not donnees["email"]:
            messagebox.showwarning("Champs manquants", "Nom, prénom et email sont obligatoires.")
            return

        try:
            reponse = requests.post(f"{URL_BASE}/etudiants", json=donnees)
            if reponse.status_code == 201:
                messagebox.showinfo("Succès", "Étudiant ajouté avec succès.")
                self.charger_etudiants()
                self.champ_nom.delete(0, tk.END)
                self.champ_prenom.delete(0, tk.END)
                self.champ_email.delete(0, tk.END)
                self.champ_age.delete(0, tk.END)
            else:
                messagebox.showerror("Erreur", reponse.json().get("detail", "Erreur inconnue"))
        except requests.exceptions.RequestException as erreur:
            messagebox.showerror("Erreur de connexion", str(erreur))

    def supprimer_etudiant(self):
        selection = self.tableau.selection()
        if not selection:
            messagebox.showwarning("Aucune sélection", "Sélectionnez un étudiant à supprimer.")
            return

        valeurs = self.tableau.item(selection[0], "values")
        etudiant_id = valeurs[0]

        confirmation = messagebox.askyesno(
            "Confirmation", f"Supprimer l'étudiant {valeurs[1]} {valeurs[2]} ?"
        )
        if confirmation:
            try:
                reponse = requests.delete(f"{URL_BASE}/etudiants/{etudiant_id}")
                if reponse.status_code == 200:
                    self.charger_etudiants()
                else:
                    messagebox.showerror("Erreur", "Impossible de supprimer cet étudiant.")
            except requests.exceptions.RequestException as erreur:
                messagebox.showerror("Erreur de connexion", str(erreur))


if __name__ == "__main__":
    application = ApplicationEcole()
    application.mainloop()
