"""
Given a number n, the task is to find the even factor sum of a number.

INPUT : The first line consists of an integer T i.e. the number of test cases. First and last line of each test case consists of an integer n.

OUTPUT : Print the sum of even factors of the given integer n.

EXAMPLES:
INPUT :
2
30
18

OUTPUT : 
48
26

EXPLANATION :
Input : 30
Output : 48
Even dividers sum 2 + 6 + 10 + 30 = 48

Input : 18
Output : 26
Even dividers sum 2 + 6 + 18 = 26
"""
t = int(input())
while t > 0:
    n = int(input())
    sum = 0
    for i in range(2,n+1,2):
        if n % i == 0:
            sum += i
    print(sum)
    t -= 1