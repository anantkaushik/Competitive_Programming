"""
Problem Link: https://practice.geeksforgeeks.org/problems/reverse-each-word-in-a-given-string/0

Given a String of length N reverse each word in it. Words are separated by dots.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases. 
Each case contains a string containing dots and characters.
 
Output:
For each test case, output a String in single line containing the reversed words of the given String.

Constraints:
1<=T<=10
1<=Length of String<=2000

Example:
Input:
2
i.like.this.program.very.much
pqr.mno

Output:
i.ekil.siht.margorp.yrev.hcum
rqp.onm
"""
for _ in range(int(input())):
    print(".".join(i[::-1] for i in list(map(str,input().split(".")))))
    # s = input()
    # stack = []
    # temp = ""
    # for i in s[::-1]:
    #     if i == ".":
    #         stack.append(temp)
    #         temp = ""
    #     else:
    #         temp += i
    # stack.append(temp)
    # s = ""
    # while len(stack) > 1:
    #     s += stack.pop() + "."
    # s += stack.pop()
    # print(s)