# Itérer une liste donnée et vérifier si un élément donné existe en tant que valeur de clé dans un
# dictionnaire. Sinon, supprimez-le de la liste


def is_in_dec(l, d):
    i = 0
    while(i < len(l)):
        if l[i] not in d.values():
            l.pop(i)
            i -= 1
        i += 1
    return l
list = [47, 64, 69, 37, 76, 83, 95, 97, 12, 23, 23, 45, 67]
dec = {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
print(is_in_dec(list, dec))