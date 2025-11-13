from random import*
compteur = 0
x = randint(0, 2)

n = int(input("Entrez un nombre : "))
compteur += 1

while n != x:
    if n > x:
        print("Le nombre est plus petit")
    else:
        print("Le nombre est plus grand")

    n = int(input("Entrez un nombre : "))
    compteur += 1

print("Bravo vous avez trouver le bon numero en", compteur, "essai(s).")
