
texte = input("Entrez un mot ou une phrase : ")


texte2 = ""
for c in texte:
    if c.isalpha():
        texte2 += c.lower()


if texte2 == texte2[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
