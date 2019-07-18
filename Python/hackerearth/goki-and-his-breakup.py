"""
Problem Link: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/tds-and-his-breakup/

Goki recently had a breakup, so he wants to have some more friends in his life. Goki has N people who he can be friends with, 
so he decides to choose among them according to their skills set Yi(1<=i<=n). He wants atleast X skills in his friends.
Help Goki find his friends.

INPUT
First line of the input contains an integer N denoting the number of people.
Next line contains a single integer X - denoting the minimum skill required to be Goki's friend. 
Next n lines contain one integer Y - denoting the skill of ith person.

OUTPUT
For each person print if he can be friend with Goki. 'YES' (without quotes) if he can be friends with Goki else 'NO' (without quotes).

CONSTRAINTS
1<=N<=1000000
1<=X,Y<=1000000

SAMPLE INPUT 
5
100
110
130
90
100
45

SAMPLE OUTPUT 
YES
YES
NO
YES
NO

Explanation
X is 100, so the first query is 110, so as 110 is greater than 100 answer is YES.
"""
n = int(input())
minSkills = int(input())
for _ in range(n):
    print("YES" if int(input()) >= minSkills else "NO")