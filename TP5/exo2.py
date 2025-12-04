
notes = []
coeffs = []


for i in range(1, 6):
    saisie = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")

    valeurs = saisie.split(" ")
    note = float(valeurs[0])
    coeff = int(valeurs[1])

    notes.append(note)
    coeffs.append(coeff)


somme_notes = 0
somme_coeffs = 0
for i in range(5):
    somme_notes += notes[i] * coeffs[i]
    somme_coeffs += coeffs[i]

moyenne = somme_notes / somme_coeffs


admis = True
if moyenne <= 10:
    admis = False
if min(notes) < 8:
    admis = False


print(f"Moyenne générale : {moyenne:.2f}")
if admis:
    print("L'étudiant est admis ")
else:
    print("L'étudiant n'est pas admis ")
