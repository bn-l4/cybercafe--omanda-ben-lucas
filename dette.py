import joueur

dette = 400000
remboursement_minimum = 50000


def afficher_dette():
    print("Dette restante :", dette, "FCFA")


def rembourser():
    global dette

    print("\n===== REMBOURSEMENT =====")
    print("Argent disponible :", joueur.argent, "FCFA")
    print("Dette restante :", dette, "FCFA")
    print("Minimum à rembourser :", remboursement_minimum, "FCFA")

    montant = input("Montant à rembourser : ")

    if not montant.isdigit():
        print("Montant invalide.")
        return

    montant = int(montant)

    if montant < remboursement_minimum:
        print("Le remboursement minimum est de 50 000 FCFA.")
        return

    if montant > joueur.argent:
        print("Tu n'as pas assez d'argent.")
        return

    if montant > dette:
        print("Tu ne peux pas rembourser plus que ta dette.")
        return

    joueur.argent -= montant
    dette -= montant

    print("\nRemboursement effectué !")
    print("Montant payé :", montant, "FCFA")
    print("Argent restant :", joueur.argent, "FCFA")
    print("Nouvelle dette :", dette, "FCFA")

    if dette == 0:
        print("\nFELICITATIONS ! Tu as remboursé toute ta dette !")