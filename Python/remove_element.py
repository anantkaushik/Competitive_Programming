"""
Given a string consisting of alphabets and others characters, 
the task is to remove all the characters other than alphabets and print the string so formed.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case contains a string S.

Output:
For each test case, print the remaining string in new line, 
If no character remains in the string print "-1".

Sample Input:
2
$Gee*k;s..fo, r'Ge^eks?
P&ra+$BHa;;t*ku, ma$r@@s#in}gh

Sample Output:
GeeksforGeeks
PraBHatkumarsingh
"""
t=int(input())
while t>0:
    a = input()
    flag = 0
    for i in range(0,len(a)):
        if a[i] >='a' and a[i] <='z':
            print(a[i],end='')
            flag = 1
        elif a[i] >='A' and a[i] <='Z': 
            print(a[i],end='')
            flag = 1
    if flag == 1:
        print()
    else:
        print(-1)
    t-=1