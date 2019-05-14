"""
Find total number of Squares in a N*N cheesboard.

Input:
The first line contains an integer T, depicting total number of test cases. Then following T lines contains an integer N that is the side of the chessboard.

Output:
Each seperate line showing the maximum number of squares possible.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100

Example:
Input:
2
1
2

Output:
1
5
"""

t = int(input())

while t>0:
    n = int(input())
    sumn = 0
    while n>0:
        sumn = sumn + (n * n)
        n-=1
    print(sumn)
    t-=1
