
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

i = 0
while i < len(arr):
    if arr[i] == 0:
        del arr[i]
    else:
        i += 1

print(arr)
