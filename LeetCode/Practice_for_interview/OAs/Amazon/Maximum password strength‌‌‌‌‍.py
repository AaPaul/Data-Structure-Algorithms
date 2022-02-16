'''
https://leetcode.com/discuss/interview-question/1526418/
https://leetcode.com/discuss/interview-question/1527679/amazon-oa-password-strength

'''

def passwordStrength(password):
    last = {chr(97 + i): -1 for i in range(26)}
    ret = 0
    for i,ch in enumerate(password):
        left = i - last[ch]
        right = len(password) - i
        ret += left * right
        last[ch] = i
        
    return ret

if __name__ == "__main__":
    print(passwordStrength('good'))