"""
Problem Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/maximize-the-earning-137963bc-323025a6/
"""
def rupeesEarned(buildings,cost):
    height = -1
    count = 0
    for building in buildings:
        if building > height:
            count += 1
            height = building
    return count*cost
    
for _ in range(int(input())):
    n,r = map(int,input().split())
    buildings = list(map(int,input().split()))
    print(rupeesEarned(buildings,r))