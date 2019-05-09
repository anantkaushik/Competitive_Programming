"""
Problem Link: https://practice.geeksforgeeks.org/problems/subarray-range-with-given-sum/0

Given an unsorted array arr[] of N integers and a sum. The task is to count the number of subarray which adds to a given number.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case contains an integer N denoting the size of the array. The next line contains N space separated integers forming the array. 
The last line contains an integer denoting the value of the sum.

Output:
Print the count of the subarray which adds to the given sum.

Constraints:
1 <= T <= 200
1 <= N <= 105
-105 <= arr[i] <= 105
-105 <= sum <= 105

Example:
Input:
2
5
10 2 -2 -20 10
-10
6
1 4 20 3 10 5
33

Output:
3
1

Explanation:
Testcase 1: Subarrays with sum -10 are: [10, 2, -2, -20], [2, -2, -20, 10] and [-20, 10].
"""
def countSubSum(arr,target):
    count,summ,d = 0,0,{0:1}
    for i in arr:
        summ += i
        if summ - target in d:
            count += d[summ-target]
        d[summ] = d.get(summ,0) + 1
    return count
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    target = int(input())
    print(countSubSum(arr,target))