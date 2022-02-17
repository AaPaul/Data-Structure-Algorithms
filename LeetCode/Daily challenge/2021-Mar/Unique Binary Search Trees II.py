class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        result = []
        if start > end:
            result.append(None)
            return result

        for i in range(start, end + 1):
            # generate left and right sub tree
            leftTree = self.helper(start, i - 1)
            rightTree = self.helper(i + 1, end)
            # link left and right sub tree to root(i)
            for j in range(len(leftTree)):
                for k in range(len(rightTree)):
                    root = TreeNode(i)
                    root.left = leftTree[j]
                    root.right = rightTree[k]
                    result.append(root)

        return result

test = Solution()
test.generateTrees(3)