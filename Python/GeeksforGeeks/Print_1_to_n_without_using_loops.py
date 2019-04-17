"""
Print numbers from 1 to N without the help of loops.

Input: 
The first line of the input contains T, denoting the number of testcases. First line of test case contains an integer n.

Output: 
For each test case, print numbers from 1 to N in newline.

Constraints:
1 <= T <= 100
1 <= N <= 990

Example:
Input:
1
10

Output:
1 2 3 4 5 6 7 8 9 10
"""

def count(n):
    if n==1:
        return 1
    print(count(n-1),end=' ')
    return n
     

t = int(input())

while(t>0):
    n = int(input())
    print(count(n))
    t-=1