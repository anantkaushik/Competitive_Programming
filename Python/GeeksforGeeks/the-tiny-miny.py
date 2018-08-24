"""
Find the smallest number that can be framed using the series created by the digits obtained by raising the given number 
(  "a"  ) to the power from 1 to  n  i.e.  a^1 , a^2 , a^3 .......a^n . We get  b1,b2 , b3 , ........... bn . 
Using all the digits  ( including repeating ones )  that appear inb1 ,b2 , b3 .... bn . Frame a number that contains all 
the digits ( including repeating ones )  and find out the combination of digits that make the smallest number of all 
possible combinations. Excluding or neglecting zeroes  ( " 0 " )  . 

Input: The first line contains a number T i.e numbers of  test cases . Followed by each test case that contains two 
integers "a" and "n" . 

Output: Output of each test case contains an integer which is the smallest number out of all combinations .

Sample Input 
4
9 4
5 1
6 5
90 4

Sample Output:
1125667899
5
11223666667779
1125667899

Explanation :
Test case 1: 9 3 
9^1 = 9
9^2 = 81
9^3 = 729
9^4  = 6561 
9 81 729 6561
We get  9817296561 .
Using 9817296561 number we need to find the smallest possible number that can be framed using other combinations of the samenumber.
1298796561
8799265611
2186561997
.
.
.
1125667899
The smallest possible number that can be framed is1125667899 .
"""
t = int(input())
while t > 0:
    a,n = map(int,input().split())
    res = ""
    for i in range(1,n+1):
        res += str(a**i)
    result = list(res)
    print(("".join(sorted(result))).lstrip('0'))
    t -= 1