"""
Problem Link: https://practice.geeksforgeeks.org/problems/sum-of-all-prime-numbers-between-1-and-n/0

Given a positive integer N, calculate the sum of all prime numbers between 1 and N(inclusive).

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. 
Each testcase contains one line of input containing N.

Output:
For each testcase, in a new line, print the sum of all prime numbers between 1 and N.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106

Example:
Input:
2
5
10
Output:
10
17
"""
def primeNo(n):
    arr = [1] * (n+1)
    arr[0] = arr[1] = 0
    i = 2
    while i * i <= n:
        if arr[i] == 1:
            for j in range(i*i,n+1,i):
                arr[j] = 0
        i += 1
    return arr

numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
n = max(numbers)
primeNumbers = primeNo(n)
summ = 0
for i in range(len(primeNumbers)):
    if primeNumbers[i] == 1:
        summ += i
    primeNumbers[i] = summ
for n in numbers:
    print(primeNumbers[n])