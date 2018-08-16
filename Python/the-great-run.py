"""
Vishal loves running. He often visits his favourite Nehru Park and runs for very long distances. On one such visit he found that 
the number of girls in the park was unusually high. Now he wants to use this as an opportunity to impress a large number of girls 
with his awesome speed.
The track on which he runs is an N kilometres long straight path. There are ai girls standing within the ith kilometre of this path. 
A girl will be impressed only if Vishal is running at his maximum speed when he passes by her. But he can run at his best speed only 
for a single continuous stretch of K kilometres. Now Vishal wants to know what is the maximum number of girls that he can impress.

Input

First line of the input contains the number of testcases T.
For each test case,
First line contains two space-separated integers N and K, the length of the track and the maximum distance he can run at his best speed.
Second line contains N space-separated integers, the number of girls within each kilometre of the track.

Output
For each test case print one line containing an integer, denoting the maximum number of girls Vishal can impress.

Sample Input
1
7 2
2 4 8 1 2 1 8

Sample Output
12

Explanation
He can impress 4+8=12 girls if he runs at his best speed between the 2nd and the 3rd kilometre, inclusive.
"""
for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    maxx = 0
    for i in range(n-k+1):
        if maxx < sum(arr[i:k+i]):
            maxx = sum(arr[i:k+i])
    print(maxx) 