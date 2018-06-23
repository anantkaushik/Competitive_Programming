"""
Akash loves writing with red or green pen and to impress him his friend Kiran buys him N 
pens of 'red' or 'green' colors but Akash isn't happy to see two coloured pens ,
he wants all N pen of same color either 'red' or 'green'.He requested Kiran for the 
exchange of M pens(from the shop) so that he can have all N pens of same color 
i.e. either 'Red' or'Green. Help kiran to find the minimum number of pens(M) she should 
ask for the exchange from the shopkeeper.

Input:
The first line of input contains an integer T denoting the number of test cases . 
Next line of input contains a positive  number N denoting the number of pens Kiran 
buys for Akash and the next line of input contains the string sequence of N pen 
colours-R for 'Red' and 'G' for 'green'.

Output:
For each test case , the output is in a new line containg an integer M which 
is the minimum number of pens Kiran has to exchange.

Example:
Input :
1
5
RGRGR
Output:
2
"""
t = int(input())
while t > 0:
    n = int(input())
    s = input()
    g = s.count("G")
    print(min(g,n-g))
    t -= 1