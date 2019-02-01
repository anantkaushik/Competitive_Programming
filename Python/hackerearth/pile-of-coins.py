"""
Problem Link: https://www.hackerearth.com/challenge/competitive/february-easy-19/algorithm/pile-of-coins-d33de897/

Ashish and Jeel are playing a game. They are given two piles of coins with P and Q coins respectively. 
They take alterate turns. During each turn, the player can choose one pile and split it into two non-zero parts and 
discard the other pile that is not choosen. The discarded pile cannot be used further in the game. 
A player loses if he cannot make a move. Both the players play the game optimally.
You are given P and Q. Determine who wins the game if Ashish plays first.

Input format
First line: An integer T denoting the number of test cases
Next T lines: Two integers P and Q.

Output format
For each test case, print the winner of the game "Ashish" or "Jeel" (without quotes).
Answer for each test case should come in a new line.

SAMPLE INPUT 
3
1 1
1 2
2 2

SAMPLE OUTPUT 
Jeel
Ashish
Ashish

Explanation
In the first case, Ashish has no possible moves because both the piles are of size 1, hence Jeel wins.
In the other 2 cases, Ashish can take the pile of size 2 and split it into (1, 1) and discard the other pile. 
Jeel cannot make any move on (1, 1) piles, so Ashish wins.
"""
for _ in range(int(input())):
    p,q = map(int,input().split())
    if p % 2 !=0 and q % 2 != 0:
        print("Jeel")
    else:
        print("Ashish")