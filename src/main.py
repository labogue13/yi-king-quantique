import random

def tirage_yi_king():
    """Génère un hexagramme Yi King de 6 lignes"""
    hexagramme = [random.choice(["⚋ (ligne brisée)", "⚊ (ligne pleine)"]) for _ in range(6)]
    return hexagramme

if __name__ == "__main__":
    print("✨ Votre hexagramme Yi King Quantique :")
    for ligne in reversed(tirage_yi_king()):  # On affiche de bas en haut
        print(ligne)