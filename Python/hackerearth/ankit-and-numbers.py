"""
Problem Link: https://www.hackerearth.com/problem/algorithm/ankit-and-numbers-8/

Ankit has a set of numbers and has recently studied set theory. He has created a power set of this set and is writing a program to compute 
sum of all elements of all the subsets in power set. 
Power set of a set S is defined as set of all possible subsets of S.
Set S consist of all the number from 1 to N.
You need to calculate this sum for a given n.

Example:

Given N=3,
S={1,2,3}
P(S) = {{1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}
answer = (1)+(2)+(3)+(1+2)+(1+3)+(2+3)+(1+2+3) = 24

Input
First line has T, the total number of test cases.
The next T lines contains a number N in each line.

Output
T lines giving answer as defined in the question for each N.

Constraints
1<=T<=42
1<=N<=42

SAMPLE INPUT 
1
3
SAMPLE OUTPUT 
24
"""
for _ in range(int(input())):
    n = int(input())
    occur = 2**(n-1) # No of times each no occurs
    summN = n*(n+1)//2 # Sum of 1 to N
    print(occur*summN)