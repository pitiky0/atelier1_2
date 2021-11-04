# Ecrire un fonction Python qui inverse les lettres d’une chaîne de caractères.

def inverse(string):
    return string[::-1]
def inv(s):
    b =""
    for i in range(1,len(s)+1):
        b +=s[-i]
    return b

s = input('Entrer une chaîne de caractères : ')
print("L'inverse de cette chaîne de caractères est :" ,inv(s))