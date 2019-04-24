"""
There are times when all the inputs are provided in a single line and are separated by spaces. In such cases, the input() function takes the whole line as 
input and treats the line as a single input. We can use input().split() functionality to split the string into multiple words.

In this question, you will take input a single line string comprised of string, int, and float. You'll split the string and assign string to s, int to i, 
and float to f. Print a final string comprised of s and (i+f)

Input Format:
The first line of testcase contains T denoting the number of testcases. T testcases follow. Each testcase contains 1 lines of input.

Output Format:
For each testcase, in a new line, Output the answer.

Your Task:
Your task is to complete the function inPutS().

Constraints:
1 <= T <= 100

Example:
Input:
1
Geeks 2 2.3445
Output:
Geeks 4.3445
"""
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        inPutS() #the function that gets things done
        testcases-=1
        
if __name__=='__main__':
    main()


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def inPutS():
    a=input() ## input in a single line()
    s,i,f = a.split(" ")## split the a into three parts: string, integer, and f. 
    print(s+" "+str(int(i)+float(f))) ##type cast i to int, f to float. Add i with f. Typecast the result to string