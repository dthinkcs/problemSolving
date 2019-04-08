## Read input as specified in the question.
## Print output as specified in the question.

def solve(arr, memo, smokeTillNow=0, currIndex=0):

    # TODO memoize the length, smokeTillNow and currIndex
    tup = (len(arr), smokeTillNow, currIndex)
    if tup in memo :
        return memo[tup]

    if len(arr) == 1:
        memo[tup] = smokeTillNow
        return smokeTillNow

    if currIndex >= len(arr) - 1:
        memo[tup] = float('inf')
        return float('inf')


    # first option: skip the currIndex
    firstOption = solve(arr, memo, smokeTillNow, currIndex + 1)

    # second option
    A = arr[currIndex]
    B = arr[currIndex + 1]
    secondOption = solve(arr[ : currIndex] + [ (A + B) % 100 ] +  arr[currIndex + 2: ], memo, smokeTillNow + A * B)

    memo[tup] = min(firstOption, secondOption)
    return memo[tup]


n = int(input().strip())
arr = list(map(int, input().strip().split()))
memo = dict()
print(solve(arr, memo))
