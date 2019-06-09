
def C(n, r, memo):
    # edge cases
    if (n, r) in memo:
        return memo[(n, r)]

    if r < 0 or r > n:
        return 0

    if r == 0 or r == n:
        return 1
    memo[(n, r)] = C(n - 1, r - 1, memo) + C(n - 1, r, memo)
    return memo[(n, r)]

t = int(input().strip())
memo = dict()
while t:
    n, r = map(int, input().strip().split())
    print(C(n, r, memo))
    t-= 1
