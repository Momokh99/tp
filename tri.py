T = [8, 3, 5, 1, 7]
n = len(T)


def triSelection(T):
    for i in range(n):
        for j in range(i + 1, n):
            if T[j] < T[i]:
                T[j], T[i] = T[i], T[j]
    return T


def triBulle(T):
    for j in range(len(T) - 1):
        if T[j] < T[j + 1]:
            T[j], T[j + 1] = T[j + 1], T[j]
        print(T)
    return T


def triParInsertion(T):
    for i in range(len(T)):
        cle = T[i]
        j = i - 1
        while j >= 0 and T[j] < cle:
            T[j + 1] = T[j]
            j -= 1
            cle = T[j + 1]
    return T


print(triParInsertion(T))
