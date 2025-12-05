import random

def generer(nbr, vmin, vmax):

    return [random.randint(vmin, vmax) for _ in range(nbr)]

def combienInferieur(table, vseuil):

    compteur = 0
    for val in table:
        if val < vseuil:
            compteur += 1
    return compteur


nb = 100
print(f"Générer {nb} nombres entiers entre 0 et 100")
tab = generer(nb, 0, 100)
tab.sort()
print(tab)
total = combienInferieur(tab, 25)
print(f"Il y en a {total} inférieurs à 25")
