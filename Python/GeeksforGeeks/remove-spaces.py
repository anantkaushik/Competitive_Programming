"""
Problem Link: https://practice.geeksforgeeks.org/problems/remove-spaces/0

Given a string, remove spaces from it

Input: First line of the input is the number of test cases T. And first line of test case contains a string whose spaces are to be removed.
Output:  Modified string without any space
Constraints:  Input String Length <= 1000

Example:
Input:
2
geeks  for geeks
    g f g

Output:
geeksforgeeks
gfg
"""
print(*["".join(input().split()) for _ in range(int(input()))],sep='\n')