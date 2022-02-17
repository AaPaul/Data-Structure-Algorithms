# This is a question based on 'Find Minimum in Rotated Sorted Array'.
# I didn't solve this question.
class Solution:
    def findMin(self, nums):
        def bin_dfs(start, end):
            if end - start <=  1:
                self.Min = min(nums[start], nums[end], self.Min)
                return

            mid = (start + end)//2
            if nums[end] <= nums[mid]:
                bin_dfs(mid + 1, end)
            if nums[end] >= nums[mid]:
                bin_dfs(start, mid)
        
        self.Min = float("inf")
        bin_dfs(0, len(nums) - 1)
        return self.Min
        
        
# Reference
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/754100/Python-dfs-%2B-binary-search-explained
