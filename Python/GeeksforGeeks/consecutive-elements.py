"""
Problem Link: https://practice.geeksforgeeks.org/problems/consecutive-elements/0

For a given string delete the elements which are appearing more than once consecutively. All letters are of lowercase.

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases,  a string will be inserted.

Output:
In each seperate line the modified string should be output.

Constraints:
1<=T<=31
1<=length(string)<=100

Example:
Input:
1
aababbccd

Output:
ababcd
"""
for _ in range(int(input())):
    s = list(input())
    index = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            s[index] = s[i]
            index += 1
    s[index] = s[-1]
    print("".join(s[:index+1]))