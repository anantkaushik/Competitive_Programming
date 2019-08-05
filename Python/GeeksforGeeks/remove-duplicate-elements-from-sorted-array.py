"""
Problem Link: https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1

Given a sorted array A of size N. The function remove_duplicate takes two arguments . The first argument is the sorted 
array A[ ] and the second argument is 'N' the size of the array and returns the size of the new converted array A[ ] 
with no duplicate element.

Input Format:
The first line of input contains T denoting the no of test cases . Then T test cases follow . The first line of each 
test case contains an Integer N and the next line contains N space separated values of the array A[ ] .

Output Format:
For each test case output will be the transformed array with no duplicates.

Your Task:
Your task to complete the function remove_duplicate which removes the duplicate  elements from the array .

Constraints:
1 <= T <= 100
1 <= N <= 104
1 <= A[ ] <= 106

Example:
Input  (To be used only for expected output) :
2
5
2 2 2 2 2 
3
1 2 2
Output
2
1 2

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for 
Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. 
The task is to complete the function specified, and not to write the full code.
"""
#Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        n = remove_duplicate(n, arr)
        for i in range(n):
            print (arr[i], end=" ")
        print()

''' This is a function problem.You only need to complete the function given below '''
#Your function should return an integer denoting the size of the new list
def remove_duplicate(n, arr):
    #Code here
    if n == 0:
        return 0
    j = 1
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j +=1
    return j    