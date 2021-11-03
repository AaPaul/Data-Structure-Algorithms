class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            cnt += 1
            if i >= 2 and nums[i] < nums[i-2]:
                nums[i] = nums[i - 1]
            else:
                nums[i - 1] = nums[i]
        return cnt <= 1