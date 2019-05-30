"""
Problem Link: https://practice.geeksforgeeks.org/problems/convert-from-any-base-to-decimal/0

Given a number and its base, convert it to decimal. The base of number can be anything such that all digits can be represented using 0 to 9 and A to Z. 
Value of A is 10, value of B is 11 and so on.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is the base and second line of test 
case is the number which is to be converted to decimal.

Output:
Decimal conversion of the given number is displayed in the output.

Constraints:
1 <= T <= 5
2 <= base <=16
1 <= N <= decimal equivalents till 999999999

Example:

Input:
3
2 
1100
16
11A
8
123

Output:
12
282
83
"""
for _ in range(int(input())):
    base = int(input())
    no = input()
    decimalNo = 0
    power = 1
    hexaDict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for c in no[::-1]:
        if c.isdigit():
            decimalNo += power*int(c)
        else:
            decimalNo += power*hexaDict[c]
        power = power*base
    print(decimalNo)