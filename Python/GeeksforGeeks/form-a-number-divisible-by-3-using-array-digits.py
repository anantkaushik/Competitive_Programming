"""
Problem Link: https://practice.geeksforgeeks.org/problems/form-a-number-divisible-by-3-using-array-digits/0

Given an array of integers, the task is to find whether it’s possible to construct an integer using all the digits of these numbers 
such that it would be divisible by 3. If it is possible then print “1” and if not print “0”.

INPUT: The first line consists of an integer T i.e. the number of test cases. First line of each test case consists of an integer n. 
Next line consists of n spaced integers.

OUTPUT: Print '1' if it is possible to form a number divisible by 3 using the array elements otherwise print '0'.

CONSTRAINTS:

1<=T<=100
1<=n,a[i]<=105

EXAMPLES:
INPUT :
2
3
40 50 90
2
1 4

OUTPUT : 
1
0

EXPLANATION :
Input : arr[] = {40, 50, 90}
Output : Yes
We can construct a number which is
divisible by 3, for example 945000. 
So the answer is Yes. 

Input : arr[] = {1, 4}
Output : No
The only possible numbers are 14 and 41,
but both of them are not divisible by 3, 
so the answer is No.
"""
def isDivisibleByThree(arr):
    summ = 0
    for n in arr:
        summ += n
    return 1 if summ%3 == 0 else 0
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(isDivisibleByThree(arr))