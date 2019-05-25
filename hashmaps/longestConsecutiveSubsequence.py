
def fill(ht, l):
    for n in l:
        ht[n] = ht.get(n, 0) + 1

def longestConsecutiveSubsequence(l):
#Implement Your Code Here
#You have To Return the list of longestConsecutiveSubsequence
    ht = dict()
    fill(ht, l)
    new_list = []
    max_list = []
    index_smallest = len(l)
    for n in l:
        if ht[n] > 0:
            # go above
            new_list = []
            i = n
            while i in ht and ht[i] > 0:
                new_list.append(i)

                ht[i] -= 1
                i += 1

            # go below
            i = n - 1
            while i in ht and ht[i] > 0:
                new_list.append(i)

                ht[i] -= 1
                new_index = i
                i -= 1 # GOOD STRATEGY COZ LAST ELEMENT IS  THE SMALLEST

        if len(new_list) > len(max_list) or len(new_list) == len(max_list) and  new_index < index_smallest:
            max_list = new_list
            index_smallest = new_index



    return max_list



n=int(input())
l=list(int(i) for i in input().strip().split(' '))
final = longestConsecutiveSubsequence(l)
for num in final:
    print(num)
