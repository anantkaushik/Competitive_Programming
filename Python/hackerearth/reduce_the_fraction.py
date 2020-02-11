"""You are given a fraction - A/B.
Reduce the fraction to the lowest possible.

Input
First line consist of T - the number of test cases.
T lines follows - each consisting of 2 numbers A B

Output
Output T lines - In each line print the answer in the form P/Q.

SAMPLE INPUT 
2
6 8
12 13

SAMPLE OUTPUT 
3/4
12/13
"""
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
n = int(input())
while n>0 :
    a,b=map(int,input().split())
    gn = gcd(a,b)
    r1 = int(a/gn)
    r2 = int(b/gn)
    print("%d/%d"%(r1,r2))
    n-=1