"""
Provided a String of length N, your task is to find out whether or not the given string is a prime string. 
A prime string is a string in which the sum of the ASCII value of all the characters is prime.

Input:
The first line of the input contains an integer T, denoting the number of test cases. Then T test case follows. 
The first line of each test case contains an integer N denoting the length of the string, next line contains the input string str of length N.

Output:
For each test case print 'YES' if the string is prime string else print 'NO', on a new line.

Example:
Input
3
13
geeksforgeeks
4
JiiT
5
India

Output
YES
NO
NO
"""
t = int(input())
def prime(no):
    for i in range(2,no//2):
        if no % i == 0:
            return False
    return True
    
while t > 0:
    n = int(input())
    s = input()
    sum = 0
    for i in s:
        sum += ord(i)
    if prime(sum):
        print("YES")
    else:
        print("NO")
    t -= 1