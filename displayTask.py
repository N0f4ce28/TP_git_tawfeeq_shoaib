# dataTask.py

from dataTask import *

def main():
    choix = input("Que souhaitez-vous faire? (1: Charger une liste de tâches, 2: Créer une liste de tâches): ")

    if choix == "1":
        nom_fichier = input("Entrez le nom du fichier JSON à charger: ")
        taches = charger_dictionnaire_json(nom_fichier)
    elif choix == "2":
        taches = creer_liste_taches()  # Utilisez la fonction de la partie 2
        sauvegarder_dictionnaire_json(taches, "nom_de_votre_fichier.json")  # Remplacez par le nom de votre fichier JSON
        sauvegarder_dictionnaire_json(taches, "nom_de_votre_fichier.json")
    else:
        print("Choix invalide.")

if _name_ == "_main_":
    main()
