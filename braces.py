def numOfBraces(n, s, opening, closing, memo):

    if (opening, closing) in memo:
        return memo[(opening, closing)]



    if opening > n or closing > n:
        return 0

    if closing == n:
        return 1

    if opening == n:
        memo[(opening, closing)] = numOfBraces(n, opening, closing + 1, memo)
        return memo[(opening, closing)]

    if opening == closing :
        memo[(opening, closing)] =  numOfBraces(n, opening + 1, closing, memo)
        return memo[(opening, closing)]
    elif opening > closing:
        memo[(opening, closing)] =  numOfBraces(n, opening + 1, closing, memo) + numOfBraces(n, s, opening, closing + 1, memo)
        return memo[(opening, closing)]

    memo[(opening, closing)] = 0
    return memo[(opening, closing)] # closing > opening

t = int(input().strip())

for _ in range(t):
    n, k = tuple(map(int, input().strip().split()))
    s = list(map(int, input().strip().split()))
    memo = dict()
    print(numOfBraces(n, s, 0, 0, memo))
