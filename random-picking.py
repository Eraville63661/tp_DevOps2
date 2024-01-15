from math import comb


def proba_extraction(k, nb_rouge, nb_blanche, nb_noire):
    if k < 3:
        raise ValueError("Le nombre de boules à tirer doit être au moins 3.")

    if nb_rouge + nb_blanche + nb_noire < 3:
        raise ValueError("Le nombre total de boules doit être au moins 3.")

    if nb_rouge < 0 or nb_blanche < 0 or nb_noire < 0:
        raise ValueError("Le nombre de boules doit être positif.")

    if k > nb_rouge + nb_blanche + nb_noire:
        raise ValueError("Le nombre de boules dans l'urne est insuffisant.")

    nb_comb = comb(nb_rouge, 1) * comb(nb_blanche, 1) * comb(nb_noire, 1)
    nb_t_combi = comb(nb_rouge + nb_blanche + nb_noire, k)
    probabilite = nb_comb / nb_t_combi
    print(f"La probabilité est : {probabilite:.4f}")
    return probabilite
