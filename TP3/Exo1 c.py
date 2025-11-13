moins10 = 0
entre10_15 = 0
plus15 = 0

for i in range(10):
    valeur= int(input("Valeur (entre 0 et 20) : "))
    if valeur < 10:
        moins10 =moins10 + 1
    elif valeur < 15:
        entre10_15 =entre10_15+1
    else:
        plus15 = plus15+ 1

print("Valeurs < 10 :", moins10)
print("Valeurs entre 10 et 15 :", entre10_15)
print("Valeurs > 15 :", plus15)

