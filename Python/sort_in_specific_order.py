"""
Given an array of integers (both odd and even), the task is to sort them in such a way that 
the first part of the array contains odd numbers sorted in descending order, rest portion contains 
even numbers sorted in ascending order.

Examples:
Input  : A[] = {1, 2, 3, 5, 4, 7, 10}
Output : A[] = {7, 5, 3, 1, 2, 4, 10}

Input  : A[] = {0, 4, 5, 3, 7, 2, 1}
Output : A[] = {7, 5, 3, 1, 0, 2, 4} 


Input:
The first line of input contains an integer T denoting the no of test cases. 
Then T test cases follow. Each test case contains an integer N denoting the size of the array. 
The next line contains N space separated values of the array.

Output:
For each test case in a new line print the space separated values of the  new transformed array.

Example:
Input:
2
7
1 2 3 5 4 7 10
7
0 4 5 3 7 2 1
Output:
7 5 3 1 2 4 10
7 5 3 1 0 2 4
"""
t = int(input())
while t > 0:
    n = input()
    arr = list(map(int,input().split()))
    arro = []
    arre =[]
    for i in arr:
        if i%2 == 0:
            arre.append(i)
        else:
            arro.append(i)
    arro.sort()
    arre.sort()
    print(*arro[::-1],*arre)
    t -= 1