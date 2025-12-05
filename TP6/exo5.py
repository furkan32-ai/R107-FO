import unicodedata
import string

def nettoyer_texte(texte):
    """Supprime les caractères spéciaux, espaces et ponctuations."""

    texte_nettoye = ""
    for c in texte:
        if c.isalpha():
            texte_nettoye += c.lower()
    return texte_nettoye

def supprimer_accents(texte):
    """Remplace les caractères accentués par leur base (é -> e)."""

    texte_sans_accents = unicodedata.normalize('NFD', texte)

    texte_sans_accents = ''.join(
        c for c in texte_sans_accents if unicodedata.category(c) != 'Mn'
    )
    return texte_sans_accents

def est_palindrome(texte):

    texte = supprimer_accents(texte)
    texte = nettoyer_texte(texte)

    return texte == texte[::-1]


texte = input("Entrez un mot ou une phrase : ")

if est_palindrome(texte):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
