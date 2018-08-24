"""
Adobe is playing an array game. He is weak in the concepts of arrays. Adobe is given two arrays a[ ] and b[ ] 
of the same size. The array a[ ] will be said to fit in array b[ ] if by arranging the elements of both array, 
there exists a solution such that i_th element of a[ ] is less than or equal to an i_th element of b[ ]. 
Help Adobe find if the given arrays are fit or not.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case, 
the next subsequent line contains the integer N i.e. size of arrays followed by array a[ ] and then array b[ ].

Output:
Print 'YES' if array a[ ] fit in array b[ ] otherwise print 'NO'.

Example:
Input
2
4
7 5 3 2 
5 4 8 7
8
7 5 3 2 5 105 45 10
2 4 0 5 6 9 75 84
Output
YES
NO
"""
def check(a,b,n):
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True
t = int(input())
while t > 0:
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr1.sort()
    arr2.sort()
    if check(arr1,arr2,n):
        print("YES")
    else:
        print("NO")
    t -= 1