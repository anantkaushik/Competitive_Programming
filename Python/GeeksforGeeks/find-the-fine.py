"""
Given an array of penalties, an array of car numbers and also the date. 
The task is to find the total fine which will be collected on the given date. 
Fine is collected from odd-numbered cars on even dates and vice versa.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case consists of three lines. 
First line of each test case contains two integers N & Date, second line contains N space 
separated car numbers and third line contains N space separated penalties.

Output:
For each test case,In new line print the total fine.

Example:
Input:
2
4 12
2375 7682 2325 2352
250 500 350 200
3 8
2222 2223 2224
200 300 400

Output:
600
300
"""
t = int(input())
while t > 0:
    n,d = map(int,input().split())
    carNumber = list(map(int,input().split()))
    fine = list(map(int,input().split()))
    collected_fine = 0
    if d % 2 == 0:
        for i in range(n):
            if carNumber[i] % 2 != 0:
                collected_fine += fine[i]
    else:
        for i in range(n):
            if carNumber[i] % 2 == 0:
                collected_fine += fine[i]
    print(collected_fine)
    t -= 1