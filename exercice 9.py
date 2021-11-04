# Ecrire une fonction qui cherche un élément dans une matrice puis renvoi sa
# position « i,j ».

def is_in_mat(x):
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == x:
                return print('La position de cet élément est :',i,j )
    else:
        print("ce nombre n'existe pas dans la matrice")
l =[[1, 2, 3, 4],[5, 6, 7, 8]]
n =int(input('Entre un nombre : '))
is_in_mat(n)