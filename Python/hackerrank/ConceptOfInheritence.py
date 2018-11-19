"""
Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person 
and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.
Complete the Student class by writing the following:
A Student class constructor, which has 4 parameters:
	1. A string, firstName.
	2. A string, lastName.
	3. An integer, id.
	4. An integer array (or vector) of test scores, scores.
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated 
average:

Input Format
The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate 
method (which takes no arguments).
You are not responsible for reading the following input from stdin:
The first line contains firstName, lastName, and id, respectively. The second line contains the number of test scores. The third line of 
space-separated integers describes scores.

Constraints
4 <= | firstName |, | lastName | <= 10
| id | = 7
0 <= score, average <= 100

Output Format
This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() 
method are properly implemented.

Sample Input
Heraldo Memelli 8135627
2
100 80

Sample Output
 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
"""
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        r = sum(self.scores)/len(self.scores)
        if r >= 90:
            return 'O'
        elif r >= 80 and r < 90:
            return 'E'
        elif r >= 70 and r < 80:
            return 'A'
        elif r >= 55 and r < 70:
            return 'P'
        elif r >= 40 and r < 55:
            return 'D'
        else:
            return 'T'

        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
