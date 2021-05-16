"""
Problem Link: https://practice.geeksforgeeks.org/problems/269f61832b146dd5e6d89b4ca18cbd2a2654ebbe/1

Aterp is the head nurse at a city hospital. City hospital contains R*C number of wards and the structure of a hospital 
is in the form of a 2-D matrix.

Given a matrix of dimension R*C where each cell in the matrix can have values 0, 1, or 2 which has the following meaning:
0: Empty ward
1: Cells have uninfected patients
2: Cells have infected patients

An infected patient at ward [i,j] can infect other uninfected patient at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] 
(up, down, left and right) in unit time. Help Aterp determine the minimum units of time after which there won't 
remain any uninfected patient i.e all patients would be infected. If all patients are not infected after infinite units 
of time then simply return -1.

Example 1:
Input:
3 5
2 1 0 2 1
1 0 1 2 1
1 0 0 2 1 
Output:
2
Explanation:
Patients at positions {0,0}, {0, 3}, {1, 3}
and {2, 3} will infect patient at {0, 1}, 
{1, 0},{0, 4}, {1, 2}, {1, 4}, {2, 4} during 1st 
unit time. And, during 2nd unit time, patient at 
{1, 0} will get infected and will infect patient 
at {2, 0}. Hence, total 2 unit of time is
required to infect all patients.

Example 2:
Input:
3 5
2 1 0 2 1
0 0 1 2 1
1 0 0 2 1
Output:
-1
Explanation:
All patients will not be infected.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function helpaterp() which takes a 
2-D Matrix hospital as input parameter and returns the minimum units of time in which all patients will be infected 
or -1 if it is impossible.

Expected Time Complexity: O(R*C)
Expected Auxiliary Space: O(R*C)

Constraints:
1 ≤ R,C ≤ 1000
0 ≤ mat[i][j] ≤ 2
"""
class Solution:
    def helpaterp(self, hospital):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = []
        total_uninfected_patients = 0
        
        for i in range(len(hospital)):
            for j in range(len(hospital[0])):
                if hospital[i][j] == 2:
                    queue.append([i, j])
                elif hospital[i][j] == 1:
                    total_uninfected_patients += 1
        
        if not total_uninfected_patients:
            return 0
    
        time_taken = 0
        while queue and total_uninfected_patients:
            time_taken += 1
            
            for _ in range(len(queue)):
                row, col = queue.pop(0)
                
                for direction in directions:
                    next_row = row + direction[0]
                    next_col =col + direction[1]
                    
                    if not self.is_valid(next_row, next_col, hospital):
                        continue
                    
                    total_uninfected_patients -= 1
                    hospital[next_row][next_col] = 2
                    queue.append([next_row, next_col])
        
        return time_taken if not total_uninfected_patients else -1
    
    def is_valid(self, row, col, hospital):
        if row >= 0 and col >= 0 and row < len(hospital) and col < len(hospital[0]) and hospital[row][col] == 1:
            return True
        return False
