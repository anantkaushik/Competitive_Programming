"""
Problem Link: https://www.hackerearth.com/problem/algorithm/project-team/description/

A Professor of Physics gave projects to the students of his class. The students have to form a team of two for doing the project. 
The professor left the students to decide the teams. The number of students in a class will be even.
Each student has a knowledge level. It tells how much knowledge each student has. The knowledge level of a team is the sum of the knowledge 
levels of both the students.
The students decide to form groups such that the difference between the team with highest knowledge and the one with lowest knowledge is minimum.

Input
First line of the input will contain number of test cases t; In the next t lines the first number is n the number of students in the class 
followed by n integers denoting the knowledge levels of the n students

Output
Your output should be a single line containing the lowest possible difference between the team with highest knowledge and the one with lowest knowledge.

SAMPLE INPUT 
2
4 2 6 4 3
6 1 1 1 1 1 1

SAMPLE OUTPUT 
1
0

Explanation
Input Constraints are
1 <= t <= 100 1 <= n <= 100 1 <= knowledge level <= 10000
"""
for _ in range(int(input())):
    arr = list(map(int,input().split()))
    arr = arr[1:]
    arr.sort()
    l, h = 0, len(arr)-1
    minn,maxx = float('inf'), float('-inf')
    while l < h:
        s = arr[l] + arr[h]
        if s < minn:
            minn = s
        if s > maxx:
            maxx = s
        l += 1
        h -= 1
    print(maxx-minn)