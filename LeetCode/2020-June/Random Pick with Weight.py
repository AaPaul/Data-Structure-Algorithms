import random
# This is the solution from the reference. I didn't solve it by myself. This is the question which is related on
# picking with weight. Therefore, it is not a simple probability question. What we need to do is to transfer it as a
# cumulative probability distribution function. Then we use random numbers to perform a binary search. This question
# revealed that I am not familiar with binary search as well
class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.preSum = [0] * len(w)
        self.preSum[0] = w[0]
        for i in range(1, len(w)):
            self.preSum[i] = self.preSum[i - 1] + w[i]

    def pickIndex(self):
        """
        :rtype: int
        """
        total = self.preSum[-1]
        rand = random.randint(0, total - 1)
        left, right = 0, len(self.preSum) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if rand >= self.preSum[mid]:
                left = mid
            else:
                right = mid
        if rand < self.preSum[left]:
            return left
        return right


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
solution = Solution([1, 3, 2, 5]);
solution.pickIndex() # return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex() # return 1
solution.pickIndex() # return 1
solution.pickIndex() # return 1
solution.pickIndex() # return 0. It's returning the first element (index = 0) that has probability of 1/4.

'''
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.preSum = [0] * len(w)
        self.preSum[0] = w[0]
        for i in range(1, len(w)):
            self.preSum[i] = self.preSum[i-1] + w[i]



    def pickIndex(self):
        """
        :rtype: int
        """
        left, right = 0, len(self.preSum)-1
        maximum = self.preSum[-1]
        rand = random.randint(0, maximum-1) # The range of randint is (a, b+1)
        while left+1 < right:
            mid = (left+right) // 2
            if rand > self.preSum[mid]:
                left = mid
            else:
                right = mid
        if rand < self.preSum[left]:
            return left
        return right



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# obj = Solution([[1,3], []])
# obj.pickIndex()
        '''

''' 
# another way
    def __init__(self, w):
        wt, self.weights = 0, []
        for i in w:
            wt += i
            self.weights.append(wt)

    def pickIndex(self):
        rand = random.randint(1, self.weights[-1])
        lo, hi = 0, len(self.weights)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if self.weights[mid] < rand:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
'''


# reference
# https://blog.csdn.net/fuxuemingzhu/article/details/81807215
# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3351/discuss/682008/Python-simple-solution-with-explanation-in-comments