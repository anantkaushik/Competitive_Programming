"""
Problem Link: https://practice.geeksforgeeks.org/problems/average/0

Given a stream of numbers, print average or mean of the stream at every point.

Input: The first line of input contains an integer T denoting the number of test cases.
For each test case there will be two lines. The first line contains an integer N denoting the size of array C[], and second line contains N 
space seperated integers C[i].

Output:
Print the average of the stream at every point (in integer).

Constraints:
1 ≤ T ≤ 20
1 ≤ N ≤ 50
1 ≤ C[i] ≤ 100

Example:
Input
2
5
10 20 30 40 50
2
12 2

Output
10 15 20 25 30
12 7
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    res = []
    summ = 0
    for i in range(n):
        summ += arr[i]
        res.append(summ//(i+1))
    print(*res)