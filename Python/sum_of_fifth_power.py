"""
You will be given a number N. Your task is to find sum of Fifth powers of the first N natural numbers 
1^5 + 2^5+ 3^5 + 4^5+ …….+ N^5 till N-th term.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. 
Then T test case follows, a single line of the input containing a positive integer N.

Output:
For each test-case, print sum of Fifth powers of the first N natural numbers 1^5 + 2^5+ 3^5 + 4^5+ …….+ N^5 
till N-th term.

Example:
Input:
3
1
2
3

Output:
1
33
276

Explanation:
For testcase 2: The first 2 natural numbers are 1 and 2. So 15+25=1+32=33
"""
t = int(input())
while t > 0:
    n = int(input())
    sum = ((n**2)*(n+1)**2*(2*n**2+2*n-1))//12
    print(sum)
    t -= 1