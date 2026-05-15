A = [5, 3, 5, 4, 6, 11, 4, 7]
for k in range(len(A) - 1):
    for i in range(len(A) - 1 - k):
        if A[i + 1] < A[i]:
            A[i + 1], A[i] = A[i], A[i + 1]
            print(A)
