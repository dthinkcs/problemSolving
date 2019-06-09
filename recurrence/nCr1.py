
def C(n, r):

    memo = dict()
    for i in range(0, n  +1):
        for j in range(0, r  +1):
            if j < 0 or j > i:
                memo[(i, j)] = 0

            elif j == 0 or j == n:
                memo[(i, j)] = 1
            else: # elif is point of bug
                memo[(i, j)] = memo[(i - 1, j - 1)] + memo[(i - 1, j)]
    return memo[(n, r)]

t = int(input().strip())
while t:
    n, r = map(int, input().strip().split())
    print(C(n, r))
    t-= 1
