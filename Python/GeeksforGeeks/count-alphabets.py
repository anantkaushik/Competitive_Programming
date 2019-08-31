"""
Problem Link: https://practice.geeksforgeeks.org/problems/count-alphabets/0

Given a string, print the number of alphabets present in the string.

Input:
The first line of input contains an integer T denoting the number of test cases. 
The description of T test cases follows.Each test case contains a single string. 

Output:
Print the number of alphabets present in the string.

Constraints:
1<=T<=30
1<=size of string <=100

Example:
Input:
2
adjfjh23
njnfn_+-jf

Output:
6
7
"""
def count_alphabets(s):
    count = 0
    for c in s:
        if c.isalpha():
            count += 1
    return count
    
for _ in range(int(input())):
    s = input()
    print(count_alphabets(s))