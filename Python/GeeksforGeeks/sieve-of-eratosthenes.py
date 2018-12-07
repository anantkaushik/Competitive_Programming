"""
Problem Link: https://practice.geeksforgeeks.org/problems/sieve-of-eratosthenes/0

Given a number N, calculate the prime numbers upto N using Sieve of Eratosthenes.  

Input: 
The first line of the input contains T denoting the number of testcases. T testcases follow. 
Each testcase contains one line of input containing N.

Output: 
For all testcases, in a new line, print all the prime numbers upto or equal to N.

Constraints:
1 <= T<= 100
1 <= N <= 104

Example:
Input:
2
10
35

Output:
2 3 5 7
2 3 5 7 11 13 17 19 23 29 31 
"""
def countPrimes(n):
    if n < 2:
        return 0
    prime = [1]*(n+1)
    prime[0] = prime[1] = 0
    i = 2
    while i*i <= n:
        if prime[i] == 1:
            for j in range(i*i,n+1,i):
                prime[j] = 0 
        i+=1
    return prime
        
for _ in range(int(input())):
    n = int(input())
    prime = countPrimes(n)
    for i in range(len(prime)):
        if prime[i] == 1:
            print(i,end = ' ')
    print()