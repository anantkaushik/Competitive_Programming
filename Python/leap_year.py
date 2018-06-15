"""
For an input year tell whether the year is leap or not. 

Input:
First line contains an integer, the number of test cases 'T' Each test case should contain 
a positive integer N(Year).

Output:
Print "Yes" if it is a leap year else "No". (Without the double quotes)

Example:
Input:
1
4

Output:
Yes
"""
t = int(input())
while t > 0:
    n = int(input())
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")
    else:
        print("No")
    t -= 1