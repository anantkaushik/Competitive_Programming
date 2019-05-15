"""
You are given a number N. Determine the number of positive even integers that are smaller than or equal to it and are not a multiple of 4.

Input Format
The first line contains a single integer T, denoting the number of test cases.
Each of the next T lines contains a single integer, denoting the value of N.

Output Format
Print T lines, where the i-th line contains the answer to the i-th test case.

SAMPLE INPUT 
4
3
7
8
11
SAMPLE OUTPUT 
1
2
2
3

Explanation
For N=3, only 2 follows the given conditions, so answer is 1.
For N=11, numbers 2, 6 and 10 follows the given conditions, so answer is 3.
"""
for _ in range(int(input())):
    n = int(input())
    print((n//2)-(n//4))