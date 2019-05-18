"""
Problem Link: https://practice.geeksforgeeks.org/problems/binary-representation/0

Write a program to print Binary representation of a given number N.

Input:
The first line of input contains an integer T, denoting the number of test cases. Each test case contains an integer N.

Output:
For each test case, print the binary representation of the number N in 14 bits.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 5000

Example:
Input:
2
2
5

Output:
00000000000010
00000000000101
"""
def convertToBinary(n):
    b = ["0"]*14
    index = 13
    while n:
        b[index] = str(n%2)
        n //= 2
        index -= 1
    return "".join(b)
    
for _ in range(int(input())):
    print(convertToBinary(int(input())))