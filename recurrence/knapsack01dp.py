## Read input as specified in the question.
## Print output as specified in the question.



# take this weight
# dont take this weight


def knapsackMaxValue(weights, values, w):
    memo = dict()
    #replace   i, j ->  return memo[(len(weights), w)]
    #Choose the filling Up direction
    # if weight is negative then not allowed
    for i in range(len(weights) + 1):

        for j in range(w + 1):
            if j == 0:
                return 0

            if i == 0:
                return 0

            # either do NOT take first value
            option1 = memo[(i - 1, j)]
            # take the first value THIS IS NOT THE INFINITE VERSION so consumption does take place
            if j - weights[len(weights) - i] >= 0:
                option2 = values[-i] + dp[i - 1, j - weights[len(weights) - i]]
            else: # cant take this if he next weight becomes negative
                option2 = 0
            memo[(i, j)] = max(option1, option2)

    return memo[(len(weights), w)]

n = int(input().strip())
weights = list(map(int, input().strip().split()))
values = list(map(int, input().strip().split()))
w = int(input().strip())
memo = dict()
print(knapsackMaxValue(weights, values, w))
