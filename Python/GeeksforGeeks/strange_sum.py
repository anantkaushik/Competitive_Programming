"""
Given two non-negative numbers X and Y. The task is calculate the sum of X and Y.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case contains two numbers X and Y.

Output:
For each test case, if the number of digits in sum (X+Y) are equal to the number of digits in X, 
then print sum, else print X.

Example:
Input:
2
25 23
3 5

Output:
48
8
"""
t = int(input())
while t > 0:
    x,y = map(int,input().split())
    summ = x + y
    if len(str(x)) == len(str(summ)):
        print(summ)
    else:
        print(x)
    t -= 1