# A dynamic programming problem, solving it by recursive
# res = \sum{numSubTree{i-1} * numSubTree{n-i}}_1^n

class Solution:
    def numTrees(self, n: int) -> int:
        # the length should be n+1 as this process includes 0.
        numSubtrees = [1] * (n+1)
        # calculate the number of BST for each node.
        for node in range(2, n+1):
            sum = 0
            # calculate the number of BST for node.
            for root in range(1, node+1):
                left = root - 1
                right = node - root
                sum += numSubtrees[left] * numSubtrees[right]
            numSubtrees[node] = sum

        return numSubtrees[n]
        # def recursive(num):
        #     if num == 0:
        #         return 1
        #     elif num == 1:
        #         return 1
        #     elif num == 2:
        #         return 2
        #     elif num == 3:
        #         return 5
        #     else:
        #         return recursive(num-1) * recursive(num+1)
        # sum = 0
        # for i in range(1, n+1):
        #     sum += recursive(i)
        # return sum

S1 = Solution()
res = S1.numTrees(5)
print(res)
