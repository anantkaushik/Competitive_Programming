"""
It’s time to find out which player is consistent in cricket. You need to calculate the average of a
player based on his score. Player average is defined as total runs scored by a player in N matches
divided by the number of matches in which he gets out. If the answer is too large you need to print
“-1” (without inverted comma’s).

Input:

The first line of the input contains T denoting number of test cases.
First line of each test case contains N denoting number of matches.
Next N line contains an integer denoting the number of runs scored by player in that match 
followed by a string which can be "out" or "notout" depending on whetherthe player is out or 
not-out in the match.

Output:
You need to print average of the player. If answer is not an integer take ceil and print your answer.

Example:
Input:
1
5
40 out
20 notout
13 out
60 notout
100 out
Output:
78
"""
import math
t = int(input())
while t > 0:
    n = int(input())
    out = 0
    runs = 0
    while n > 0:
        r,s = map(str,input().split())
        runs += int(r)
        if s == "out":
            out += 1
        n -= 1
    print(math.ceil(runs/out) if out!=0 else -1)
    t -= 1