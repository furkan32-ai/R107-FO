
jour = int(input(Entrez le jour du mois ))
heure = int(input("Entrez l'heure (entre 0 et 23) : "))
minute = int(input("Entrez les minutes (entre 0 et 59) : "))
minutes_ecoulees = ((jour - 1) * 24 * 60) + (heure * 60) + minute
print("Nombre de minutes écoulées depuis le début du mois :", minutes_ecoulees)
               
