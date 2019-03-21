def numOfBraces(n, s, opening=0, closing=0):

    if ((opening + closing + 1) in s):
        return numOfBraces(n, s, opening + 1, closing)

    if opening > n or closing > n:
        return 0

    if closing == n:
        return 1

    if opening == n:
        return numOfBraces(n, s, opening, closing + 1)


    if opening == closing :
        return numOfBraces(n, s, opening + 1, closing)
    elif opening > closing:
        return numOfBraces(n, s, opening + 1, closing) + numOfBraces(n, s, opening, closing + 1)

    return 0 # closing > opening

t = int(input().strip())

for _ in range(t):
    n, k = tuple(map(int, input().strip().split()))
    s = list(map(int, input().strip().split()))
    print(numOfBraces(n, s))
