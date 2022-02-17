from typing import List


class Solution:
    def search(self, L: int, a: int, modulus: int, n:int, nums:List[int]) -> str:
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus
        
        seen = {h}
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1

    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(s[i]) - ord('a') for i in range(n)]

        # base value
        a = 131
        modulus = 2**64-1

        left, right = 0, n

        while left != right:
            L = (left + right) // 2
            if self.search(L, a, modulus, n, nums) != -1:
                left = L + 1
            else:
                right = L

        start = self.search(left - 1, a, modulus, n, nums)
        return s[start: start+left-1] if start != -1 else ""


if __name__=="__main__":
    t1 = Solution()
    case1 = "nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy"
    print(t1.longestDupSubstring(case1))