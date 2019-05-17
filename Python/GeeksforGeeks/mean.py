"""
Problem Link: https://practice.geeksforgeeks.org/problems/mean/0

Given the marks of all students, calculate the mean.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case there will be two lines. 
The first line contains the integer N denoting the number of students, and second line contains the N space seperated integrers 
denoting the marks of all the students.

Output:
Corresponding to each test case, print the floor value of the mean in a new line.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= Marks <= 100

Example:
Input:
3
4
56 67 30 79
4
78 89 67 76
5
90 100 78 89 67
Output:
58
77
84
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sum(arr)//n)