# ce probleme revient a parcourir de droite a gauche les deux tableaux A et B
# et a operer une addition mod 2 avec retenue en sauvegardant la j-eme retenue pour le i-eme bit, avec i = j + 1

def addition(A, B):
    n = len(A) # aussi len(B)
    C = [0] * (n + 1) # tableau a n + 1 elements
    carry = 0
    for i in range(n, 0, -1):
        bit = (A[i - 1] + B[i - 1] + carry) % 2
        carry = (A[i - 1] + B[i - 1] + carry) // 2
        C[i] = bit
    C[0] = carry

    return C

assert(addition([0,0,0,1], [1,1,1,1]) == [1,0,0,0,0])
assert(addition([1,0,0,1], [1,1,1,1]) == [1,1,0,0,0])
assert(addition([1,0,1,0], [0,1,0,1]) == [0,1,1,1,1])
assert(addition([1,1,1,1], [1,1,1,1]) == [1,1,1,1,0])
assert(addition([0,1], [0,0]) == [0,0,1])
