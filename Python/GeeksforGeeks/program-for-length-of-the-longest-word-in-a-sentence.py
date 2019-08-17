"""
Problem Link: https://practice.geeksforgeeks.org/problems/program-for-length-of-the-longest-word-in-a-sentence/0/

Given a string, we have to find the longest word in the input string and then calculate 
the number of characters in this word.

Input:
The first line of input contains an integer T,  number of test cases. For each test case, 
there is a string s. 

Output:
For each test case, the output is an integer denoting the length of the longest word in the sentence.

Constraints:
1<=T<=100

Example:
Input:
2
A computer science portal for geeks
I am an intern at geeksforgeeks

Output
8
13
"""
for _ in range(int(input())):
    sentence = list(map(str,input().split()))
    length_longest_word = 0
    for word in sentence:
        if len(word) > length_longest_word:
            length_longest_word = len(word)
    print(length_longest_word)