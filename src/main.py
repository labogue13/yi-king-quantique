import random

def tirage_yi_king():
    hexagramme = [random.choice(["ligne brisée", "ligne pleine"]) for _ in range(6)]
    return hexagramme

if __name__ == "__main__":
    print("Votre hexagramme Yi King Quantique :")
    print(tirage_yi_king())