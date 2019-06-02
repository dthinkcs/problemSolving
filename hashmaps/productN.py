

k = int(input())
nums = list(map(int, input().strip().split()))
seen = set()

for n in nums:
    if k % n == 0 and k // n in seen:
        print(k // n, n)
    seen.add(n)
