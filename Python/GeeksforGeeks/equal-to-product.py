"""
Problem Link: https://practice.geeksforgeeks.org/problems/equal-to-product/0

Given an array of positive integers. Check whether there are two numbers present with given product.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N and a product P.
The second line of each test case contain elements of array.

Output:
Print "Yes" (Without quotes) if two numbers product is equal to P else "No" (without quotes).

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
0 ≤ Ai ≤ 263 - 1
0 <= P <= 264 - 1

Example:
Input:
2
5 25
1 2 3 4 5
8 63
5 7 9 22 15 344 92 8

Output:
No
Yes
"""
for _ in range(int(input())):
    l1 = list(map(int,input().split()))
    if len(l1) == 2:
        prod = l1[1]
    else:
        prod = int(input())
    arr = list(map(int,input().split()))
    temp = set()
    flag = 0
    for i in arr:
        if i:
            target = prod/i
            if target in temp:
                print("Yes")
                flag = 1
                break
            temp.add(i)
    if flag == 0:
        print("No")