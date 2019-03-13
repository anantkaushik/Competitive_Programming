"""
Problem Link: https://practice.geeksforgeeks.org/problems/add-two-fractions/1

You are given four numbers num1, den1, num2, and den2. You need to find (num1/den1)+(num2/den2) and 
output the result in the form of (numx/denx).

Input Format:
The first line of input contains an integer T denoting the number of test cases . Then T test cases follow . 
Each test case contains four integers num1, den1, num2, den2 respectively .

Output Format:
For each test case, in a new line,  output will be the fraction in the form a/b where the fraction denotes 
the sum of the two given fractions in reduced form.

Your Task:
Since this is a function problem, you don't need to worry about the testcases. Your task is to complete the 
function addFraction  which adds the two fractions and prints the resulting fraction. 
The function takes four arguments num1, den1, num2, den2 where num1, num2 denotes the numerators 
of two fractions and den1, den2 denotes their denominators.

Constraints:
1 <= T <= 100
1 <= den1,den2,num1,num2 <= 1000

Example:
Input
1
1 500 2 500
Output
3/500

Explanation:
In above test case 1/500+2/500=3/500

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be 
used by a user for Expected Output only. As it is a function problem, hence a user should not read 
any input from stdin/console. The task is to complete the function specified, and not to write the full code.
"""
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split(' ')))
        addFraction(arr[0], arr[1], arr[2], arr[3])


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#Your task is to complete this function
#Your shouldn't return any thing it should print the required output
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
    
def lcm(a,b):
    return (a*b)//gcd(a,b)
    
def addFraction(num1, den1, num2, den2):
    #Code here
    den = lcm(den1,den2)
    num = num1 * (den//den1) + num2 * (den//den2)
    gcdND = gcd(num,den)
    print(str(num//gcdND)+"/"+str(den//gcdND))