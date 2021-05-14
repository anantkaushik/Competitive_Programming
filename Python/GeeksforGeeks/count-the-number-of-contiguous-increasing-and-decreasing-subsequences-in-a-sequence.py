"""
For a given distinct integer sequence of size N, the task is to count the number of contiguous increasing subsequence and 
contiguous decreasing subsequence in this sequence.

Examples: 
Input: arr[] = { 80, 50, 60, 70, 40 } 
Output: 1 2 
Explanation: 
The only one increasing subsequence is (50, 60, 70) and 
two decreasing subsequences are (80, 50) and (70, 40).

Input: arr[] = { 10, 20, 23, 12, 5, 4, 61, 67, 87, 9 } 
Output: 2 2 
Explanation: 
The increasing subsequences are (10, 20, 23) and (4, 61, 67, 87) 
whereas the decreasing subsequences are (23, 12, 5, 4) and (87, 9). 
"""
def num_of_subseq(seq):
    is_decreasing_regularly = is_increasing_regularly = False

    increasing = decreasing = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1] and not is_increasing_regularly:
            increasing += 1
            is_increasing_regularly = True
            is_decreasing_regularly = False
        elif seq[i] < seq[i-1] and not   is_decreasing_regularly:
            decreasing += 1
            is_decreasing_regularly = True
            is_increasing_regularly = False

    return increasing, decreasing
