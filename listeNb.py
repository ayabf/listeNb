def somme_nbs_pairs(liste):
    somme = 0
    for nombre in liste:
        if nombre % 2 == 0:
            somme += nombre
    return somme

ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = somme_nbs_pairs(ma_liste)
print(f"La somme des nombres pairs est : {resultat}")
