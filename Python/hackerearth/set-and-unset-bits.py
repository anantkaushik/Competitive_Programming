"""
Proble Link: https://www.hackerearth.com/challenge/college/bitbyte-republic-nation/algorithm/set-and-unset-bits/

Lazy problem setter runs out of stories for this problem and doesn't want to gift arrays on birthdays. 
Construct a sequence of positive integers for which the greatest common divisor of their count of set and unset bits is 1.
S = {xi : xi is a positive integer and gcd of count of its set and unset bits is 1}
You will be asked Q queries, each query contains a number  K. For each query you need to find the Kth element of this sequence.

Input:
First line contains Q and subsequent Q lines contain only one integer K.

Output:
Output Q lines each line containing Kth element of sequence S.

SAMPLE INPUT 
5
1
2
3
4
5
SAMPLE OUTPUT 
1
2
4
5
6

Explanation
Number	Binary	gcd(set,unset)
1	1	gcd(1,0) = 1
2	10	gcd(1,1) = 1
3	11	gcd(2,0) = 2
4	100	gcd(1,2) = 1
and so on, S = {1,2,4,5,6.....}
"""
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

arr = [1]
def seq(x):
    if x <= len(arr):
        return arr[x-1]
    n = arr[-1] + 1
    x = x - len(arr)
    while x:
        binary = bin(n)[2:]
        count1 = binary.count('1')
        count0 = binary.count('0')
        if gcd(count1,count0) == 1:
            arr.append(n)
            x -= 1
        n += 1
    return arr[-1]
    
for _ in range(int(input())):
    print(seq(int(input())))