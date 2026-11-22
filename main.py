import sauvegarde
import joueur
import cybercafe
import temps
import dette


print("=======================")
print("     CYBERCAFE")
print("=======================")

print("\nBienvenue dans votre cybercafe !")
print("Vous avez 30 jours pour rembourser votre dette.\n")

print("===== COMMANDES DU JEU =====")
print("S : Sauvegarder la partie")
print("R : Mettre le jeu en pause")
print("Q : Quitter le jeu")
print("============================\n")

print("Argent :", joueur.argent, "FCFA")
print("Dette :", dette.dette, "FCFA")
print("Postes disponibles :", cybercafe.poste_disponibles)

print("\n=======================")
print("    DEBUT DU JEU")
print("=======================\n")

reprise = None

choix = input("N : Nouvelle partie | C : Continuer : ").lower()

if choix == "c":
    reprise = sauvegarde.charger()

    if reprise is None:
        print("Demarrage d'une nouvelle partie.")

while temps.jour_actuel <= temps.limite:

    continuer = temps.lancer_journee(reprise)

    reprise = None

    if continuer == False:
        break

print("\n=======================")
print("    FIN DU JEU")
print("=======================")