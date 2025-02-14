import random
import json

# Charger les interprétations depuis le fichier JSON
with open("src/hexagrammes.json", "r", encoding="utf-8") as f:
    interpretations = json.load(f)

def tirage_yi_king():
    """Génère un hexagramme Yi King"""
    hexagramme = [random.choice(["⚋", "⚊"]) for _ in range(6)]
    return "".join(hexagramme)  # Transformer en une seule chaîne

if __name__ == "__main__":
    hexagramme = tirage_yi_king()
    print("✨ Votre hexagramme Yi King Quantique :")
    for ligne in reversed(hexagramme):  # Affichage en colonne
        print(ligne)
    
    # Afficher l'interprétation si elle existe
    interpretation = interpretations.get(hexagramme, "Interprétation inconnue.")
    print("\n📖 Signification :", interpretation)