"""
Problem Link: https://codezen.codingninjas.in/practice/463/347/print-the-pattern

Print the following pattern for the given number of rows.
Pattern for N = 5
 1    2   3    4   5
 11   12  13   14  15
 21   22  23   24  25
 16   17  18   19  20
 6    7    8   9   10

Input format : N (Total no. of rows)
Output format : Pattern in N lines

Sample Input :
4
Sample Output :
1  2  3  4
9 10 11 12
13 14 15 16
5  6  7  8
"""
n = int(input())
start = 1
for i in range(1,n+1):
    for no in range(start,start+n):
        print(no,end=" ")
    print()
    if i == (n+1)//2:
        start = n*(n-2)+1 if n%2 else n*(n-1)+1
    elif i < (n+1)//2:
        start += (2*n)
    else:
        start -= (2*n)