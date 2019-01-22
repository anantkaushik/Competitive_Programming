"""
A thief wants to loot houses. He knows the amount of money in each house. He cannot loot two consecutive houses. 
Find the maximum amount of money he can loot.

Input Format
Line 1 : An integer N 
Line 2 : N spaced integers denoting money in each house

Output Format
Line 1 : Maximum amount of money looted

Input Constraints
1 <= n <= 10^4
1 <= A[i] < 10^4

Sample Input:
6
5 5 10 100 10 5
Sample Output:
110
"""
## Read input as specified in the question.
## Print output as specified in the question.
def rob(nums,l):
  if l == 0: return 0
  elif l == 1: return nums[0]
  prev2, prev1 = nums[0], max(nums[0], nums[1])

  for i in range(2, l):
    curr = max(prev1, prev2 + nums[i])
    prev2 = prev1
    prev1 = curr
  return prev1
  
n = int(input())
nums = list(map(int,input().split()))
print(rob(nums,n))