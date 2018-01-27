"""Given a List of Distinct N number a1,a2,a3........an.
Find The Position Of Number K In The Given List.

Input Format
First Line Take Input Value Of N
Second Line Take Input N Space Separated Integer Value
Third Line Take Input Value Of K
Output Format
Position Of K In The Given List

Sample Input:
5
1 2 3 4 5
4
Sample Output:
3
"""
N = int(input())
arr = list(map(int,input().split()))
K = int(input())
for i in range(N):
    if (K == arr[i]):
        print(i)