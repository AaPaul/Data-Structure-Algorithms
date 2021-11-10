class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        res = []

        for i, ch in enumerate(expression):
            if ch in '*-+':
                left = self.diffWaysToCompute(expression[: i])
                right = self.diffWaysToCompute(expression[i+1:])
            
                for l in left:
                    for r in right:
                        if ch == '-':
                            res.append(l - r)
                        elif ch == '+':
                            res.append(l + r)
                        else:
                            res.append(l * r)

        return res