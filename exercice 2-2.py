# Deviser la liste en 3 morceaux égaux et inverser chaque morceau
def div_en_3(l):
    l1 = []; l2 = []; l3 = []
    for i in range(len(l)):
        if i < len(l)/3 :
            l1.insert(0, l[i])
        elif i >= len(l)/3 and i < 2*len(l)/3 :
            l2.insert(0, l[i])
        else:
            l3.insert(0, l[i])
    return l1, l2, l3
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(div_en_3(list))