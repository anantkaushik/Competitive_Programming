"""
Shreya has to find the strangeness of the array. The strangeness at an index ‘i’ is defined as the number of indices 
(continuous) starting from ‘i’ having the same sign as A[i]. You have to help Shreya to find the strangeness of the 
array at each position.

For example: 2 3 9 -2 3
The strangeness at 1st position is 3.

Input:
First line will have an integer ‘n’ denoting the value of size of array.
Next line will have ‘n’ space separated integers denoting the array.

Constraints:
1 <= n <= 10^6
-10^9 <= Ai <= 10^9
Time Limit: 1 second

Output:
Print ‘n’ space separated integers denoting the strangeness of array at particular index.

Sample Input:
5
2 3 9 -2 3
Sample Output:
3 2 1 1 1
"""
# Write your code here
n = int(input())
nums = list(map(int,input().split()))

i = j = count = 0
while i < len(nums):
  if nums[i] > 0 and nums[j] > 0:
    count += 1
  elif nums[i] <= 0 and nums[j] <= 0:
    count += 1
  else:
    while j != i:
      nums[j] = count
      count -= 1
      j += 1
    i -= 1
  i += 1
while j != i:
  nums[j] = count
  count -= 1
  j += 1
    
print(*nums)