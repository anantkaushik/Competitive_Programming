"""
Print the common elements in Two Sorted Arrays.
"""
def commonElements(arr1,arr2):
    p1 = p2 = 0
    res = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
            p2 += 1
        elif arr1[p1] > arr2[p2]:
            p2 += 1
        else:
            p1 += 1
    return res

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
print(*commonElements(arr1,arr2))