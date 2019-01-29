"""
Given a number your task is to complete the function convertFive which replace all zeros in the number with 5 and returns the number.

Input:
The first line of input contains an integer T denoting the number of test cases . Then T test cases follow . Each test case contains a 
single integer N denoting the number.

Output:
The output of the function will be an integer where all zero's are converted to 5 .

Constraints:
1<=T<100
1<=N<=10000

Example:
Input
2
1004
121

Ouput
1554
121
"""
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        print(convertFive(n))

def convertFive(n):
    # Code here
    res = 0
    count = 1
    while n:
        rem = n % 10
        res += count*(5 if rem == 0 else rem)
        count *= 10
        n //= 10
    return res
# def convertFive(n):
#     return str(n).replace("0","5")