
def fact(n, memo):
    if n in memo:
        return memo[n]

    if n == 0:
        return 1

    memo[n] = n * fact(n - 1, memo)
    return memo[n]

t = int(input().strip())
memo = dict()
while t:
    n = int(input().strip())
    print(fact(n, memo))
    t -= 1
