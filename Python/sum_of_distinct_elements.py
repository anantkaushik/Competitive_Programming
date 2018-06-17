"""
Find the sum of all non- repeated elements in an array.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N, N is the size of array.
The second line of each test case contains N input C[i].

Output:
Print the sum of all non-repeated elements.

Example:
Input:
3
5
1 2 3 4 5
5
5 5 5 5 5
4
22 33 22 33

Output:
15
5
55
"""
t = int(input())
while t > 0:
    n = input()
    s = set(map(int,input().split()))
    print(sum(s))
    t -= 1