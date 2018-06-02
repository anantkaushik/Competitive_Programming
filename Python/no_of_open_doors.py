"""
Consider a long alley with a N number of doors on one side. All the doors are closed initially. 
You move to and fro in the alley changing the states of the doors as follows: you open a door that is 
already closed and you close a door that is already opened. You start at one end go on altering the 
state of the doors till you reach the other end and then you come back and start altering the states of 
the doors again.
In the first go, you alter the states of doors numbered 1, 2, 3, … , n.
In the second go, you alter the states of doors numbered 2, 4, 6 …
In the third go, you alter the states of doors numbered 3, 6, 9 …
You continue this till the Nth go in which you alter the state of the door numbered N.
You have to find the number of open doors at the end of the procedure.

Input:
The first line of input contains a single integer T denoting the number of test cases. 
Then T test cases follow. Each test case consists of one line. The line consists of a positive integer N.

Output:
Corresponding to each test case, in a new line, print the number of doors that will be open at the end 
of the procedure mentioned above.

Example:
Input
5
372
2
100
825625
63542

Output
19
1
10
908
252
"""
import math
t = int(input())
while t > 0:
    n = int(input())
    print(int(math.sqrt(n)))
    t -= 1