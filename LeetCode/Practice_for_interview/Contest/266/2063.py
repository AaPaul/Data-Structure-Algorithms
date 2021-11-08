class Solution:
    # In ith letter which is a vowel, the number of substring should be 
    # (i + 1) * (n - i)
    def countVowels(self, word: str) -> int:
        ans = 0
        n = len(word)
        for i, ch in enumerate(word):
            if ch in 'aeiou':
                ans += (i+1) * (n-i)
        
        return ans

    # Brute force. Time limitition
    def countVowels2(self, word: str) -> int:
        ans = 0
        n = len(word)
        for i in range(n):
            c = 0
            for j in range(i, n):
                if word[j] in 'aeiou':
                    c += 1
                ans += c
        return ans