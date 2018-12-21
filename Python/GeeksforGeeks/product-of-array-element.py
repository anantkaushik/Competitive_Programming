"""
Problem Link: https://practice.geeksforgeeks.org/problems/product-of-array-element/1

This is a functional problem . Your task is to return the product of array elements under a given modulo. 
The modulo operation finds the remainder after division of one number by another. For example, K(mod(m))=K%m= r
emainder obtained when K is divided by m.

Input:
The first line of input contains T denoting the number of testcases.Then each of the T lines contains a single 
positive integer N denotes number of element in array. Next line contain 'N' integer elements of the array.

Output:
Return the product of array elements under a given modulo.
That is, return (Array[0]*Array[1]*Array[2]...*Array[n])%modulo.

Constraints:
1<=T<=200
1<=N<=10^5
1<=ar[i]<=10^5

Example:
Input:
1
4
1 2 3 4

Output:
24
"""
if __name__=="__main__":
    t=int(input())
    mod=1000000007
    for j in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        print(product(arr,n,mod))

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# arr is the array
# n is the number of element in array
# mod= modulo value
def product(arr,n,mod):
    p = 1
    for i in arr:
        p *= i
    return p % mod