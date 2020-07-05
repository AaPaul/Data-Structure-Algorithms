

class Solution:
    # run time error
    def hammingDistance1(self, x: int, y: int) -> int:
        b_max, b_min = str(reversed(max(bin(x), bin(y)))), str(reversed(min(bin(x), bin(y))))
        count = 0
        for i in range(len(b_min)-2):
            if b_max[i] != b_min[i]:
                count += 1

        for i in range(len(b_min)-2, len(b_max)-2):
            if b_max[i] != '0':
                count += 1

        return count

    # >> is Shift operation
    # this function will return the bin version of the number while it needs to be reversed.
    def toBin(self, x: int):
        res = []
        while (x > 0):
            # res.insert(0, x%2)
            res.append(x%2)
            x >>= 1
        return res

    def hammingDistance(self, x: int, y: int) -> int:
        n_max, n_min = max(x, y), min(x, y)
        b_max, b_min = self.toBin(n_max), self.toBin(n_min)
        count = 0
        for i in range(len(b_min)):
            if b_min[i] != b_max[i]:
                count += 1

        for i in range(len(b_min), len(b_max)):
            if b_max[i] != 0:
                count += 1

        return count



s1 = Solution()
print(s1.hammingDistance(1501377268, 258791155))
# print(s1.hammingDistance(1, 8))
