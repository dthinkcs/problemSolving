def fn(nums):
    seen = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            tot = nums[i] + nums[j]

            if tot in seen:
                return True

            seen.add(tot)

    return False

n = int(input().strip())
nums = list(map(int, input().strip().split()))

print("true" if fn(nums) else "false")
