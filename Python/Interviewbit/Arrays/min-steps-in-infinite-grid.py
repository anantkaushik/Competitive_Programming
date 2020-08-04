"""
Problem Link: https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

Problem Description

You are in an infinite 2D grid where you can move in any of the 8 directions

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.
NOTE: This question is intentionally left slightly vague. Clarify the question by trying out 
a few cases in the “See Expected Output” section.

Input Format
Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith 
point respectively.

Output Format
Return an Integer, i.e minimum number of steps.

Example Input
Input 1:
A = [0, 1, 1]
B = [0, 1, 2]

Example Output
Output 1:
2

Example Explanation
Explanation 1:
Given three points are: (0, 0), (1, 1) and (1, 2).
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2)
"""
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        steps = 0
        for i in range(1, len(A)):
            steps += max(abs(A[i] - A[i-1]), abs(B[i] - B[i-1]))
        return steps

# Pythonic
class Solution1:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        return sum(max(abs(A[i] - A[i-1]), abs(B[i] - B[i-1])) for i in range(1, len(A)))
