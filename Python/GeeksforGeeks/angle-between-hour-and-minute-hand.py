"""
Problem Link: https://practice.geeksforgeeks.org/problems/angle-between-hour-and-minute-hand/0

Calculate the angle between hour hand and minute hand.
There can be two angles between hands, we need to print minimum of two. Also, we need to print floor of final result angle. 
For example, if the final angle is 10.61, we need to print 10.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. 
Each test case consists of one line conatining two space separated numbers h and m where h is hour and m is minute.

Output:
Coresponding to each test case, print the angle b/w hour and min hand in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ h ≤ 12
1 ≤ m ≤ 60

Example:
Input
2
9 60
3 30

Output
90
75
"""
def calcAngle(h,m):
    h = 0 if h == 12 else h
    m = 0 if m == 60 else m
    hourAngle = (h*60 + m)*0.5
    minuteAngle = m * 6
    angle = abs(hourAngle - minuteAngle)
    return angle if angle < (360-angle) else 360-angle
    
for _ in range(int(input())):
    h,m = map(float,input().split())
    print(int(calcAngle(h,m))