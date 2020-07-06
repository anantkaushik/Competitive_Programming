"""
Problem Link: https://www.interviewbit.com/problems/mathbug01/

Following code tries to figure out if a number is prime
However, it has a bug in it.
Please correct the bug and then submit the code.
"""
class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        upperLimit = int(A**0.5)
        for i in xrange(2, upperLimit + 1):
            if A % i == 0:
                return 0
        return int(A != 1)
