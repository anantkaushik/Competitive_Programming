"""
Given a stream of characters consisting only '0' and '1',  print the last index of the '1' 
present in it. Input stream may either be sorted in decreasing order or increasing order. 
If not present than print "-1".

Input:
First line of the input contains the number of test cases (T) ,
T lines follow each containing a stream of characters.

Output: 
Corresponding to every test case , output the last index of 1 present.

Example:
Input:
2
00001
1
Output:
4
0
"""
t = int(input())
while t > 0:
    s = input()
    print(s.rfind('1'))
    t -= 1