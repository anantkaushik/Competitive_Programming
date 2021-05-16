"""
Problem Link: https://practice.geeksforgeeks.org/problems/shortest-direction4201/1

A person wants to go from origin to a particular location, he can move in only 4 directions(i.e East, West, North, South) 
but his friend gave him a long route, help a person to find minimum Moves so that he can reach to the destination.
Note: You need to print the lexicographically sorted string. Assume the string will have only ‘E’ ‘N’ ‘S’ ‘W’ characters.

Example 1:
Input:
S = "SSSNEEEW"
Output: EESS
Explanation: Following the path SSSNEEEW
and EESS gets you at the same final point.
There's no shorter path possible.

Example 2:
Input: 
S = "NESNWES"
Output: E
Explanation: Following the path NESNWES
and E gets you at the same final point.
There's no shorter path possible.

Your Task:
You don't need to read input or print anything. Your task is to complete the function shortestPath() which takes the string 
S as input and returns the resultant string denoting the shortest path in lexicographic order.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|) for output.

Constraints:
1<=|S|<=105
"""
class Solution:
    def shortestPath(self, s):
        count = {
            "E": 0,
            "W": 0,
            "S": 0,
            "N": 0
        }
        
        for direction in s:
            count[direction] += 1
        
        res = ""
        if count["E"] > count["W"]:
            res += ("E" * (count["E"] - count["W"]))
        if count["S"] < count["N"]:
            res += ("N" * (count["N"] - count["S"]))
        if count["S"] > count["N"]:
            res += ("S" * (count["S"] - count["N"]))
        if count["E"] < count["W"]:
            res += ("W" * (count["W"] - count["E"]))
        
        return res
