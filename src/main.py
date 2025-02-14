import random
import json

# Charger les interprétations des hexagrammes
with open("source/hexagrammes_complet.json", "r", encoding="utf-8") as f:
    interpretations = json.load(f)

def tirage_yi_king():
    """Génère un hexagramme Yi King en 6 lignes"""
    hexagramme = "".join(random.choice(["⚋", "⚊"]) for _ in range(6))
    return hexagramme

if __name__ == "__main__":
    # Générer un hexagramme aléatoire
    hexagramme = tirage_yi_king()

    # Afficher l'hexagramme
    print("✨ Votre hexagramme Yi King Quantique :\n")
    for ligne in reversed(hexagramme):  # Affichage de bas en haut
        print(ligne)

    # Trouver l'interprétation
    interpretation = interpretations.get(hexagramme, {"nom": "Inconnu", "signification": "Pas d'interprétation disponible."})

    # Afficher l'interprétation
    print(f"\n📖 Hexagramme : {interpretation['nom']}")
    print(f"🧐 Signification : {interpretation['signification']}")