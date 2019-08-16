"""
Problem Link: https://practice.geeksforgeeks.org/problems/confused-pappu/0

Pappu is confused between 6 & 9 . He works in billing department of abc company and 
his work is to return the remaining amount to the customers. If actual remaining amount is 
given we need to find the maximum possible extra amount given by the pappu to the customers.
For ex:- actual remaining amount = 56
so, maximum possible extra amount =  (59 - 56 ) = 3

Input
The first line of the input contains a single integer T denoting the number of test cases.
The first line of each test case contains N (actual remaining amount).
 
Output
For each test case, output the maximum possible extra amount in newline.

Example

Input:
3
6
66
666

Output:
3
33
333
"""
def get_real_no(n):
    new_no = list(n)
    for i in range(len(new_no)):
        if new_no[i] == '6':
            new_no[i] = '9'
    return int(''.join(new_no))
    
for _ in range(int(input())):
    n = input()
    new_no = get_real_no(n)
    print(new_no-int(n))