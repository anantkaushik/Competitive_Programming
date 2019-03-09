"""
Problem Link: https://practice.geeksforgeeks.org/problems/armstrong-numbers/0

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
def isArmstrong(n):
    cube = 0
    temp = n
    while temp:
        cube += (temp % 10)**3
        temp //= 10
    return "Yes" if cube == n else "No"
    
for _ in range(int(input())):
    n = int(input())
    print(isArmstrong(n))
