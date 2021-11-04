# Ecrire un programme en Python pour calculer la somme des nombres de 1 à n en
# utilisant la récursivité.

def sum (n):
    if n == 1:  #ici c'est la condition d'arrete
        return n
    else:
        return n+sum(n-1)

n = int(input('entré un nombre : '))
print('la somme de 1 à ',n ,' est : ' , sum(n))