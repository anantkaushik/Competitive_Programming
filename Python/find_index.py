"""Given an unsorted array Arr[] of N integers and a Key which is present in this array. You need to write a program to find the start index
( index where the element is first found from left in the array ) and end index( index where the element is first found from right in the array ).

Input:
Fisrt line of input contains an integer T which denotes the number of test cases. First line of each test case contains a single integer N which denotes 
the number of elements in the array. Second line of each test case contains N space separated integers. Third line of each test case contains the key to 
be searched.

Output:
For each test case print two space separated integeres, first is the start index and second is the end index. If the key doesnot exist in the array then 
print -1 in this case.

Sample Input:
2
6
1 2 3 4 5 5
5
6
6 5 4 3 1 2
4
Sample Output:
4 5
2 2
"""
count = int(input())
while count>0:
    n,a,k = int(input()),list(map(int,input().split())),int(input())
    print(a.index(k),(n - a[::-1].index(k) - 1))
    count-=1