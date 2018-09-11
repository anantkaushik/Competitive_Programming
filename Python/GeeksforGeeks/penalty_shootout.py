"""
Ishaan loves playing football. He is a penalty master as he practices a lot. 
Now during a match he wants to know how many goals does he score during a penalty.
Since he wants to focus on the match, he asks you to count the goals for him. 
You are given a string which consists of 3 different characters :
"0" stands for "no goal".
"1" stands for "goal".
"2" stands for a foul which gives Ishaan a penalty.
Note : You need to count only those goals which are scored on a penalty.

Input : 
First line of input contains a single integer T denoting the number of test cases.
The only line of each test case contains a string S.

Output : 
For each test case, print the required answer in a new line.

Example : 
Input : 
3
101201212110
10101
2120
Output : 
2
0
1

Explanation : 
Case 1 : 
101201212110
We consider only those goals which are after a penalty.
101201212110
There are 3 penalties, of which he scores only 2.

Case 2 : 
10101
Since there is no penalty in this match, answer is 0.

Case 3 : 
2120
We consider only those goals which are after a penalty.
2120
There are 2 penalties, of which he scores only 1.
"""
t = int(input())
while t > 0:
    s = input()
    goals = 0
    for i in range(len(s)):
        if s[i]=="2":
            goals+=int(s[i+1])
    print(goals)
    t -= 1