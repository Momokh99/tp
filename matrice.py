n, m = 3, 4
M = [[0] * m for _ in range(n)]

M = []


def inpMatrice(M, n, m):
    n, m = 3, 4
    M = [[0] * m for _ in range(n)]
    M = []
    for i in range(n):
        ligne = []
        for j in range(m):
            val = int(input(f"M[{i}][{j}]="))
            ligne.append(val)
        M.append(ligne)
    return M


def affMatrice(M):
    print("la matrice est")
    for ligne in M:
        for val in ligne:
            print(f"{val:4d}", end="")


Y = [[3, 3, 5], [9, 8, 0], [8, 0, 8], [8, 0, 3]]
Z = [[3, 3, 5], [9, 5, 0], [8, 7, 8], [6, 5, 4]]


def someMatrice(A, B):
    n = len(A)
    m = len(A[0])
    C = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C
