base=4
fromagt=800
eau=2
ail=2
pain=400

personne = int(input('Entrez le nombre de personne(s) conviées à la fondue :'))
print('Pour faire une fondue fribourgeoise pour',personne,' il vous faut :')

fromage = (fromagt * personne / base)
eau =( eau * personne / base)
ail = (ail * personne / base)
pain = (pain * personne / base)

print('-',fromage,'gr de fromage')
print('-',eau,'dl d eau')
print('-',ail,'gousses d ail ')
print('-',pain,'gr de pain')