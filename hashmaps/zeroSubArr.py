## Read input as specified in the question.
## Print output as specified in the question.

def zeroSubArray(nums):

    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if sum(nums[i:j + 1]) == 0:
                return True

    return False

n = int(input())

nums = list(map(int, input().strip().split()))

print("true" if zeroSubArray(nums) else "false" )
