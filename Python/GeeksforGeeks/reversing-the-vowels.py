"""
Given a string, reverse only the vowels present in it and print the resulting string.

Input: First line of the input file contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case has a single line containing a string.

Output: Corresponding to each test case, output the string with vowels reversed.

Sample Input:
4
geeksforgeeks
practice
wannacry
ransomware

Sample Output:
geeksforgeeks
prectica
wannacry
rensamwora
"""
t = int(input())
while t > 0:
    s = input()
    vowels = []
    for i in s:
        if i in "aeiou":
            vowels.append(i)
    new = ""
    for i in s:
        if i in "aeiou":
            new += vowels.pop()
        else:
            new += i
    print(new)
    t -= 1