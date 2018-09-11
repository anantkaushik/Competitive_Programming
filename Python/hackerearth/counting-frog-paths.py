"""
There is a frog initially placed at the origin of the coordinate plane. In exactly 1 second, the frog can either move up 1 unit, 
move right 1 unit, or stay still. In other words, from position (x,y), the frog can spend 1 second to move to:
(x+1,y)
(x,y+1)
(x,y)
After T seconds, a villager who sees the frog reports that the frog lies on or inside a square of side-length s with coordinates 
(x,y),(x+s,y) ,(x,y+s) ,(x+s,y+s). Calculate how many points with integer coordinates on or inside this square could 
be the frog's position after exactly T seconds.

Input Format:
The first and only line of input contains four space-separated integers: x, y, s, and T.

Output Format:
Print the number of points with integer coordinates that could be the frog's position after T seconds.

SAMPLE INPUT 
2 2 3 6
SAMPLE OUTPUT 
6
"""
x,y,s,t = map(int,input().split())
print(sum(1 for i in range(s+1) for j in range(s+1) if(x+i+y+j <= t)))