def tri_insertion(A, cmp=(lambda x,y: x < y), print_mode=False):
    for j in range(1, len(A)):
        key = A[j]
        # on insere A[j] dans la sequence triee A[1..j-1]
        i = j - 1
        while i >= 0 and cmp(key, A[i]):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
        if print_mode:
            print(A)

A = [31, 41, 59, 26, 41, 58]
print("---initial values---")
print(A)
print("--------------------")
tri_insertion(A, cmp=(lambda x,y: y < x), print_mode=True)
print("-----End values-----")
print(A)
print("--------------------")
