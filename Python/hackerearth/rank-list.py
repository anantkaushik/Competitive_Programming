"""
Problem Link: https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/practice-problems/algorithm/rank-list/

Mid sem marks of a particular subject is announced , since you are curious in knowing your position in class so you decided to make a rank list. 
You are given the name , scholoar number and marks of every student in your class. You have to come up with accurate rank list i.e student 
having maximum marks at the top and if two students are having same marks then the student having lexicographically smaller name comes first, 
if both name and marks of the student collide then student having smaller scholar number comes first.

Input: 
First line of input contains N - Total number of students in class 
Next N line contains name of student , scholar number and marks scored in exam .

Output:
Print the ranklist of students as explained above. 

Constraints
1 <= N <= 1000 
1 <= length of name <= 10 
1 <= scholar number <= 1000 
0 <= marks <= 30 
Problem Setter : Satyam Swarnkar

SAMPLE INPUT 
5
arun 8 28
harshit 10 30
surya 7 26
satyam 27 6
arun 1 28

SAMPLE OUTPUT 
harshit 10 30
arun 1 28
arun 8 28
surya 7 26
satyam 27 6
"""
students = []
for _ in range(int(input())):
    temp = list(map(str,input().split()))
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    students.append(temp)

students.sort(key = lambda x:(-x[2], x[0], x[1]))
for i in range(len(students)):
    print(students[i][0],students[i][1],students[i][2])
