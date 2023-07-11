def recherche(A, v):
    i = 0
    n = len(A)
    while i < n and A[i] != v:
        i += 1
    return None if i == n else i
assert(recherche([3,7,2,4], 4) == 3)
assert(recherche([3,7,2,4], 3) == 0)
assert(recherche([3,7,2,4], 7) == 1)
assert(recherche([3,7,2,4], 10) == None)

# Initialisation:   Quand i = 0, on ne vient pas encore de parcourir le tableau. En outre le sous-tableau vide
#                   ne contient pas v (trivial)
# Conservation:     De maniere informelle, le corps de la boucle fonctionne en se deplacant vers la droite du tableau
#                   de sorte a ce que le sous-tableau [0, i - 1] ne contienne pas v.
#                   Si l'on trouve la valeur v a la position i, on sort de la boucle, et le sous tableau [0, i - 1]
#                   ne contient pas v
#                   Si l'on ne trouve pas la valeur v a la position i, alors le sous-tableau [0;i] ne contient pas v
#                   et l'incrementation de j pour l'iteration suivante conserve l'invariant.
# Terminaison:      Quand la boucle se termine, il y a deux possibilites:
#                   - Soit A[i] == v, on a alors trouve la valeur v dans A, et l'on peut rendre en sortie la position de v
#                   - Soit i >= n, on a alors parcouru tout le tableau, mais nous n'avons pas trouve v dans A, nous renvoyons
#                     None
#                   Dans tous les cas, l'algorithme est valide
