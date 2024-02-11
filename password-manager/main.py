import json
import random
import string

file = "data.json"

def add_mdp():
    print("\n----- Menu: -----")
    print("| 1. Entrer un mot de passe")
    print("| 2. Generer un mot de passe")
    print("| 0. Quitter")
    print("-------------------")

    choice = input("Entrez votre choix : ")

    if choice == "0":
        return
    elif choice == "1":
        app = input("Entrez le nom de l'app qui utilise le mot de passe: ")
        psd = input("Entrez le pseudo/email utilisé: ")
        mdp = input("Entrez votre mot de passe: ")

        try:
            # Charger les données existantes du fichier JSON
            with open(file, "r") as fichier_json:
                donnees_existantes = json.load(fichier_json)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore ou est vide, initialiser à une liste vide
            donnees_existantes = []

        # Ajouter les nouvelles données aux données existantes
        nouvelle_entree = {"App": app, "Pseudo": psd, "Mdp": mdp}
        donnees_existantes.append(nouvelle_entree)

        # Réécrire toutes les données dans le fichier JSON
        with open(file, "w") as fichier_json:
            json.dump(donnees_existantes, fichier_json, indent=4)

        print("Données ajoutées avec succès dans", file)

    elif choice == "2":
        nbr = int(input("Entrez le nombre de caractères de votre mdp: "))
        char = input("Voulez-vous des caractères spéciaux (y/n): ")
        if char == "y":
            caracteres = string.ascii_letters + string.digits + string.punctuation
            mdp = ''.join(random.choice(caracteres) for _ in range(nbr))
        elif char == "n":
            caracteres = string.ascii_letters + string.digits
            mdp = ''.join(random.choice(caracteres) for _ in range(nbr))
        else:
            print("Choix invalide")
            return
        app = input("Entrez le nom de l'app qui utilise le mot de passe: ")
        psd = input("Entrez le pseudo/email utilisé: ")
        nouvelle_entree = {"App": app, "Pseudo": psd, "Mdp": mdp}

        try:
            # Charger les données existantes du fichier JSON
            with open(file, "r") as fichier_json:
                donnees_existantes = json.load(fichier_json)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore ou est vide, initialiser à une liste vide
            donnees_existantes = []

        # Ajouter les nouvelles données aux données existantes
        donnees_existantes.append(nouvelle_entree)

        # Réécrire toutes les données dans le fichier JSON
        with open(file, "w") as fichier_json:
            json.dump(donnees_existantes, fichier_json, indent=4)

        print("Données ajoutées avec succès dans", file)

    else:
        print("Choix invalide")

def view_mdp():
    try:
        # Charger les données du fichier JSON
        with open("data.json", "r") as json_file:
            data = json.load(json_file)

        print(data)
        
    except FileNotFoundError:
        print("Le fichier JSON n'existe pas.")
        return []
    except json.decoder.JSONDecodeError:
        print("Le fichier JSON est vide ou mal formaté.")
        return []


# Boucle principale
def main():
    while True:
        print("\n----- Menu: -----")
        print("| 1. Ajouter un mot de passe")
        print("| 2. Voir un mot de passe")
        print("| 0. Quitter")
        print("-------------------")

        choice = input("Entrez votre choix : ")

        if choice == "0":
            print("Au revoir !")
            break
        elif choice == "1":
            add_mdp() 
        elif choice == "2":
            print(view_mdp() )
        else:
            print("Choix invalide")

# Lancer le programme
if __name__ == "__main__":
    main()
