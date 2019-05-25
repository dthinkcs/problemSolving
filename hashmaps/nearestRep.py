## Read input as specified in the question.
## Print output as specified in the question.

_ = int(input())
nums = list(int(i) for i in input().strip().split(' '))

ht = dict()
for n in nums:
    ht[n] = ht.get(n, 0) + 1

htarr = dict()
for i in range(len(nums)):
    n = nums[i]
    if ht[n] > 1:
        if n not in htarr:
            htarr[n] = [i]
        else:
            htarr[n].append(i)

for e in htarr:
