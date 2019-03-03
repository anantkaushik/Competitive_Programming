"""
Check if an sorted array is a rotation of another sorted array.
"""
def isRotation(a,b):
    if len(a) != len(b):
        return False
    key,keyIndex = a[0],-1
    for i in range(len(b)):
        if key == b[i]:
            keyIndex = i
            break
    if keyIndex == -1:
        return False
    for i in range(len(a)):
        j = (i+keyIndex) % len(a)
        if a[i] != b[j]:
            return False
    return True

a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(isRotation(a,b))