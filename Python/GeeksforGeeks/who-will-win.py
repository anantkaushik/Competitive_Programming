"""
Problem Link: https://practice.geeksforgeeks.org/problems/who-will-win/0

Given a sorted array arr[] of N integers and a number K is given. The task is to check if the element K is present in the array or not.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the array 
and the number K seperated by space. Next line contains N elements.

Output:
For each testcase, if the element is present in the array print "1" (without quotes), else print "-1" (without quotes).

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= K <= 106
1 <= arr[i] <= 106

Example:
Input:
2
5 6
1 2 3 4 6
5 2
1 3 4 5 6

Output:
1
-1

Explanation:
Testcase 1: Since, 6 is present in the array at index 4 (0-based indexing), so output is 1.
Testcase 2: Since, 2 is not present in the array, so output is -1.
"""
def binarySearch(arr,target):
    start,end = 0,len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return 1
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
        
for _ in range(int(input())):
    n,target = map(int,input().split())
    arr = list(map(int,input().split()))
    print(binarySearch(arr,target))