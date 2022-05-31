def solution(words, variableName):
    n = len(words)
    l = len(variableName)
    # visited = []
    def check(lt, string):
        if lt > l:
            return False
        if lt == l:
            return string == variableName
        for i in range(n):
            # if i not in visited:
            #     visited.append(i)
            t = words[i]
            ltt = len(t)
            if t == variableName[lt: lt+ltt]:
                return check(lt+ltt, string+t)
            elif t.title() == variableName[lt: lt+ltt]:
                return check(lt+ltt, string+t.title())
                # else:
                #     visited.pop()
                #     continue
        return False
    
    ans = check(0, '')
        
    
    return ans
words = ['is', 'valid', 'right']
var = 'isValid'
s = solution(words, var)

print(s)