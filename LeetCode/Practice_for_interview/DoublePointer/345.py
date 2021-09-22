# 345. Reverse Vowels of a String
class Solution:
    def vowelReverse(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] not in vowel:
                i += 1
            elif s[j] not in vowel:
                j -= 1
            else:
                t = s[i]
                s[i] = s[j]
                s[j] = t
                i += 1
                j -= 1
        return "".join(s)

if __name__ == "__main__":
    s1 = Solution()
    print(s1.vowelReverse('hello'))