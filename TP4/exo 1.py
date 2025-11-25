n = int(input("entrez un nombre"))
l=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(11):
    l[i]=n*i
    print( n,"*",i,"=",l[i])