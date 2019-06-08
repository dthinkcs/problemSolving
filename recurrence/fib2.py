
M = pow(10, 9) + 7

def fib(n):
    curr, next = 0, 1
    for _ in range(1, n + 1):
        curr, next = next, (curr + next) % M
    return curr

t = int(input().strip())
while t:
    n = int(input().strip())
    print(fib(n))
    t-= 1
