"""
Problem Link: https://practice.geeksforgeeks.org/problems/key-pair/0

Given an array A of N positive integers and another number X. Determine whether or not there exist two 
elements in A whose sum is exactly X.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each 
test case is N and X, N is the size of array. The second line of each test case contains N integers 
representing array elements C[i].

Output:
Print "Yes" if there exist two elements in A whose sum is exactly X, else "No" (without quotes).

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 200
1 ≤ C[i] ≤ 1000

Example:

Input:
2
6 16
1 4 45 6 10 8
5 10
1 2 4 3 6

Output:
Yes
Yes

Explanation:
Testcases 1: 10 and 6 are numbers making a pair whose sum is equal to 16.
"""
def twoSum(arr,target):
    n = set()
    for i in arr:
        temp = target - i
        if temp in n:
            return "Yes"
        n.add(i)
    return "No"
    
for _ in range(int(input())):
    n,target = map(int,input().split())
    arr = list(map(int,input().split()))
    print(twoSum(arr,target))