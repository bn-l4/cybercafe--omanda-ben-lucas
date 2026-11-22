import sys
import select
import tty
import termios
import time

ancien_mode = None


def activer_clavier():
    global ancien_mode

    if not sys.stdin.isatty():
        raise RuntimeError("Terminal non compatible.")

    if ancien_mode is None:
        ancien_mode = termios.tcgetattr(sys.stdin.fileno())

    tty.setcbreak(sys.stdin.fileno())

    mode = termios.tcgetattr(sys.stdin.fileno())
    mode[3] &= ~termios.ECHO

    termios.tcsetattr(
        sys.stdin.fileno(),
        termios.TCSADRAIN,
        mode
    )


def lire_touche():
    touches = select.select([sys.stdin], [], [], 0)[0]

    if touches:
        return sys.stdin.read(1).lower()

    return None


def touche_r_appuyee():
    return lire_touche() == "r"


def mettre_en_pause():

    print("\n===== PAUSE =====")
    print("R : Reprendre")
    print("Q : Quitter")

    while True:

        touche = lire_touche()

        if touche == "r":
            print("\nReprise du jeu !")
            return True

        elif touche == "q":
            print("\nFermeture du jeu.")
            return False

        time.sleep(0.1)


def restaurer_clavier():
    global ancien_mode

    if ancien_mode is not None:

        termios.tcsetattr(
            sys.stdin.fileno(),
            termios.TCSADRAIN,
            ancien_mode
        )

        ancien_mode = None
