"""
Amicable numbers are two different numbers so related that the sum of the proper divisors 
of each is equal to the other number. (A proper divisor of a number is a positive factor 
of that number other than the number itself.

INPUT: The first line consists of an integer T i.e. the number of test cases. 
First and the last line of each test case consists of two integers x and y.
OUTPUT: Print '1' if the following pair is amicable pair otherwise print '0'.

SAMPLE INPUT :
2
220 284
1 2

SAMPLE OUTPUT : 
1
0

Explanation :
Test Case 1 : Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110. 
Sum of these is 284. Proper divisors of 284 are 1, 2, 4, 71 and 142 with sum 220.
"""
for _ in range(int(input())):
    a,b=map(int,input().split())
    if sum(i for i in range(1,int(a/2)+1) if a%i==0) == b and sum(i for i in range(1,int(b/2)+1) if b%i==0) == a:
        print("1")
    else:
        print("0")