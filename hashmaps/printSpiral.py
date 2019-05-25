def spiralPrint(arr):
    # base case
    if len(arr) == 0:
        return

    # print outer strip of the spiral
    n = len(arr) #num of rows
    m = len(arr[0]) # num of columns

    for i in range(m):
        print(arr[0][i], end = " ")

    for i in range(1, n):
        print(arr[i][m - 1], end = " ")

    for i in range(m - 2, -1, -1):
        print(arr[n - 1][i], end = " ")

    for i in range(n - 2, 0, -1):
        print(arr[i][0], end= " ")


    # call the inner spiral arr[1:n][1:m]
    new_arr = []
    for i in range(1, n - 1):
        art = []
        for j in range(1, m - 1):
            art.append(arr[i][j])
        new_arr.append(art)

    spiralPrint(new_arr)

#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
spiralPrint(arr)
