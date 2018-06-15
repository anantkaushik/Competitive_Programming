"""
Given a string s check if it is palindrome or not.

Input:
The first line contains 'T' denoting the number of test cases. Then follows description of test cases.
Each case begins with a single integer N denoting the length of string. The next line contains the string s.


Output:
Print "Yes" if it is a palindrome else "No". (Without the double quotes)

Example:
Input:
1
4
abba

Output:
Yes
"""
t = int(input())
while t > 0:
    l = input()
    str = input()
    if str == str[::-1]:
        print("Yes")
    else:
        print("No")
    t -= 1