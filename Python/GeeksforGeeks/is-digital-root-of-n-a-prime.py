"""
Given a number N, you need to find if its digital root is prime or not. 
DigitalRoot of a number is the repetitive sum of its digits until we get a single digit number.
Eg.DigitalRoot(191)=1+9+1=>11=>1+1=>2

Input:
The first line of the input contains a single integer T, denoting the number of test cases. 
Then T test case follows. Each testcase contains a single line having N as input.

Ouput:
For each testcase, print 1 if the digitalRoot(N) is prime, else print 0.

Example:
Input:
3
89
45
12

Output:
0
0
1

Explanation:
For testcase 1: DigitalRoot(89)=>17=>1+7=>8; not a prime.
For testcase 3: DigitalRoot(12)=>1+3=>3; a prime number.
"""
def checkPrime(num):
    if num in [2,3,5,7]:
        return True
    return False
    
def digitalRoot(num): #reference- https://en.wikipedia.org/wiki/Digital_root
    if num < 10:
        return num
    return num % 9 if num % 9 != 0 else 9
    
t = int(input())
while t > 0:
    num = int(input())
    if checkPrime(digitalRoot(num)):
        print(1)
    else:
        print(0)
    t -= 1