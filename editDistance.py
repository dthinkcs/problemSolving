def editDistance(s, t, memo = dict()):
    #BUG#if len(s) == 0 or len(t) == 0:
    #    return

    if (s, t) in memo:
        return memo[(s, t)]

    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)
    if s[0] == t[0]:
        memo[(s, t)] = editDistance(s[1:], t[1:])
    else:
        subAns = 1 + editDistance(s[1:], t[1:])
        insAns = 1 + editDistance(s, t[1:])
        delAns = 1 + editDistance(s[1:], t)
        memo[(s, t)] = min(subAns, insAns, delAns)
    return memo[(s, t)]

s = 'a cat!' * 10#input()
t = 'the cats!' * 10#input()
print(editDistance(s, t))
