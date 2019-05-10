"""
Given a sorted array with duplicate elements and we have to find the index of last duplicate element and print index of it and also print the duplicate element.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case, the first line contains an integer N denoting 
the size of array A followed by N-space separated integers denoting the elements of the array.

Output:
For each test case, the output is two integers denoting the last index of the duplicate element and that duplicate element respectively and 
if no duplicate element occurs print -1.

Constraints:
1<=T<=100
1<=N<=50
1<=A[i]<=50

Example:
Input:
2
6
1 5 5 6 6 7
5
1 2 3 4 5
Output
4 6
-1

Explanation:
1.  Last duplicate element is 6 having index 4.
2. As no duplicate element exist, hence -1 is printed. 
"""
def duplicateIndex(arr):
    for i in range(len(arr)-1,0,-1):
        if arr[i] == arr[i-1]:
            return [i,arr[i]]
    return [-1]
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(*duplicateIndex(arr))