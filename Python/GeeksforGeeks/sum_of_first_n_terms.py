"""
Given and integer n. Print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till n-th term.

Input:
The first line consists of an integer T i.e number of test cases. The first and only line of each test case 
consists of an integer n. As the output could be large so take mod with 109+7.

Output:
Print the required sum.

Example:
Input:
2
5
7

Output:
225
784
"""

t = int(input())
while t > 0:
    n = int(input())
    sum = (((n*(n+1))//2)**2)%1000000007 
    # 1^3 + 2^3 + 3^3 + ... + n^3 = ((n*(n+1))/2)^2
    print(sum)
    t -= 1
