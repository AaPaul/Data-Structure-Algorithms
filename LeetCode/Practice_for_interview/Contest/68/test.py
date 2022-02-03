class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                stack.append([s[i], locked[i]])
            else:
                if not stack:
                    return False
                t = stack.pop()
                if t[0] != '(' and t[1] != '0':
                    return False
        
        return True if len(stack) % 2 == 0 else False
                
            
                
s1 = Solution()
s = "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
locked = "100011110110011011010111100111011101111110000101001101001111"

print(s1.canBeValid(s, locked))