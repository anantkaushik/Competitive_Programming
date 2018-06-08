"""
Given a number n, check if it is Full Prime or not.  
Note : A full prime number is one in which the number itself is prime and all its digits are also prime.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. 
Then T test case follows, a single line of the input containing a positive integer N.

Output:
Print 'Yes' if it is full prime,otherwise print 'No'.

Input:
2
53
41

Output:
Yes
No
"""
def prime(no):
    if no == 1:
        return False
    else:
        for i in range(2,(no//2)+1):
            if no % i == 0:
                return False
        return True

def digit(n):
    while n > 0:
        temp = n % 10
        if prime(temp):
            n = n//10
        else:
            return False
    return True
t = int(input())

while t > 0:
    n = int(input())
    if prime(n):
        if digit(n):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    t -= 1