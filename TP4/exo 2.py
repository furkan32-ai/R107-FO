

nbe = int(input("Donnez le nombre d'etudiants : "))
somme = 0.0
notes = []

for i in range(nbe):
    note = float(input(f"Note etudiant {i} : "))
    while note < 0 or note > 20:
        print("Erreur : entrez un nombre entre 0 et 20")
        note = float(input(f"Note etudiant {i} : "))
    notes.append(note)
    somme += note


moyenne = somme / nbe
print("Moyenne de classe :", moyenne)


print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nbe):
    ecart = notes[i] - moyenne
    print(f"{i} | {notes[i]} | {ecart:.2f}")