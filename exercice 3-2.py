# Écrire un programme pour itérer une liste donnée et compter l'occurrence de chaque élément et
# créer un dictionnaire pour montrer le nombre de chaque élément
def count_list(l):
    dec = {}
    for i in l:
        a = l.count(i)
        dec.update({i: a})
    return dec
list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(count_list(list))