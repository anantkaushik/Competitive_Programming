"""
Problem Link: https://practice.geeksforgeeks.org/problems/perfect-number/0

Check if  a given number is perfect or not. A number is perfect if sum of factorial of its digit is equal to the given number. 
For example 145 is a Perfect Number because 1! + 4! + 5! = 145

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case there will be single 
line which contains an integer N.

Output:
Corresponding to each test case, in a new line, print "Perfect " if it follow above condition else print "Not Perfect"  without quotes.

Constraints:
1 <= T <=  50
1 <= N <= 104
Example:
Input:
2
23
145

Output:
Not Perfect
Perfect
"""
def fact(no,factArr):
    if no < len(factArr):
        return factArr[no]
    for n in range(len(factArr),no+1):
        factArr.append(factArr[n-1]*n)
    return factArr[no]
    
def isPerfect(n):
    factArr = [1]
    summ = 0
    temp = n
    while temp:
        no = temp%10
        summ += fact(no,factArr)
        temp //=10
    return summ == n
        

for _ in range(int(input())):
    n = int(input())
    print("Perfect" if isPerfect(n) else "Not Perfect")