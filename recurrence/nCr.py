
def C(n, r):
    # edge cases
    if r < 0 or r > n:
        return 0
        
    if r == 0 or r == n:
        return 1
    return C(n - 1, r - 1) + C(n - 1, r)

t = int(input().strip())
while t:
    n, r = map(int, input().strip().split())
    print(C(n, r))
    t-= 1
