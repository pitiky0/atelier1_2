# Ecrire un programme en Python pour trouver la somme des séries 1! / 1 + 2! / 2 + 3! /
# 3 + 4! / 4 + 5! / 5 en utilisant la fonction.

def facto(n):
    if n == 0 : # ici c'est la condition d'arrete
        return 1
    else:
        return n*facto(n-1) # ici en utilise la recurcivite pour calculer le factoriel

def sum(x):
    n = 0
    for i in range(1,x+1):
        n += facto(i)/i
    return n
x = int(input('entrer le nombre n : '))
print(sum(x))