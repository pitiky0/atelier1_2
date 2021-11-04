# Ecrire un programme en Python pour compter les chiffres d'un nombre donné en
# utilisant la récursivité.
#
def count1(n):
    return len(str(n))

def count2(n ,a):
    if n // 10 == 0:
        return a
    else:
        a += 1
        return count2(n//10, a)

n = int(input('entrer un nombre : '))
print('le nombre des chiffres de ce nombre est ', count1(n))
print('le nombre des chiffres de ce nombre est ', count2(n,1))