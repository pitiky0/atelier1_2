#  Ecrire un programme en Python pour imprimer la série Fibonacci en utilisant la
# récursivité.

def fibo(n):
    if n in [0, 1] :
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input('entrer un nombre : '))
print('la serie de fibonacci de ce nombre est : ',end="")
l = [fibo(i) for i in range(n)]
for i in l:
    print(i, end=" ")