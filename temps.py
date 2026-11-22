import time
import cybercafe
import clients
import random
import dette
import pause
import sauvegarde


jour_actuel = 1
limite = 30
duree_journee = 3
temps_ecoule = 0
compteur = 0


def lancer_journee(reprise=None):
    global jour_actuel, compteur

    rats_declenches = False
    coupure_declenchee = False

    pause.activer_clavier()

    try:

        if reprise is None:
            #Nouvelle journée
            clients.nouvelle_journee()
            compteur = 0
            temps_restant = 60

        else:
            #Reprendre une sauvegarde
            temps_restant, compteur = reprise
            print("\nReprise de votre ancienne partie !")

        while temps_restant > 0:

            minutes, secondes = divmod(temps_restant, 60)

            print(
                f"Jour {jour_actuel} | "
                f"00:{minutes:02d}:{secondes:02d} | "
                f"Dette : {dette.dette} FCFA"
            )

            #Gestion des touches
            touche = pause.lire_touche()

            if touche == "r":
                if not pause.mettre_en_pause():
                    return False

            elif touche == "q":
                print("\nFermeture du jeu.")
                return False

            elif touche == "s":
                sauvegarde.sauvegarder(temps_restant)

            time.sleep(1)

            #Declenchement des rats
            if not rats_declenches and random.randint(1, 100) <= 2:
                rats_declenches = True

                pause.restaurer_clavier()

                try:
                    cybercafe.attaque_rats()

                finally:
                    pause.activer_clavier()

            #Declenchement des coupures
            if not coupure_declenchee and random.randint(1, 100) <= 5:
                coupure_declenchee = True
                cybercafe.provoquer_coupure()

                pause.restaurer_clavier()

                try:
                    cybercafe.reparer_courant()

                finally:
                    pause.activer_clavier()

            clients.mettre_a_jour_clients()

            temps_restant -= 1
            compteur += 1

            if compteur == 3:
                clients.accueillir_clients(cybercafe.poste_disponibles)
                compteur = 0

    finally:
        pause.restaurer_clavier()

    print(f"\nJour {jour_actuel} TERMINE!")

    if jour_actuel >= limite and dette.dette > 0:
        print("\n============================")
        print("         GAME OVER")
        print("  DETTE NON REMBOURSEE")
        print("============================")
        return False

    while True:
        choix = input("\nA : Jour suivant | W : Rembourser : ").lower()

        if choix == "w":
            dette.rembourser()

            if dette.dette == 0:
                print("\n============================")
                print("        VICTOIRE !")
                print("   DETTE REMBOURSEE")
                print("============================")
                return False

        elif choix == "a":
            if jour_actuel >= limite:
                print("\n============================")
                print("         GAME OVER")
                print("  DETTE NON REMBOURSEE")
                print("============================")
                return False

            jour_actuel += 1
            print(f"\nJour {jour_actuel}/{limite}")
            return True

        else:
            print("Touche incorrecte.")
