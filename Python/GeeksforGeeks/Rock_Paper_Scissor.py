"""
The RPS world championship is here. Here two players A and B play the game. You need to determine who wins.
Both players can choose moves from the set {R,P,S}.
The game is a draw if both players choose the same item. 
The winning rules of RPS are given below:

Rock crushes scissor
Scissor cuts paper
Paper envelops rock
Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains single line of input that contains two characters sidebyside. These characters denote the moves of players A and B respectively.

Output:
For each testcase, in a newline, print the winner. If match is draw, print 'DRAW'.

Constraints:
1<= T <= 50

Example:
Input:
7
RR
RS
SR
SP
PP
PS
RP

Output:
DRAW
A
B
A
DRAW
B
B
"""

t = int(input())

while(t>0):
    game = input()
    if game[0] == game[1]:
        print("DRAW")
    elif ((game[0]=='R' and game[1]=='S') or (game[0]=='S' and game[1]=='P') or (game[0]=='P' and game[1]=='R')):
        print("A")
    else:
        print("B")
    t-=1