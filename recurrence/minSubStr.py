## Read input as specified in the question.
## Print output as specified in the question.


def fill(s, ht):
    for c in s:
        ht[c] = ht.get(c, 0) + 1

def ht2InHt1(ht1, ht2):

    for k in ht2:
        if k not in ht1:
            return False
        if ht2[k] > ht1[k]:
            return False

    return True


mainStr = input().strip()
subStr = input().strip()

ht2 = dict()
fill(subStr, ht2)

minSoFar = float('inf')

for i in range(len(mainStr)):
    for j in range(i, len(mainStr)):
        currStr = mainStr[i: j + 1]
        ht1 = dict()
        fill(currStr, ht1)

        if ht2InHt1(ht1, ht2):
            currLen = len(currStr)

            if currLen < minSoFar:
                minSoFar = currLen
                minStr = currStr

if minSoFar != float('inf'):
    print(minStr)
else:
    print("null")
