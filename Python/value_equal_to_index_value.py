"""
Given an array, we need to find that element whose value is equal to that of its index value.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input A[].

Output:

Print the elements whose value is equal to index value. Print "Not Found" when index value 
does not match with value.
Note: There can be more than one element in the array which have same value as their index. 
You need to print every such element's index separated by a single space. Follows 1-based 
indexing of the array. 

Example:
Input
2
5
15 2 45 12 7
1
1

Output
2
1
"""
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    result = []
    for i in range(0,n):
        if arr[i] == i+1:
            result.append(i+1)
    if len(result) == 0:
        print("Not Found")
    else:
        print(*result)
    t -= 1