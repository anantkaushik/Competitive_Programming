"""
Problem Link: https://practice.geeksforgeeks.org/problems/count-zero/0

Given a number d, representing the number of digits of a number. Find the total count of positive integers 
which have at-least one zero in them and consist d or less digits.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is D,D is number of digits.

Output:
Print the total count of positive integers which have at-least one zero in them.

Constraints:
1 ≤ T ≤ 15
1 ≤ N ≤ 15

Example:

Input:
2
2
3

Output:
9
180
"""
for _ in range(int(input())):
    n = int(input())
    print((9*((10**n)-1)//9) - (9*((9**n)-1)//8))