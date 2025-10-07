import pandas as pd

# Déclaration du dictionnaire "Magasin" avec des listes de longueurs différentes
Magasin = {
    "Fruits": ["Pomme", "Banane", "Orange", "Fraise"],
    "Légumes": ["Carotte", "Brocoli", "Tomate", "Épinard"],
    "Produits laitiers": ["Lait", "Fromage", "Yaourt"],  # Liste plus courte
    "Viandes": ["Poulet", "Boeuf", "Porc", "Poisson"],
    "Céréales": ["Riz", "Pâtes", "Pain", "Quinoa"]
}

# Fonction pour afficher le contenu du dictionnaire
def afficher_magasin(magasin):
    print("\nDonnées brutes: ")
    for categorie, produits in magasin.items():
        print(f"{categorie}: {', '.join([str(p) for p in produits])}")

# Appel de la fonction d'affichage
afficher_magasin(Magasin)

print("\n")
print("\n")

# Fonction qui transforme les données en DataFrame
def dictToDataframe(data: dict):
    # Normaliser les longueurs des listes du dictionnaire
    max_len = max(len(liste) for liste in data.values())
    for key in data:
        while len(data[key]) < max_len:
            data[key].append("")

    return pd.DataFrame(data)

result = dictToDataframe(Magasin)

print("\nData frame: ")

print(result)

result.to_csv('magasin.csv', index=False)

print("\nCSV sauvegardé sous le nom 'magasin.csv.")