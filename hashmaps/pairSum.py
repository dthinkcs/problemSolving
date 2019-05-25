

def pairSum0(l):
#Implement Your Code Here(
    ht = dict()

    for n in l:
        ht[n] = ht.get(n, 0) + 1

    seen = set()
    for n in ht.keys():
        if -n in ht and n not in seen and -n not in seen :
            s = str(min(n, -n)) + " " + str(max(n, -n)) + "\n"
            print(s * (ht[n] * ht[-n]), end="")
            seen.add(n)
            seen.add(-n)


    # seen = set()
    #
    # for n in l:
    #     if -n in seen:
    #         print(str(min(n, -n)) + " " + str(max(n, -n)))
    #     seen.add(n)
    #

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pairSum0(l)
