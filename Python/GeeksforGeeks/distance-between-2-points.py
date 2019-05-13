"""
Problem Link: https://practice.geeksforgeeks.org/problems/distance-between-2-points/0

Given coordinates of 2 points on a cartesian plane, output the distance between them rounded up to nearest integer.

Input:
The first line of the input contains the number of test cases T. For each test case there will be single line containing 4 integers denoting the 2 co-ordinates 
(x1,y1) and (x2,y2).

Output: 
For each test case print in a single line the distance between the two points.

Constraints:
1 <= T <= 100
-1000000 <= |x1,x2,y1,y2| <= 1000000

Example: 
Input:
4
0 0 2 -2
-20 23 -15 68
30 37 79 -51
-69 63 57 11

Output:
3
45
101
136
"""
for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    print(round(((x2-x1)**2 + (y2-y1)**2)**0.5))