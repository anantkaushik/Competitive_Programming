"""
Pitsy needs help in the given task by her teacher. The task is to divide a array into two 
sub array (left and right) containing n/2 elements each and do the sum of the subarrays and 
then multiply both the subarrays.

Input:
First line consists of T test cases. Only line of every test case consists of an integer N.​

Output:
Print the answer by dividing array into left and right array and add their elements individually 
and then multiply both the array

Example:
Input:
2
4
1 2 3 4
3
4 5 6
Output:
21
44
"""
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    sum1 = 0
    sum2 = 0
    for i in range(0,n//2):
        sum1+=arr[i]
    for i in range(n//2,n):
        sum2+=arr[i]
    print(sum1*sum2)
    t -= 1