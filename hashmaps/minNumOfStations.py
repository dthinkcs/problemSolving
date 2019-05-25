
count = 0
while len(trains) != 0:
    # take a greedy route,
    # remove the trains taken in that route
    # increment count by 1
    trains = sorted(trains, key=lambda ele: ele['t2'])
    for train in trains:
        
