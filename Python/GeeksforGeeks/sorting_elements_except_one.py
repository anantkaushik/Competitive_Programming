"""
Given an array A of positive integers, sort the array in ascending order such that element at 
index K in unsorted array stays unmoved and all other elements are sorted.

Input:
The first line contains an integer T, number of test cases. For each test case, there is an integer 
n denoting the size of the array A. Next line contains n space separated integers denoting the 
elements of the array. Next line contains an integer k denoting the index.

Output:
For each test case, the output is the sorted array except the element at index k.

Example:
Input
2
6
10 4 11 7 6 20
2
3
30 20 10
0
Output
4 6 11 7 10 20
30 10 20
"""
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    no = int(input())
    temp = arr[no]
    del arr[no]
    arr.sort()
    arr.insert(no,temp)
    print(*arr)
    t -= 1