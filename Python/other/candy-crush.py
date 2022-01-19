"""
Implement 1-d Candy crush. Any sequence of 3 or more like items should be removed from left.
Input: "aabbbacd"
Output: "cd"
"""

def candy_crush(input):
    if not input:
        return ""
        
    stack = []
    char = input[0]
    f = 1
    
    for index in range(1, len(input)):
        if char == input[index]:
            f += 1
        else:
            if f >= 3:
                char = input[index]
                if stack and char == stack[-1][0]:
                    f = stack.pop()[1] + 1
                else:
                    f = 1
            else:
                stack.append([char, f])
                char = input[index]
                f = 1
            
    if f < 3:
        stack.append([char, f])
    
    res = []
    while stack:
        char, f = stack.pop()
        res.append(char*f)
    
    return "".join(res[::-1])
