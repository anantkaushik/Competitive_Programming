"""
Problem Link: https://practice.geeksforgeeks.org/problems/run-length-encoding/1

Given a string, Your task is to  complete the function encode that returns the run length encoded string for the 
given string.
eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.
You are required to complete the function encode that takes only one argument the string which is to be encoded and 
returns the encoded string.

Input:
The first line contains T denoting no of test cases . Then T test cases follow . Each test case contains a string str 
which is to be encoded .

Output:
For each test case output in a single line the so encoded string .

Constraints:
1<=T<=100
1<=length of str<=100

Example:
Input
2
aaaabbbccc
abbbcdddd

Output
a4b3c3
a1b3c1d4
"""
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#Your task is to complete this function
#Function should return complete string
def encode(arr):
    # Code here
    newArr = []
    countConsecutive = 0
    for i in range(len(arr)):
        countConsecutive += 1
        if i+1 >= len(arr) or arr[i] != arr[i+1]:
            newArr.append(arr[i])
            newArr.append(str(countConsecutive))
            countConsecutive = 0
    return "".join(newArr)