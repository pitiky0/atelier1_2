# Ecrire une fonction Python pour trouver la fréquence d’un caractère dans une chaîne.

def fre(string, a):
   n = 0
   for i in string:
       if i == a:
           n += 1
   return n
string = input('entrer une chaîne : ')
a = input('entre un caractère : ')
print('la fréquence de caractère est : ', fre(string,a))