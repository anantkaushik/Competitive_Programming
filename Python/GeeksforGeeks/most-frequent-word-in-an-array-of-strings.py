"""
Problem Link: https://practice.geeksforgeeks.org/problems/most-frequent-word-in-an-array-of-strings/0

Given an array containing N words consisting of lowercase characters. Your task is to find the most frequent word 
in the array. If multiple words have same frequency, then print the word that comes first in lexicographical order.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. 
Each test case contains 2 lines, the size of array N and N words separated by spaces.

Output:
For each testcase, output the most frequent word.

Constraints:
1 <= T <= 100
1 <= N <= 1000

Example:
Input:
3
3
geeks for geeks
2
hello world
3
world wide fund

Output:
geeks
hello
fund

Explanation:
Testcase 1: "geeks" comes 2 times.
Testcase 2: "hello" and "world" both have 1 frequency. We print hello as it comes first in lexicographical order.
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(str,input().split()))
    d = {}
    maxx = 0
    for i in arr:
        d[i] = d.get(i,0) + 1
        if d[i] > maxx:
            maxx = d[i]
    for k in sorted(d.keys()):
        if d[k] == maxx:
            print(k)
            break