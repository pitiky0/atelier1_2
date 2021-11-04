#  Ecrire un programme en Python pour convertir le nombre décimal en nombre binaire
# en utilisant la fonction.

def dis_2_bin(n):
    if n == 0:
        return 0
    else:
        return n%2 + (10*dis_2_bin(n//2))
n = int(input('entré le nombre en décimal :'))
print('ce nombre en binaire égale a :',dis_2_bin(n))