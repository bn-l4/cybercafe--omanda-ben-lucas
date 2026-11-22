import random
import cybercafe
import  joueur

clients = 0
prix_session = 2500
revenu = 0

liste_clients = [
    {"nom": "Edgard :)", "type": "Regulier", "dialogue": "Bonjour !"},
    {"nom": "Richard :)", "type": "Regulier", "dialogue": "Un poste stp"},
    {"nom": "Carl :)", "type": "Regulier", "dialogue": "Mon frere comment sa vas, un poste stp"},
    {"nom": "Evelyne :|", "type": "Normal", "dialogue": "Bonjour !"},
    {"nom": "Fabio :(", "type": "Normal", "dialogue": "Puis je avoir un poste "},
    {"nom": "Inconnu:|", "type":"Normal", "dialogue": "Bonjour tout le monde !"},
    {"nom": "Karim :)", "type": "Regulier", "dialogue": "Mam un poste stp" },
    {"nom": "Mr charle :{", "type": "Regulier", "dialogue": "Bonjour mon jeune ami, un pose"},
    {"nom": "Inconnu :|", "type": "Normal", "dialogue": "Bonjour !"},
    {"nom": "Inconnu :? ", "type": "Normal", "dialogue": "Un poste"}
]

clients_presents = []

def accueillir_clients(postes_disponibles):

    if not cybercafe.courant:
        print("Impossible le courant est coupe !")
        return

    place_libres = postes_disponibles - len(clients_presents)

    if  place_libres <= 0:
        print("Plus de poste disponible !")
        return

    nombre_clients = random.randint(1, 2)

    #Limitation des clients selon les postes libres

    nombre_clients = min(nombre_clients, place_libres)

    nouveaux_clients = random.sample(liste_clients, nombre_clients)

    for client in nouveaux_clients:
        client_actuel = client.copy()
        client_actuel["temps_restant"] = 3

        clients_presents.append(client_actuel)

        joueur.ajouter_argent(prix_session)

        print(f"Paiement : +{prix_session} FCFA")
        print(f"Argent en caisse : {joueur.argent} FCFA")

        print("\nUn client est rentre !")
        print(f"{client_actuel['nom']} ({client_actuel['type']}) : \"{client_actuel['dialogue']}\"")

    print("Clients presents :", len(clients_presents))


def calculer_revenu(nombre_clients):
    return  nombre_clients * prix_session

def nouvelle_journee():
    clients_presents.clear()
    print("Les anciens client sont partis.")
    print("Le cybercafe est pres pour une nouvelle journee")


def mettre_a_jour_clients():
    for client in clients_presents[:]:

        client["temps_restant"] -= 1

        if client["temps_restant"] <= 0:

            print(f"\n{client['nom']} quitte le cybercafe.")
            clients_presents.remove(client)

            print("Un poste vient de se liberer !")
            print("CLients present : ", len(clients_presents))
