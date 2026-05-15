l, c = 3, 3


def inpMatrice(c, l) -> list:
    M = []
    for i in range(c):
        ligne = []
        for j in range(l):
            val = int(input(f"M[{i}][{j}]= "))
            ligne.append(val)
        M.append(ligne)
    return M


def affMatrice(M) -> None:
    print("La matrice est")
    for ligne in M:
        for val in ligne:
            print(f"{val:4d}", end="")
        print()


def affTriangleInferieur(M: list) -> None:
    print("Sous-triangle inférieur")
    for i, ligne in enumerate(M):
        for j, val in enumerate(ligne):
            print(f"{val:4d}" if j <= i else "    ", end="")
        print()


def affTriangleSuperieur(M: list) -> None:
    print("Sous-triangle supérieur")
    for i, ligne in enumerate(M):
        for j, val in enumerate(ligne):
            print(f"{val:4d}" if j >= i else "    ", end="")
        print()


def cstFoisMatrice(M: list, n: int) -> list:
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] *= n
    return M

Y = [[3, 3, 5], [9, 8, 0], [8, 0, 8], [8, 0, 3]]
Z = [[3, 3, 5], [9, 5, 0], [8, 7, 8], [6, 5, 4]]


def someMatrice(A: list, B: list) -> list:
    n = len(A)
    m = len(A[0])
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C


M = inpMatrice(c, l)
affMatrice(M)
affTriangleInferieur(M)
affTriangleSuperieur(M)
