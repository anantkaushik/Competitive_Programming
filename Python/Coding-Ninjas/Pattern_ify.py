"""
Print the following pattern for the given number of rows.

Pattern for N = 4
****
***
**
*

Input format : N (Total no. of rows)
Output format : Pattern in N lines

Sample Input :
5
Sample Output :
* * * * *
* * * *  
* * *
* *
*
"""
## Read input as specified in the question.
## Print output as specified in the question.
for i in range(int(input()),0,-1):
  print("*"*i)