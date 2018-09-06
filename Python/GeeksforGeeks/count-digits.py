"""
Problem Link: https://practice.geeksforgeeks.org/problems/count-digits/0

Given a number N. You need to write a program to count the number of digits in N which evenly divides N.

Input:
First line of input contains an integer T which denotes the number of test cases. T test cases follows. 
First line of each test case contains a single integer N.

Output:
For each test case in a new line print the total number of digits of N which evenly divides N.

Input:
3
12
1012
23
Output:
2
3
0
"""
for _ in range(int(input())):
    n = int(input())
    temp,count = n,0
    while temp > 0:
        if temp%10 != 0 and n % (temp%10) == 0:
            count += 1 
        temp//=10
    print(count)