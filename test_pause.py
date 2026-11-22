import pause
import time

pause.activer_clavier()

try:
    print("R : Pause | Q : Quitter")

    while True:

        touche = pause.lire_touche()

        if touche == "r":
            continuer = pause.mettre_en_pause()

            if not continuer:
                break

        elif touche == "q":
            print("Au revoir !")
            break

        time.sleep(0.1)

finally:
    pause.restaurer_clavier()