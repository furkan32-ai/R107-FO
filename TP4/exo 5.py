
def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

date_str = input("Entrez une date au format jjmmaaaa : ")

if len(date_str) != 8 or not date_str.isdigit():
    print("Format incorrect ! La date doit contenir exactement 8 chiffres (jjmmaaaa).")
else:

    jour = int(date_str[0:2])
    mois = int(date_str[2:4])
    annee = int(date_str[4:8])


    if mois < 1 or mois > 12:
        print("Date incorrecte : le mois doit être compris entre 01 et 12.")
    else:

        jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if est_bissextile(annee):
            jours_par_mois[1] = 29


        if jour < 1 or jour > jours_par_mois[mois - 1]:
            print("Date incorrecte : le jour n'existe pas dans ce mois.")
        else:
            print("Date correcte :", f"{jour:02d}/{mois:02d}/{annee}")
