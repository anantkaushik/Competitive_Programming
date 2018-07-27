"""
Given a string S as input. You have to reverse the given string.

Input: First line of input contains a single integer T which denotes the number of test cases. 
T test cases follows, first line of each test case contains a string S.

Output: Corresponding to each test case, print the string S in reverse order.

Sample Input:
3
Geeks
GeeksforGeeks
GeeksQuiz

Sample Output:
skeeG
skeeGrofskeeG
ziuQskeeG
"""
t = int(input())
while t > 0:
    print(input()[::-1])
    t -= 1