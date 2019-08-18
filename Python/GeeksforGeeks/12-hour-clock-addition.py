"""
Problem Link: https://practice.geeksforgeeks.org/problems/12-hour-clock-addition/0

Given two positive integers num1 and num2, the task is to find the sum of the two numbers on a 
12 hour clock rather than a number line.

Input
First line of the input contains an integer T denoting the number of test cases. 
For each test case there will be single line containing two space seperated integers.

Output
Corresponding to each test case, print the sum in a new line.

Constraints:
1 <= T <= 100
0 <= num1 <= 50
0 <= num2 <= 50

Example:
Input:
2
7 5
3 5

Output
0
8
"""
def get_time(t1, t2):
    time = t1 + t2
    if time < 12:
        return time
    return time % 12
    
for _ in range(int(input())):
    t1,t2 = map(int,input().split())
    print(get_time(t1,t2))