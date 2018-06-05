"""
Ishaan is getting really fat. He wants to lose his weight but can't get the motivation to workout. 
Seeing this, his friend Charul offers him a deal. For every K pushups Ishaan does, 
Charul will give him money equal to the number of pushups Ishaan has done till then 
(Refer Example for Explanation).Find out the amount of money he made if he does N pushups.

Input : 
The first line of input contains a single integer T denoting the number of test cases.
The only line of each test case contains 2 space-separated integers N and K.

Output : 
For each test case, print the required answer in a new line.

Example : 
Input : 
3
5 2
5 3
5 6
Output : 
6
3
0

Explanation : 
Case 1 : 
Pushup 1: No Money
Pushup 2: +2
Pushup 3: No Money
Pushup 4: +4
Pushup 5: No Money
Case 2 : 
Pushup 1: No Money
Pushup 2: No Money
Pushup 3: +3
Pushup 4: No Money
Pushup 5: No Money
Case 3 : 
Pushup 1: No Money
Pushup 2: No Money
Pushup 3: No Money
Pushup 4: No Money
Pushup 5: No Money
"""
t = int(input())
while t > 0:
    n,k = map(int,input().split())
    sum = 0
    for i in range(k,n+1,k):
        sum += i
    print(sum)
    t -= 1