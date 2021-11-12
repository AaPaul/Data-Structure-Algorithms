import collections


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped = set()
        
        for i in range(len(s)):
            letter_s = s[i]
            letter_t = t[i]
            if letter_s in mapping:
                if letter_t != mapping[letter_s]:
                    return False

            else:
                if letter_t in mapped:
                    return False
                else:
                    mapping[letter_s] = letter_t
                    mapped.add(letter_t)
        
        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        s1,t1 = collections.defaultdict(list), collections.defaultdict(list)
        for i, ch in enumerate(s):
            s1[ch].append(i)
        for i, ch in enumerate(t):
            t1[ch].append(i)
        
        for x, y in zip(s1.values(), t1.values()):
            if x != y:
                return False
        return True