T = [8, 3, 5, 1, 7]
n = len(T)


def triSelection(T):
    for i in range(len(T) - 1):
        i_min = i
        for j in range(i + 1, len(T)):
            if T[j] < T[i_min]:
                T[j], T[i_min] = T[i_min], T[j]
        print(f"étape {i} : T = {T}")
    return T


def triBulle(T):
    compare = 0
    change = 0
    for i in range(len(T) - 1):
        change = True
        for j in range(len(T) - 1 - i):
            compare += 1
            if T[j] > T[j + 1]:
                T[j + 1], T[j] = T[j], T[j + 1]
            if not change:
                break
    return T, compare, change


def triParInsertion(T):
    for i in range(len(T)):
        cle = T[i]
        print(f"étape {i} : T = {T}")
        j = i - 1
        while j >= 0 and T[j] > cle:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = cle
    return T


T = [1, 2, 3, 4, 5, 6]


def tst_triSelection(T):
    print("Tableau initial : ", T)
    print("______________________________________")
    triSelection(T)
    print("______________________________________")
    print("Tableau final :", T)


def tst_triBulle():
    T1 = [5, 3, 8, 1, 2]
    T1_trie, c1, e1 = triBulle(T1.copy())
    print(f"""le Tableau       : T={T1}
le trie tab      : {T1_trie}
Comparaison      : {c1}
l'exchange       : {e1}
______________________________________""")
    # meilleur cas
    T2 = [1, 2, 3, 5, 8]
    T2_trie, c2, e2 = triBulle(T2.copy())
    print(f"""Tableau déja trié: T={T2}
Comparaison      : {c2}
l'exchange       : {e2}
______________________________________""")
    # tab trie en inverse
    T3 = [8, 5, 4, 2, 1]
    T3_trie, c3, e3 = triBulle(T3.copy())
    print(f"""Tableau inverse trié: T={T3}
le trie tab      : {T3_trie}
Comparaison      : {c3}
l'exchange       : {e3}
______________________________________""")


tst_triBulle()
