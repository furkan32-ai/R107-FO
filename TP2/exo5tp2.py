from math import *
nombre = int(input('Entrez un nombre entier:'))

if nombre > 0:
    signe = "positif"
elif nombre < 0:
    signe = "négatif"
else:
    signe = "zéro"

if nombre % 2 == 0:
    parite = "pair"
else:
    parite = "impair"
print('Le nombre est ',signe,'et',parite,)