"""
Print the given pattern without using loop.
Example:

Input:
123456
Output:
100000 + 20000 + 3000 + 400 + 50 + 6

Input:
654
Output:
600 + 50 + 4
"""
s = ""
i = 0
def check(num,l):
    global s
    global i
    if l <= 0:
        return s
    s += num[i] + ''.join(map(str, [0]*(l-1)))
    i+=1
    l-=1
    if l!=0:
        s+= " + "
    return check(num,l)
    
num = input()
i = 0
l = len(num)
print(check(num,l))
