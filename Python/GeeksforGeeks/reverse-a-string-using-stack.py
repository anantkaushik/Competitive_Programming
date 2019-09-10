"""
Problem Link: https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1

An string of words is given, the task is to reverse the string using stack.

Input Format:
The first line of input will contains an integer T denoting the no of test cases. 
Then T test cases follow. Each test case contains a string s of words without spaces.

Output Format:
For each test case ,print the reverse of the string in new line. 

Your Task:
Since this is a function problem, you don't need to take any input. Just complete the provided function.

Constraints:
1 <= T <= 100
1 <= length of the string <= 100

Example:
Input:
2
GeeksQuiz
GeeksforGeeks
Output:
ziuQskeeG
skeeGrofskeeG
"""
{

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
}
''' This is a function problem.You only need to complete the function given below '''

def reverse(string):
    stack = []
    for c in string:
        stack.append(c)
    reversedString = []
    while stack:
        reversedString.append(stack.pop())
    return "".join(reversedString)
        