"""
Back in Bombay in 1992, Gaitonde's terror was spreading as his men take out rival gang members by the dozen. 
Now, Gaitonde targeted 7 areas where he wanted his rule. He makes a team of 7 accomplices for the same.
Every day at 5 pm, Gaitonde used to communicate with his accomplices and asked them about the progress they have made. 
Gaitonde had given a "code" to all his accomplices for communication.
Delighted by his accomplices progress, he prepares dinner for them; seven chairs, seven plates, seven forks and seven 
knives for seven hungry gangsters.
On the day of dinner, nine gangsters came, instead of seven (nobody knows how or why), each of them claiming to be one 
of Gaitonde's seven accomplices.
Luckily, each accomplice had a "code" (which Gaitonde had given them). This "code" is a positive integer less than 100. 
Gaitonde, a famous mathematician, realised long ago that the sum of numbers on the "code" of his seven accomplices was 
exactly 100. You are manager of Gaitonde and he has shared this information with you. Now, you have to decide which 
of the seven gangsters are legit.
Write a program which determines which gangsters are legit, i.e. pick seven of nine numbers that add to 100.

Input Format:
There are 9 lines of input. Each contains an integer between 1 and 99 (inclusive). All of the numbers will be distinct.
Note: The test data will be such that the solution is unique.

Constraints:
Time Limit: 1 second

Output Format:
Your program must produce exactly seven lines of output – the "codes" of Gaitonde's seven gangsters. 
Output the numbers in any order. 

Sample Test Cases:
Sample Input 1:
7
8
10
13
15
19
20
23
25
Sample Output 1:
7
8
10
13
19
20
23
Explanation:
Out of the given 9 value, only these 7 values sum up to form 100. 
"""
#Write your code here
arr = []
for i in range(9):
  arr.append(int(input()))
 
summ = sum(arr)
target = summ - 100
nums = set()
discard = []
for i in arr:
  temp = target - i
  if temp in nums:
    discard.append(i)
    discard.append(temp)
    break
  nums.add(i)
for i in arr:
  if i not in discard:
    print(i)