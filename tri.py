T = [8, 3, 5, 1, 7]
n = len(T)


def triSelection(T):  
    for i in range(len(T)-1):
        i_min= i
        for j in range(i + 1, len(T)):
            if T[j] < T[i_min]:
                T[j], T[i_min] = T[i_min], T[j]       
    return T


def triBulle(T):
    compare=0
    change=0
    for i in range(len(T) - 1):
        change=True
        for j in range(len(T)-1-i):
            compare+=1
            if T[j] > T[j + 1]:
                T[j+1], T[j] = T[j], T[j+1]
            if not change:
                break
    return T, compare,change


def triParInsertion(T):
    for i in range(len(T)):
        cle = T[i]
        j = i - 1
        while j >= 0 and T[j] > cle:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1]=cle
    return T

print(triParInsertion(T))
