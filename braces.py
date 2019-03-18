
def numOfBraces(n, opening=0, closing=0):

    if opening > n or closing > n:
        return 0

    if closing == n:
        return 1

    if opening == n:
        return numOfBraces(n, opening, closing + 1)

    if opening > closing:
        return numOfBraces(n, opening + 1, closing) + numOfBraces(n, opening, closing + 1)
    elif opening == closing:
        return numOfBraces(n, opening + 1, closing)
    return 0 # closing > opening


n = int(input().strip())
print(numOfBraces(n))
