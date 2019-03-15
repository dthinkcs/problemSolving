n = int(input().strip())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

q = int(input().strip())

for _ in range(q):
    l, r = tuple(map(int, input().strip().split()))

    max_ele = max(A[l - 1: r])
    lt1 = []
    for i in range(l - 1, r):
        if A[i] == max_ele:
            lt1.append(i)


    min_b = float('inf')
    for idx in lt1:
        if B[idx] < min_b:
            min_b = B[idx]


    lt2 = []
    for idx in lt1:
        if B[idx] == min_b:
            lt2.append(idx)

    print(lt2[0] + 1)
