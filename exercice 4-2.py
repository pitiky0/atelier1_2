# 4. Trouver l'intersection (commune) de deux Sets et supprimez ces éléments du premier Set
def intersec(s1, s2):
    inter = set()
    for i in s2 :
        if i in s1 :
            inter.add(i)
            s1.remove(i)
    return inter, s1
set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
print(intersec(set1, set2))