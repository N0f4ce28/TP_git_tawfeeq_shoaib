# Modifier le fichier taskTool.py pour inclure la fonction d'enregistrement JSON

# taskTool.py

import json

# Ancienne code...

def sauvegarder_dictionnaire_json(dictionnaire, nom_fichier):
    """
    Enregistre le dictionnaire dans un fichier JSON.

    Args:
        dictionnaire (dict): Le dictionnaire à enregistrer.
        nom_fichier (str): Le nom du fichier JSON.
    """
    with open(nom_fichier, 'w') as fichier:
        json.dump(dictionnaire, fichier)

class Dictionary:
    def init(self):
        self.words = {}

    def add_word(self, key, value):
        if key in self.words:
            print(f"The key '{key}' already exists in the dictionary.")
        else:
            self.words[key] = value
            print(f"The word '{key}' has been added to the dictionary.")

    def update_word(self, key, new_value):
        if key in self.words:
            self.words[key] = new_value
            print(f"The word '{key}' has been updated in the dictionary.")
        else:
            print(f"The key '{key}' does not exist in the dictionary.")

# Modifier le fichier taskTool.py pour inclure la fonction de suppression de la base de données

# taskTool.py

# Votre code existant ici...

def supprimer_base_de_donnees():
    """
    Supprime la base de données (le fichier JSON) s'il existe.
    """
    nom_fichier = "nom_de_votre_fichier.json"  # Remplacez par le nom de votre fichier JSON
    try:
        os.remove(nom_fichier)
        print(f"La base de données {nom_fichier} a été supprimée.")
    except FileNotFoundError:
        print("La base de données n'existe pas.")

# Votre code existant ici...
    def remove_word(self, key):
        if key in self.words:
            del self.words[key]
            print(f"The word '{key}' has been removed from the dictionary.")
        else:
            print(f"The key '{key}' does not exist in the dictionary.")

    def display_words(self):
        print("Current words in the dictionary:")
        for key, value in self.words.items():
            print(f"{key}: {value}")


# Create a Dictionary object
my_dict = Dictionary()

# Add words to the dictionary
my_dict.add_word('apple', 'A fruit')
my_dict.add_word('banana', 'A yellow fruit')
my_dict.add_word('orange', 'An orange fruit')

# Update a word in the dictionary
my_dict.update_word('banana', 'A yellow fruit with a long tail')

# Remove a word from the dictionary
my_dict.remove_word('orange')

# Display the words in the dictionary
my_dict.display_words()

# Modifier le fichier taskTool.py pour inclure la fonction de suppression de la base de données

# taskTool.py

# Votre code existant ici...

def supprimer_base_de_donnees():
    """
    Supprime la base de données (le fichier JSON) s'il existe.
    """
    nom_fichier = "nom_de_votre_fichier.json"  # Remplacez par le nom de votre fichier JSON
    try:
        os.remove(nom_fichier)
        print(f"La base de données {nom_fichier} a été supprimée.")
    except FileNotFoundError:
        print("La base de données n'existe pas.")

# Votre code existant ici...
class Dictionary:
    def init(self):
        self.words = {}

    def add_word(self, key, value):
        if key in self.words:
            print(f"The key '{key}' already exists in the dictionary.")
        else:
            self.words[key] = value
            print(f"The word '{key}' has been added to the dictionary.")

    def update_word(self, key, new_value):
        if key in self.words:
            self.words[key] = new_value
            print(f"The word '{key}' has been updated in the dictionary.")
        else:
            print(f"The key '{key}' does not exist in the dictionary.")

    def remove_word(self, key):
        if key in self.words:
            del self.words[key]
            print(f"The word '{key}' has been removed from the dictionary.")
        else:
            print(f"The key '{key}' does not exist in the dictionary.")

    def display_words(self):
        print("Current words in the dictionary:")
        for key, value in self.words.items():
            print(f"{key}: {value}")


# Create a Dictionary object
my_dict = Dictionary()

# Add words to the dictionary
my_dict.add_word('apple', 'A fruit')
my_dict.add_word('banana', 'A yellow fruit')
my_dict.add_word('orange', 'An orange fruit')

# Update a word in the dictionary
my_dict.update_word('banana', 'A yellow fruit with a long tail')

# Remove a word from the dictionary
my_dict.remove_word('orange')

# Display the words in the dictionary
my_dict.display_words()

# Ajouter et valider les modifications
git add taskTool.py
git commit -m "Ajouter la fonction pour charger un fichier JSON dans taskTool.py"

# Revenir à la branche bdd
git checkout bdd

# Ajouter et valider les modifications
git add taskTool.py
git commit -m "Ajouter la fonction pour supprimer la base de données dans taskTool.py"


