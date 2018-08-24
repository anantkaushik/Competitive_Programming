"""
You have to merge the two sorted arrays into one sorted array (in non-increasing order)

Input:
First line contains an integer T, denoting the number of test cases.
First line of each test case contains two space separated integers X and Y, denoting the size of the 
two sorted arrays.Second line of each test case contains X space separated integers, denoting the first 
sorted array P.Third line of each test case contains Y space separated integers, denoting the second array Q.

Output:
For each test case, print (X + Y) space separated integer representing the merged array.

INPUT:
1
4 5
7 5 3 1
9 8 6 2 0

OUTPUT:
9 8 7 6 5 3 2 1 0
"""
t = int(input())
while t > 0:
    a = input()
    x = list(map(int,input().split()))
    x += list(map(int,input().split()))
    x.sort()
    print(*x[::-1])
    t -= 1