"""
Given an unsorted array of size n. Array elements are in range from 1 to n. One number 'A' 
from set {1, 2, …n} is missing and one number 'B' occurs twice in array. Find these two numbers.
Note: If you find multiple answers then print the Smallest number found.

Input:
The first line of input contains an integer T denoting the number of test cases. 
The description of T test cases follows.
The first line of each test case contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements 
of the array.


Output:
Print B, the repeating number followed by A which is missing in a single line.

Example:
Input
2
2
2 2
3 
1 3 3
Output
2 1
3 2
"""
t = int(input())

def missingNumber(n,nums):
        return (n*(n+1))//2 - sum(nums)
        
def findDup(nums):
    dup = []
    for i in nums:
        if i in dup:
            return i
        dup.append(i)
        
while t > 0:
    n = int(input())
    nums = list(map(int,input().split()))
    nums.append(0)
    print(findDup(nums),missingNumber(n,set(nums)))
    t -= 1