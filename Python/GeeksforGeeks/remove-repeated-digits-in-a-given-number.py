"""
Problem Link: https://practice.geeksforgeeks.org/problems/remove-repeated-digits-in-a-given-number/0
       
Given an integer N, remove consecutive repeated digits from it.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
The first line of each test case contains the integer N.

Output:
Print the number after removing consecutive digits. Print the answer for each test case in a new line.

Input:
1
12224

Output:
124
"""
for _ in range(int(input())):
    n = input()
    stack = []
    stack.append(n[0])
    for i in n:
        if stack[-1] != i:
            stack.append(i)
    print("".join(stack))