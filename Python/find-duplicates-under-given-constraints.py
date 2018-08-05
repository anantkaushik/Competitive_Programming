"""
Given a sorted array having 10 elements which contains 6 different numbers in which only 1 number is repeated five times. Your task 
is to find the duplicate number using two comparisons only.

Examples:
Input: A[] = {1, 1, 1, 1, 1, 5, 7, 10, 20, 30}
Output: 1

Input: A[] = {1, 2, 3, 3, 3, 3, 3, 5, 9, 10}
Output: 3

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow . 
Each test case contains 10 space separated values of the array A[].

Output:
For each test case in a new line print the required duplicate element.

Sample Input:
2
1 2 4 5 6 9 9 9 9 9
1 2 3 3 3 3 3 5 9 10

Sample Output:
9
3
"""
t = int(input())
while t > 0:
    n = list(map(int,input().split()))
    c,ans = 0,0
    for i in range(0,7):
        if c == 0:
            ans = n[i]
            c += 1
        elif ans == n[i]:
            c += 1
        else:
            c -= 1
    print(ans)
    t -= 1