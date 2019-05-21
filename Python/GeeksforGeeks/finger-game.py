"""
Problem Link: https://practice.geeksforgeeks.org/problems/finger-game/0

Count the given numbers on your fingers and find the correct finger on which the number ends.

The first number starts from the thumb, second on the index finger, third on the middle finger, fourth on the ring finger and 
fifth on the little finger.
Again six comes on the ring finger and so on.

Input:
First line consists of T test cases. Only line input, one integer N.

Output:
Single line output, print the number of finger.

Constraints:
1<=T<=5000
1<=N<=5000

Example:
Input:
2
1
2
Output:
1
2
"""
for _ in range(int(input())):
    n = int(input())
    f = (n-1) % 8
    print(f+1 if f < 5 else 10-f-1)