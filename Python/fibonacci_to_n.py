"""
Given a positive integer N, print the Fibonacci series till the number N. 
If N is a part of the series, print N as well.

Input:
The first line of input is an integer T, denoting the number of test cases. 
For each test case, input an integer N, denoting the number up to which Fibonacci needs to be printed.

Output:
For each test case, there is only one line of input that will comprise of space separated elements 
of the Fibonacci series.

Example:
Input:
3
5
15
50
Output:
0 1 1 2 3 5
0 1 1 2 3 5 8 13
0 1 1 2 3 5 8 13 21 34

Explanation:
In the first test case, 5 is the number up to which the series needs to be printed. 
5 is also a part of the series hence the output is printed till 5.
In the second test case, the maximum element of Fibonacci series which is less than or equal to 15 is 13. 
The output is printed till 13.
Similarly, in the third test case, 34 is the maximum element less than or equal to 50. 
So, the output is printed till 34.
"""
t = int(input()) #taking the no of testcases
series = [0,1] #fibonacci series
def fib(n):
    l = len(series)
    if(series[l-1] > n): #if needed fibonacci series already exist
        for i in range(0,l):
            if series[i] > n :
                print(*series[:i])
                break
    else: #if needed fibonacci series does not exist.
        a = series[l - 2] 
        b = series[l - 1]
        while True:
            c = a + b
            if c > n:
                break
            series.append(c) #adding values to the existing fibonacci series
            a = b
            b = c
        print(*series)
while t > 0:
    n = int(input())
    fib(n)
    t -= 1