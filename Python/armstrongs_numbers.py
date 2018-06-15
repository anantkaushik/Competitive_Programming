"""
For a given 3 digit number, find whether it is armstrong number or not. An Armstrong number of three 
digits is an integer such that the sum of the cubes of its digits is equal to the number itself. 
For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371

Input:
First line contains an integer, the number of test cases 'T' Each test case should contain a positive integer N.

Output:
Print "Yes" if it is a armstrong number else print "No".

Example:
Input:
1
371

Output:
Yes
"""
t = int(input())
while t > 0:
    n = int(input())
    cube = 0
    temp = n
    while temp > 1:
        temp1 = temp % 10
        temp //= 10
        cube += temp1**3
    if cube == n:
        print("Yes")
    else:
        print("No")
    t -= 1