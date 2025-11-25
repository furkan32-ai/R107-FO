nMax=3
v1=[]
v2=[]
n=int(input("Entrez la taille effective des vecteurs"))
while n<1  or n>nMax:
    print("erreur")
    n = int(input("Entrez une nouvelle taille effective des vecteurs"))

print("Saisie du premier vecteur :")
for i in range(n):
    valeur = int(input())
    v1.append(valeur)

print("Saisie du second vecteur :")
for i in range(n):
    valeur = int(input())
    v2.append(valeur)

produit_scalaire = 0
for i in range(n):
    produit_scalaire += v1[i] * v2[i]

print(f"Le produit scalaire de v1 par v2 vaut" ,produit_scalaire)