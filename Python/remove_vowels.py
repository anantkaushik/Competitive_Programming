"""
Given a string, remove the vowels from the string and print the string without vowels.

Input:
The first line consists of an integer T i.e number of test cases. The first and only line 
of each test case consists of a string s. 

Output:
Print the required output.

Example:
Input:
2
welcome to geeksforgeeks
what is your name ?

Output:
wlcm t gksfrgks
wht s yr nm ?
"""
t = int(input())
while t > 0:
    s = input()
    a = "aeiou"
    ns = ""
    for i in s:
        if i not in a:
            ns+=i
    print(ns)
    t -= 1