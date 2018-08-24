"""
Given a list of characters, merge all of them into a string.
Input:
First line of the input contains an integer T, denoting the number of testcases. 
Then T test case follows. Each testcase contains two lines:-
The number of characters in the array N.
The array of characters separated by space
Output:
For each testcase, print the character array converted into a string.

Sample Input:
2
13
g e e k s f o r g e e k s
11
p r o g r a m m i n g

Sample Output:
geeksforgeeks
programming
"""
t = int(input())
while t>0:
    n = int(input())
    arr = list(input().split())
    for i in arr:
        print(i,end='')
    print()
    t-= 1