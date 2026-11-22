import json
import joueur
import dette
import cybercafe
import clients
import temps
import os

def sauvegarder(temps_restant):



    donnees = {
        "jour_actuel": temps.jour_actuel,
        "argent": joueur.argent,
        "dette": dette.dette,

        "postes": cybercafe.postes,
        "postes_panne": cybercafe.postes_panne,
        "poste_disponibles": cybercafe.poste_disponibles,

        "courant": cybercafe.courant,
        "code_compteur": cybercafe.code_compteur,

        "clients_presents": clients.clients_presents,

        "temps_restant": temps_restant,
        "compteur": temps.compteur
    }

    with open("sauvegarde.json", "w") as fichier:
        json.dump(donnees, fichier, indent=4)

    print("\n===== SAUVEGARDE =====")
    print("Partie sauvegardee avec succes !")

def charger():

    if not os.path.exists("sauvegarde.json"):
        print("\nAucune sauvegarde trouvee.")
        return None

    try:
        with open("sauvegarde.json", "r") as fichier:
            donnees = json.load(fichier)

    except (json.JSONDecodeError, OSError):
        print("\nImpossible de lire la sauvegarde.")
        return None

#Restaurer les informations du joueur
    temps.jour_actuel = donnees["jour_actuel"]
    joueur.argent = donnees["argent"]
    dette.dette = donnees["dette"]

#Restaurer le cybercafe
    cybercafe.postes = donnees["postes"]
    cybercafe.postes_panne = donnees["postes_panne"]
    cybercafe.poste_disponibles = donnees["poste_disponibles"]

    cybercafe.courant = donnees["courant"]
    cybercafe.code_compteur = donnees["code_compteur"]

#Restaurer les clients
    clients.clients_presents[:] = donnees["clients_presents"]

    print("\n===== CHARGEMENT =====")
    print("Partie chargee avec succes !")

    return donnees["temps_restant"], donnees["compteur"]