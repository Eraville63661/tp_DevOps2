from math import comb

def proba_extraction(k, nb_rouge, nb_blanche, nb_noire):


    # Vérification que le nombre total de boules à tirer est au moins 3
    if k < 3:
        raise ValueError("Le nombre de boules à tirer doit être >=3.")

    # Vérification que le nombre total de boules dans l'urne est au moins 3
    if nb_rouge + nb_blanche + nb_noire < 3:
        raise ValueError("Le nombre boules dans l'urne au moins 3.")

    # Vérification que le nombre de boules rouges, blanches et noires est positif
    if nb_rouge < 0 or nb_blanche < 0 or nb_noire < 0:
        raise ValueError("Le nombre de boules doit être positif.")

    # Vérification que le nombre total de boules dans l'urne est suffisant pour tirer k boules
    if k > nb_rouge + nb_blanche + nb_noire:
        raise ValueError("Pas assez de boules pour tirer k boules.")

    # Calcul du nombre de façons d'obtenir exactement une boule de chaque couleur
    nombre_combinaisons = comb(nb_rouge, 1) * comb(nb_blanche, 1) * comb(nb_noire, 1)

    # Calcul du nombre total de façons de tirer k boules parmi toutes les boules de l'urne
    nombre_total_combinaisons = comb(nb_rouge + nb_blanche + nb_noire, k)

    # Calcul de la probabilité
    probabilite = nombre_combinaisons / nombre_total_combinaisons

    return probabilite

# Exemple d'utilisation
k = 3
nb_rouge = 5
nb_blanche = 4
nb_noire = 3

resultat = proba_extraction(k, nb_rouge, nb_blanche, nb_noire)
print(f"La probabilité est : {resultat:.4f}")
