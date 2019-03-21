def minExpenditure(opening, closing, arr, n, memo):
    if (opening, closing) in memo:
        return memo[(opening, closing)]

    if opening > n or closing > n:
        return float('inf')

    if closing == n:
        return 0

    if opening == n: # must choose closing now
        memo[(opening, closing)] = arr[opening + closing][0] + minExpenditure(opening, closing + 1, arr, n, memo)
        return memo[(opening, closing)]

    if opening == closing:
        memo[(opening, closing)] = arr[opening + closing][1] + minExpenditure(opening + 1, closing, arr, n, memo)
        return memo[(opening, closing)]
    elif opening > closing:
        memo[(opening, closing)] = min(arr[opening + closing][1] + minExpenditure(opening + 1, closing, arr, n, memo), arr[opening + closing][0] + minExpenditure(opening, closing + 1, arr, n, memo))
        return memo[(opening, closing)]

    return float('inf')

def minExpenditureDP(arr):

    n = len(arr) // 2
    dp = [ [0] * (n + 1) for i in range(n + 1)]

    dp[n][n] = 0 # closing == n

    for i in range(n): # n - 1
        # must closing >  opening
        dp[i][n] = float('inf')
        #print(i, n)


     #dp[n][n] = 0 # closing == n

    for j in range(n - 1, -1, -1):
        # must close since opening == n
        # i(opening) == n
        # taking i + j current value, store cumulative starting from i + j till the end of arr
        dp[n][j] = arr[n + j][0] + dp[n][j + 1]
        #print(dp)


    for opening in range(n - 1, -1, -1):
        for closing in range(n - 1, -1, -1):
            if opening == closing: # must use opening
                dp[opening][closing] = arr[opening + closing][1] + dp[opening + 1][closing]
            elif opening > closing:
                option1 = arr[opening + closing][0] + dp[opening][closing + 1]
                option2 = arr[opening + closing][1] + dp[opening + 1][closing]
                dp[opening][closing] = min(option1, option2)
            else:
                dp[opening][closing] = float('inf')
            #print(dp[opening][closing])

    return dp[0][0]

N = int(input().strip())
arr = [tuple(map(int, input().strip().split())) for i in range(N)]
memo = dict()
#print(minExpenditure(0, 0, arr, N // 2, memo))
print(minExpenditureDP(arr))
