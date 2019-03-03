"""
This is one of the most easiest problem you will ever code.

Mr. Bournville loves programming and he likes to face new programming challenges. After completing many challenges 
he has now given you one challenge which is one of his favourites. He has given you a list of N random integers 
and he wants you to find the integer which has the maximum frequency in the given list.

Mr. Bournville already has a solution for this but he is not satisfied with his solution. 
He wants you to write a shortest possible code for this task. In case Frequency of two numbers is same print 
the smaller one

Input:
First line of input contains N, number of integers.
Second line will contains N spaces separated integers.

Output:
Print the most frequent integer.

SAMPLE INPUT 
5
1 1 1 2 2

SAMPLE OUTPUT 
1
Explanation
Clearly, count of 1 more than count of 2.
"""
n = int(input())
arr = list(map(int,input().split()))
d = {}
maxx, maxItem = 0, None
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
    if d[i] >= maxx:
        if d[i] != maxx or i < maxItem:
            maxx = d[i]
            maxItem = i
print(maxItem)