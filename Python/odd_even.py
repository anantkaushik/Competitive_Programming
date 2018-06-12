"""
Given a positive integer determine whether it is odd or even.

Input:
First line contains an integer T, the number of test cases. Each test case contains a positive integer N.

Output:
In each seperate line print "odd" if odd and "even" if even.(Dont print the quotes)

Example:
Input:
1
23

Output:
odd
"""
t = int(input())
while t > 0:
    n = int(input())
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
    t -= 1