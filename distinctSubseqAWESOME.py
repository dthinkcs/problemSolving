M = 1000000007

'''
    AAAAAA :- arr[i] -= sub WORKS!!!
    AAABAAC :- must also add condition that if sub == 0: arr[i] + arr[i - 1] * 2 - sub
    AAABABA :- DOESNT WORK
'''

# [1, 2, 3, 4, 5, 6, ]

def solution(s):

    lastOcc = dict()

    arr = [0] * (len(s) + 1)

    arr[0] = 1

    for i in range(1, len(s) + 1):
        str_index = i - 1
        curr_char = s[str_index]
        if curr_char in lastOcc:
            arr[i] = arr[i - 1] * 2 - arr[lastOcc[curr_char]]
        else:
            arr[i] = arr[i - 1] * 2
        lastOcc[curr_char] = str_index

    return arr[len(s)]

def solution3(s):

    arr = [0] * (len(s) + 1)

    arr[0] = {''}

    for i in range(1, len(s) + 1):
        s_old = arr[i - 1]
        s_new = s_old.copy()
        for ele in s_old:
            s_new.add(ele + s[i - 1])
        arr[i] = s_new

    return (len(arr[len(s)]))



def solution2(s):

    arr = [0] * (len(s) + 1)

    arr[0] = 1
    arr[1] = 2

    for i in range(2, len(s) + 1):
        arr[i] = 1
        sub = 0
        # arr[i] = arr[i - 1] * 2 #- subtractionValue(s[i - 1], s[ : i - 1]) % M
        for j in range(i):
            arr[i] += arr[j]

            if j > 0 and s[j - 1] == s[i - 1]:
                sub += arr[j - 1]
        if sub == 0:
            arr[i] = arr[i - 1] * 2 - sub
        else:
            arr[i] -= sub

    return arr[len(s)]

t = int(input())
for _ in range(t):
    word = input().strip()
    print(solution(word))
