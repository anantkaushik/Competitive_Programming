"""
Problem Link: https://www.interviewbit.com/problems/fizzbuzz/

Fizzbuzz is one of the most basic problems in the coding interview world. 
Try to write a small and elegant code for this problem. 

Given a positive integer A, return an array of strings with all the integers from 1 to N.
But for multiples of 3 the array should have “Fizz” instead of the number.
For the multiples of 5, the array should have “Buzz” instead of the number.
For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz” instead of the number.

Look at the example for more details.
Example
A = 5
Return: [1 2 Fizz 4 Buzz]
"""
class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        res = []
        for i in range(1, A+1):
            if not i % 3 and not i % 5:
                res.append("FizzBuzz")
            elif not i % 3:
                res.append("Fizz")
            elif not i % 5:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
