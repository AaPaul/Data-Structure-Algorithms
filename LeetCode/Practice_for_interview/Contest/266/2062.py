class Solution:
    # BruteForce
    def countVowelSubstrings(self, word: str) -> int:
        n = len(n)
        ans = 0
        for i in range(n):
        # i 为起始点， 遍历后面所有长度大于等于5位的子字符串
            for j in range(i+4, n):
                sub = word[i:j+1]
                # set 去除重复字母
                s = set(sub)
                flag = True
                if len(s) == 5:
                    for ch in s:
                        if ch not in 'aeiou':
                            flag = False
                            break
                if flag == True:
                    ans += 1
        
        return ans

    # Sliding window
    def countVowelSubstrings2(self, word: str) -> int:
        '''
        i: current position
        j: the start position of vowel substring
        k: the window between k-1 and i is the smallest window including 5 vowels('aeiou')
        cnt: the number of required substring

        k-j is the number of required substring in i position
        '''
        m = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        
        j = k = cnt = vow = 0
        n = len(word)
        for i in range(n):
            if word[i] in m.keys():
                m[word[i]] += 1
                vow += m[word[i]] == 1

                while vow == 5:
                    m[word[k]] -= 1
                    vow -= m[word[k]] == 0
                    k += 1
                cnt += k - j

            else:
                for c in 'aeiou':
                    m[c] = 0
                vow = 0
                j = k = i+1
        return cnt