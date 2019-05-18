"""
Problem Link: https://practice.geeksforgeeks.org/problems/pascal-triangle/0

Given a positive integer K, return the Kth row of pascal triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.

Example :
1
1 1
1 2 1
1 3 3 1
For K = 3, return 3rd row i.e 1 2 1

Input:
First line contains an integer T, total number of test cases. Next T lines contains an integer N denoting the row of triangle to be printed.

Output:
Print the Nth row of triangle in a separate line.

Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 25

Example:
Input:
1
4
Output:
1 3 3 1
"""
for _ in range(int(input())):
    line = int(input())
    no = 1
    for i in range(1,line+1):
        print(no,sep=' ',end=' ')
        no = no * (line-i)//i
    print()