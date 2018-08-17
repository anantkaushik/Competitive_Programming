"""
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ). 
The digits are stored such that the most significant digit is at the head of the list.

Example:
If the array has [4, 5, 6] the resultant array should be [4, 5, 7] as 456 + 1 = 457.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the space separated resultant array in a separate line for each case.

Input:
2
4
5 6 7 8
3
9 9 9
Output:
5 6 7 9
1 0 0 0 
"""
t = int(input())
while t > 0:
    input()
    arr = input().split()
    result = list(str(int("".join(arr))+1))
    while len(arr) > len(result):
        result.insert(0,'0')
    print(*result)
    t -= 1