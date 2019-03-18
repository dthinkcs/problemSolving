t = int(input())

for _ in range(t):

    N, C = tuple(map(int, input().strip().split()))
    arr = [0] * (N +1)

    for __ in range(C):

        lt = list(map(int, input().strip().split()))

        if lt[0] == 0:
            for i in range(lt[1], lt[2] + 1):
                arr[i] += lt[3]
        else:
            print(sum(arr[lt[1]: lt[2] + 1]))
