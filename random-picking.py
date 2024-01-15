from math import comb

def proba_extraction(k, nb_rouge, nb_blanche, nb_noire):


    if k < 3:
        raise ValueError("Le nombre de boules à tirer doit être >=3.")

    if nb_rouge + nb_blanche + nb_noire < 3:
        raise ValueError("Le nombre boules dans l'urne au moins 3.")

    if nb_rouge < 0 or nb_blanche < 0 or nb_noire < 0:
        raise ValueError("Le nombre de boules doit être positif.")

    if k > nb_rouge + nb_blanche + nb_noire:
        raise ValueError("Pas assez de boules pour tirer k boules.")

    nombre_combinaisons = comb(nb_rouge, 1) * comb(nb_blanche, 1) * comb(nb_noire, 1)

    nombre_total_combinaisons = comb(nb_rouge + nb_blanche + nb_noire, k)

    probabilite = nombre_combinaisons / nombre_total_combinaisons

    return probabilite

# Exemple d'utilisation
k = 3
nb_rouge = 5
nb_blanche = 4
nb_noire = 3

resultat = proba_extraction(k, nb_rouge, nb_blanche, nb_noire)
print(f"La probabilité est : {resultat:.4f}")
