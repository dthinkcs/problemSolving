
n, total_value = tuple(map(int, stringinput.split()))
coins_arr = list(map(int, input().strip().split()))

arr = [[0] * (total_value + 1)] * (len(coins_arr) + 1)

for i in range(total_value + 1):
    arr[0][i] = float('inf')

for i in range((len(coins_arr) + 1)):
    arr[i][0] = 0

for i in range(1, len(coins_arr) + 1):
    for j in  range(1, total_value + 1):
        #arr[i] = min(arr[i - 1][j], 1 + arr[i][j - coins_arr[len(coins_arr) - i]])
        a = arr[i - 1][j]
        b = float('inf')
        if len(coins_arr) - i >= 0:
            b = 1 + arr[i][j - coins_arr[len(coins_arr) - i]]
        arr[i][j] = min(a, b)

print(arr[len(coins_arr)][total_value])
