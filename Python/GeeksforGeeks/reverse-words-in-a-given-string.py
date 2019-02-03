"""
Problem Link: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0

Given a String of length S, reverse the whole string without reversing the individual words in it. 
Words are separated by dots.

Input:
The first line contains T denoting the number of testcases. T testcases follow. 
Each case contains a string S containing characters.

Output:
For each test case, in a new line, output a single line containing the reversed String.

Constraints:
1 <= T <= 100
1 <= |S| <= 2000

Example:
Input:
2
i.like.this.program.very.much
pqr.mno

Output:
much.very.program.this.like.i
mno.pqr
"""
for _ in range(int(input())):
    s = input()
    temp = ""
    stack = []
    for i in s:
        if i != ".":
            temp += i
        else:
            stack.append(temp)
            temp = ""
    stack.append(temp)
    s = ""
    while stack:
        if len(stack) == 1:
            s += stack.pop()
        else:
            s += stack.pop()
            s += "."
    print(s)
    # print(".".join(input().split(".")[::-1])) # One Line Solution