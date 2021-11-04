# 1. Créer une liste en choisissant des éléments d'index impair dans la première liste et des
# éléments d'index pair dans la seconde.
# Étant donné deux listes, l1 et l2, écrivez un programme pour créer une troisième liste l3 en
# choisissant un élément d'indice impair dans la liste l1 et des éléments d'indice pair dans la liste
# l2.

def append_in_list(l1,l2):
    l3=[]
    for i in range(len(l1)):
        if i%2 != 0:
            l3.append(l1[i])
    for j in range(len(l2)):
        if j%2 == 0:
            l3.append(l2[j])
    return l3
list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 4, 3, 2, 3, 2, 44]
print(append_in_list(list1, list2))