

L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

max_freq = 0
most_frequent = L1[0]

for i in range(len(L1)):
    freq = L1.count(L1[i])
    if freq > max_freq:
        max_freq = freq
        most_frequent = L1[i]

print("Le nombre le plus frequent dans la liste est le :", most_frequent, f"({max_freq} x)")
