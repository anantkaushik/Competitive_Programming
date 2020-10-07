import re

patterns = [ r'[a-z]', r'[A-Z]' , r'[13579]'  ,r'[02468]']
data = input()
t = [  r for pattern in patterns for r in sorted(re.findall( pattern, data ))  ]
print("".join(t))
