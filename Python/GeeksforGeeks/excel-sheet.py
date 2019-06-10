"""
Problem Link: https://practice.geeksforgeeks.org/problems/excel-sheet/0

Given a positive integer N, print its corresponding column title as it would appear in an Excel sheet.
For N =1 we have column A, for 27 we have AA and so on.
Note: The alphabets are all in uppercase.

Input:
The first line contains an integer T, depicting total number of test cases. Then following T lines contains an integer N.

Output:
For each testcase, in a new line, print the string corrosponding to the column number.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107

Example:
Input:
1
51
Output:
AY
"""
for _ in range(int(input())):
    col = int(input())
    res = []
    while col:
        col = col-1
        res.append(chr((col%26)+65))
        col = col//26
    print("".join(res[::-1]))