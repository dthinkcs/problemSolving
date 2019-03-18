def minExpenditure(opening=0, closing=0, arr, n):
    if closing > opening or opening > n or closing > n:
        return float('inf')

    if closing == n:
        return arr[-1][1]

    openingOption = float('inf')
    closingOption = float('inf')
    if opening == n: # must choose closing now
        return arr[opening + closing][1] + minExpenditure(opening + 1, closing + 1, arr, n)
    elif opening == closing : # 2

    else: opening < n




N = int(input().strip())

arr = [tuple(map(int, input().strip().split())) for _ in range(N)]
print(minExpenditure(arr, N // 2))
