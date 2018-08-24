"""
Calculate the factorial for a given number.

Input:
The first line contains an integer 'T' denoting the total number of test cases. 
In each test cases, it contains an integer 'N'.

Output:
In each seperate line output the answer to the problem.

Example:
Input:
1
1

Output:
1
"""
def fact(n):
    if n == 0 or n==1:
        return 1
    return n* fact(n-1)
    
t = int(input())
while t > 0:
    n = int(input())
    print(fact(n))
    t -= 1