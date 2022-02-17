'''
https://leetcode.com/discuss/interview-question/1557009/amazon-oa-valid-string

Similar question as https://leetcode.com/problems/valid-parentheses/

An empty string is valid
You can add same character to a valid string X, and create another valid string yXy
You can concatenate two valid strings X and Y, so XY will also be valid.
Ex: vv, xbbx, bbccdd, xyffyxdd are all valid.
'''

def isValid(s:str) -> bool:
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    return True if not stack else False

print(isValid('vv'))
print(isValid('bbccdd'))
print(isValid('aabbcd'))
        