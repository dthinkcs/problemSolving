def isPalindrome(s):
    s = s.lower()

    #remove all non alpha characters
    snew = ""
    for c in s:
        if c.isalpha():
             snew += c
    print(snew)

    return snew[::-1] == snew
