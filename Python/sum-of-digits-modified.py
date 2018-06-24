"""
A number is said to be a magic number, if the sum of its digits are calculated till a 
single digit recursively by adding the sum of the digits after every addition. If the 
single digit comes out to be 1,then the number is a magic number.

Input:
First line of input contains a single integer T, denoting the number of test cases. 
First line of each test case contains an integer N.
 
Output:
For each of the test case print whether the number N is "Magic" or "Not Magic"

Example:
Input:
2
1234
67

Output
Magic
Not Magic

Explanation:
1234 sums up to 10 which sums upto 1 so its a Magic Number.
67 sums up to 13 which sums upto 4 so its not a Magic Number
"""
def digitalRoot(num): #reference- https://en.wikipedia.org/wiki/Digital_root
    if num < 10:
        return num
    return num % 9 if num % 9 != 0 else 9

t = int(input())
while t > 0:
    print("Magic" if digitalRoot(int(input()))==1 else "Not Magic")
    t -= 1
