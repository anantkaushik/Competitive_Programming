"""
Problem Link: https://practice.geeksforgeeks.org/problems/find-winner-of-the-game-of-nim/0

In Game of Nim, two players take turns removing objects from heaps or the pile of stones.
Suppose two players A and B are playing the game. Each is allowed to take only one stone from the pile. The player who picks the last stone of the 
pile will win the game. Given N the number of stones in the pile, the task is to find the winner, if player A starts the game .

Input:
The input line contains T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.

Output:
Print the winner i.e. Player A or Player B for each testcase in a separate line.

Constraints:
1 <= T <= 100
1 <= N <= 1000

Example:
Input:
2
3
15

Output:
Player A
Player A

Explanation:
Testcase 1: Player A remove stone 1 which is at the top, then Player B remove stone 2
and finally player A removes the last stone.
"""
for _ in range(int(input())):
    print("Player A" if int(input()) % 2 != 0 else "Player B")