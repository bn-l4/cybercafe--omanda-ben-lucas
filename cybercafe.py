import  random
import joueur


courant = True
code_compteur = 0

postes = 6
postes_panne =  0
poste_disponibles = postes - postes_panne
cout_reparation = 15000

#PC en panne
def provoquer_panne():
    global postes_panne ,poste_disponibles
    nombre  =  random.randint(1, 100)

    if nombre <= 20:
         if  postes_panne < postes:
             postes_panne += 1
             poste_disponibles -= 1

#Coupure
def provoquer_coupure():
    global courant, code_compteur

    courant = False
    code_compteur = random.choice([1, 3, 5])

    print("\nAlerte COUPURE DE COURANT !")
    print("Le cybercafe est dans le noir.")
    print("Impossible d'accueillir de nouveaux clients.")
    print("Tape Q pour aller au compteur.")

#Compteur
def reparer_courant():
    global courant

    while not courant:

        choix = input("Tape Q pour aller au compteur : ").lower()

        if choix == "q":

            print("\n=== COMPTEUR ELECTRIQUE ===")
            print(f"Pour remettre le courant entrer : {code_compteur} ")

            code = input("Chiffre : ")

            if code.isdigit() and int(code) == code_compteur:

                courant = True
                print("\nLe courant est revenu !")
                input("Tape Q pour retourner au cybercafe : ")

            else:
                print("Mauvais code ! Le courant est toujours coupe.")

        else:
            print("Tu dois taper Q.")

#Pour les rats
def attaque_rats():
    global postes_panne, poste_disponibles

    if postes_panne >= postes:
        print("Tous les postes sont deja detruits !")
        return

    nombre = random.randint(1, postes - postes_panne)

    postes_panne += nombre
    poste_disponibles = postes - postes_panne

    print("\nDES RATS ONT ATTAQUE LE CYBERCAFE !")
    print(f"{nombre} poste(s) ont ete detruits !")
    print(f"Postes fonctionnels : {poste_disponibles}/{postes}")

    reparateur()

#Pour les raparateur
def reparateur():
    global  poste_disponibles, postes_panne

    while True:

        choix = input("\nTape E pour voir le reparateur ou Q pour revenir : ").lower()

        if choix == "q":
            print("Retour au cybercafe.")
            return

        elif choix == "e":

            print("\n===== REPARATEUR =====")
            print("Argent disponible :", joueur.argent, "FCFA")
            print("Postes detruits :", postes_panne)

            # Prix aleatoire pour chaque poste
            prix_postes = []

            for i in range(postes_panne):
                prix = random.randint(50000, 120000)
                prix_postes.append(prix)

            # Afficher les offres
            print("\n===== OFFRES DE REPARATION =====")

            for nombre in range(1, postes_panne + 1):

                prix_total = sum(prix_postes[:nombre])

                print(f"Reparer {nombre} PC : {prix_total} FCFA")

            choix_nombre = input("\nCombien de PC veux-tu reparer ? : ")

            if not choix_nombre.isdigit():
                print("Choix invalide.")
                continue

            nombre_a_reparer = int(choix_nombre)

            if nombre_a_reparer < 1 or nombre_a_reparer > postes_panne:
                print("Nombre de PC invalide.")
                continue

            prix_reparation = sum(prix_postes[:nombre_a_reparer])

            print(f"\nReparation de {nombre_a_reparer} PC")
            print("Prix :", prix_reparation, "FCFA")
            print("Ton solde :", joueur.argent, "FCFA")

            choix_paiement = input("Tape E pour payer ou Q pour revenir : ").lower()

            if choix_paiement == "q":
                print("Tu refuses la reparation.")
                print("Postes fonctionnels :", poste_disponibles)
                continue

            elif choix_paiement == "e":

                if joueur.argent < prix_reparation:
                    print("\nTu n'as pas assez d'argent !")
                    print("Solde :", joueur.argent, "FCFA")
                    print("Prix :", prix_reparation, "FCFA")
                    continue

                joueur.argent -= prix_reparation

                postes_panne -= nombre_a_reparer
                poste_disponibles = postes - postes_panne

                print("\nReparation effectuee !")
                print("PC repares :", nombre_a_reparer)
                print("Argent restant :", joueur.argent, "FCFA")
                print(f"Postes fonctionnels : {poste_disponibles}/{postes}")

                return

            else:
                print("Choix invalide.")

        else:
            print("Tape E ou Q.")