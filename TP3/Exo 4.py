
choix=int(input("choisissez votre boucle 1while ou 2for"))
fact=1
if choix==2:
    n=int(input("entrez un nombre"))
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
else:
    n =int(input("entrez un nombre"))
    while n!=0:
     fact = fact*choix
     n=n-1
    print(fact)
