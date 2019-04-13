"""
Problem Link: https://practice.geeksforgeeks.org/problems/taking-input-and-typecasting-python/1/

You have learned to take string input in python. Now, you'll learn how to take input of int, float, and bool.

In Python, we use the input() function and put this function in either int(), float(), or bool() to typecast the input into 
required data type. Also, integers, floating-points and boolean variables don't have any range in Python. 
As long as you have enough memory, you can work with them.

In this question, you will take input of 4 variables that are in separate lines. The first variable is an integer, 
the second is a string(single/multiple words possible), the third is a floating number, the fourth is a boolean value.
You need to take the inputs and print the outputs.

Input Format:
The first line of testcase contains T denoting the number of testcases. T testcases follow. Each testcase contains 4 lines of input.

Output Format:
For each testcase, in a new line, print the inputs and the class of the input.

Your Task:
Your task is to complete the function inPut().

Constraints:
1 <= T <= 100

Example:
Input:
1
56
fdg fgdf
3.43534
True

Output:
56
fdg fgdf
3.43534
True
"""
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        inPut() #the function that gets things done
        testcases-=1
        
if __name__=='__main__':
    main()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def inPut():
    #Take input and assign the input to a,b,c,d. Please also typecast as type() will produce wrong answer without it
    a= int(input()) ## a is integer
    b= input() ## b is string
    c= float(input()) ## c is float
    d= bool(input()) ## d is a boolean
    
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))