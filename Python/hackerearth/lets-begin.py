"""
February Easy Challenge 2015 is underway. Hackerearth welcomes you all and hope that all you awesome coders have a great time. 
So without wasting much of the time let's begin the contest.

Prime Numbers have always been one of the favourite topics for problem setters. For more information on them you can use see this link 
http://en.wikipedia.org/wiki/Prime_number .

Aishwarya is a mathematics student at the Department of Mathematics and Computing, California. Her teacher recently gave her an intriguing assignment 
with only a single question. The question was to find out the minimum number of single digit prime numbers which when summed equals a given number X.

Input:
The first line contains T denoting the number of test cases. Each of the next T lines contains a single integer X.

Output:
Print the minimum number required. If it is not possible to obtain X using single digit prime numbers, output -1.

Constraints:
1<=T<=100
1<=X<=10^6

SAMPLE INPUT 
4
7
10
14
11
SAMPLE OUTPUT 
1
2
2
3
Explanation
10 can be represented as 7 + 3.
14 can be represented as 7+7
11 can be represented as 5+3+3.
"""
def check(n,prime):
    if n - prime < 0:
        return False
    return True
    
for i in range(int(input())):
    n = int(input())
    if n > 7:
        dp = [float('inf')]*(n+1) 
    else:
        dp = [float('inf')]*(8) 
    dp[2] = dp[3] = dp[5] = dp[7] = 1
    for i in range(1,n+1):
        if check(i,2):
            dp[i] = min(dp[i],1+dp[i-2])
        if check(i,3):
            dp[i] = min(dp[i],1+dp[i-3])
        if check(i,5):
            dp[i] = min(dp[i],1+dp[i-5])
        if check(i,7):
            dp[i] = min(dp[i],1+dp[i-7])
    
    print(-1 if dp[n] == float('inf') else dp[n])