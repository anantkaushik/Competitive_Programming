"""
Problem Link: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/e-maze-in-1aa4e2ac/

Ankit is in maze. The command center sent him a string which decodes to come out from the maze. He is initially at (0, 0). 
String contains L, R, U, D denoting left, right, up and down. In each command he will traverse 1 unit distance in the respective direction.

For example if he is at (2, 0) and the command is L he will go to (1, 0).

Input:
Input contains a single string.

Output:
Print the final point where he came out.

Constraints:
1 ≤ |S| ≤ 200

SAMPLE INPUT 
LLRDDR

SAMPLE OUTPUT 
0 -2
"""
path = input()
start = [0,0]
for direction in path:
    if direction == "L":
        start[0] -= 1
    elif direction == "R":
        start[0] += 1
    elif direction == "U":
        start[1] += 1
    elif direction == "D":
        start[1] -= 1
print(*start)