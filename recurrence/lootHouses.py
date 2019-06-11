memo = dict()
def loot(arr):
    if len(arr) in memo:
        return memo[len(arr)]

    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    memo[len(arr)] = max(arr[0] + loot(arr[2:]) , loot(arr[1:]) ) # take it OR leave it
    return memo[len(arr)]


def lootBasic(arr):

    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    return max(arr[0] + loot(arr[2:]) , loot(arr[1:]) ) # take it OR leave it


n = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]
print(loot(arr))
