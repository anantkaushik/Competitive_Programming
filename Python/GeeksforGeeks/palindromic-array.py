"""
Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. Which will return 1 if all the elements of 
the Array are palindrome otherwise it will return 0.

Input:
The first line of input contains an integer denoting the no of test cases. Then T test cases follow. Each test case contains two lines. 
The first line of input contains an integer n denoting the size of the arrays. In the second line are N space separated values of the 
array A[].

Output:
For each test case in a new line print the required result.

Constraints:
1<=T<=50
1<=n<=20
1<=A[]<=10000

Example:
Input:
2
5
111 222 333 444 555
3
121 131 20

Output:
1
0
"""
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)

def PalinArray(arr ,n):
    for i in arr:
        if not(pal(i)):
            return False
    return True
    
def pal(a):
    if str(a)==str(a)[::-1]:
        return True
    return False
