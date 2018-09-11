"""
Ishaan has been learning different representations of numbers, like binary, octal, decimal, etc. 
He has an assignment of a lot of problems. He is given 2 integers N and K.
Ishaan needs to convert N (given in decimal) and convert it to base K. Help him calculate the answer.

Input : 
First line of input contains a single integer T denoting the number of test cases.
The only line of each test case contains 2 space-separated integers N and K.

Output : 
For each test case, print the required answer in a new line.

Example : 
Input : 
3
10 2
4 8
15 6
Output : 
1010
4
23

Explanation : 
Case 1 : 
10 in Binary = 1010
Case 2 : 
4 in Octal = 4
Case 3 : 
15 in Base 6 = 23
"""
t = int(input())
while t > 0:
    n,k = map(int,input().split())
    ans = ""
    while n >= k:
        ans += str(n%k)
        n = n//k
    ans +=str(n)
    print(ans[::-1])
    t -= 1