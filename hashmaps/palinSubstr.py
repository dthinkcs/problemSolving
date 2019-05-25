def isPalin(w):
    return w[::-1] == w



s = input()
count = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        if isPalin(s[i: j + 1]):
            count += 1


print(count)
