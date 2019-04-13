"""
Problem Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/roys-life-cycle/

Roy is going through the dark times of his life. Recently his girl friend broke up with him and to overcome 
the pain of acute misery he decided to restrict himself to Eat-Sleep-Code life cycle. For N days he did nothing but eat, sleep and code.
A close friend of Roy kept an eye on him for last N days. For every single minute of the day, he kept track of Roy's actions 
and prepared a log file.
The log file contains exactly N lines, each line contains a string of length 1440 ( i.e. number of minutes in 24 hours of the day).
The string is made of characters E, S, and C only; representing Eat, Sleep and Code respectively. ith character of the string 
represents what Roy was doing during ith minute of the day.
Roy's friend is now interested in finding out the maximum of longest coding streak of the day - X.
He also wants to find the longest coding streak of N days - Y.
Coding streak means number of C's without any E or S in between.

See sample test case for clarification.

Input:
First line of each file contains N - number of days.
Following N lines contains a string of exactly 1440 length representing his activity on that day.

Output:
Print X and Y separated by a space in a single line.

Constraints:
1 ≤ N ≤ 365
String consists of characters E, S, and C only.
String length is exactly 1440.

Note: The sample test case does not follow the given constraints on string length to avoid large data. 
It is meant only for explanation. We assure you that the hidden test files strictly follow the constraints.

SAMPLE INPUT 
4
SSSSEEEECCCCEECCCC
CCCCCSSSSEEECCCCSS
SSSSSEEESSCCCCCCCS
EESSSSCCCCCCSSEEEE

SAMPLE OUTPUT 
7 9

Explanation
Longest coding streak for each day is as follows:
Day 1: 4
Day 2: 5
Day 3: 7
Day 4: 6
Maximum of these is 7, hence X is 7.

Now in order to find longest coding streak of the all days, we should also check if Roy continued his coding from previous days.
As in the sample test case, Roy was coding for 4 minutes at the end of Day 1 and he continued to code till 5 more minutes on Day 2. 
Hence the longest coding streak is 4+5 equals 9. There is no any other coding streak larger than this. So the longest coding 
streak of all days is 9.
"""
lStreak = 0
maxStreak = 0
tempLStreak = 0
for _ in range(int(input())):
    streak = 0
    for i in input():
        if i == 'C':
            streak += 1
            tempLStreak += 1
        else:
            streak = 0
            tempLStreak = 0
        if streak > maxStreak:
                maxStreak = streak
        if tempLStreak > lStreak:
            lStreak = tempLStreak
print(maxStreak,lStreak)