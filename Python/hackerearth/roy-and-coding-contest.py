"""
Problem Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/roy-and-coding-contest/

Roy is going to organize Finals of Coding Contest in his college's computer labs. According to the rules of contest, 
problem statements will be available on each computer as pdf file.
Now there are N number of computers and only one of them has the pdf file. Roy has collected M number of pendrives from his friends. 
Copying pdf from computer to pendrive or from pendrive to computer takes exactly 1 minute. 
Roy has to copy pdf to all N computers in minimum (optimal) time possible. You are to find this minimum time. 

Input:
First line will contain integer T - number of test cases.
Next T lines each will contain two space separated integers, N - number of computers, M - number of pendrives.

Output:
Print the minimum time (in minutes) for each test case in a new line.

SAMPLE INPUT 
1
10 3
SAMPLE OUTPUT 
5
"""
for _ in range(int(input())):
    n,m = map(int,input().split())
    if n <= 1:
        print(0)
    else:
        count = time = 1
        while count < m and count < n:
            count *= 2
            time += 1
        if count > n:
            count //= 2
            time -= 1
        rem = n - count
        time += rem//m
        if rem % m != 0:
            time += 1
        print(time)