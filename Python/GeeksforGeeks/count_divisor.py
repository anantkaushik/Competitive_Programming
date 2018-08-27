"""
Given two numbers, p and q. Find the number of common divisors of p and q. 

Input: 
Each input consists of T,the number of test cases. Each test case consists of two integers p and q.

Output:
Output consists of a single line denoting the number of common divisiors of p and q.

Example:
Input:

2
2 4
3 5

Output:
2
1
"""
def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a
    
t = int(input())
while t > 0:
    a,b = map(int,input().split())
    cd = 0
    n = gcd(a,b)+1
    for i in range(1,n):
        if a % i == 0 and b % i == 0:
            cd+=1
    print(cd)
    t -= 1