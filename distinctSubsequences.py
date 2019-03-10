def solution(word, s, outputD=""):
    if len(word) == 0:
        s.add(outputD)
        return

    # excluding the 0th letter
    solution(word[1:], s, outputD)
    # includong the 0th letter
    solution(word[1:], s, outputD + word[0])

t = int(input().strip())

for _ in range(t):
    word = input().strip()
    s = set()
    solution(word, s)
    print(len(s))
