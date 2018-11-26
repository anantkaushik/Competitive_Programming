"""
Problem Link: https://practice.geeksforgeeks.org/problems/square-root/1/?ref=self

Given an integer x , Your task is to find the  square root of it. If x is not a perfect square, then return floor(√x)

Input:
You have to complete the method which takes 1 argument: the integer N. You should not read any input from stdin/console. 
There are multiple test cases. For each test cases, this method will be called individually.

Output:
Your function should return square root of given integer.

Constraints:

1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000

Example:
Input
2
5
4

Output
2
2
"""
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(floorsqrt(n))

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

def floorsqrt(n):
    # Code Goes Here
    low = 1
    high = n
    while low <= high:
        mid = (low+high)//2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            high = mid - 1
        else:
            low = mid + 1
    return high