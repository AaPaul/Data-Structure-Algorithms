class Solution:
    """
    preNum is the represent of dp array. In fact, we only care abou the sum
    of subarray until now, therefore we can just use a variabel to record the sum
    and the space complexity can be reduced from O(n) to O(1).
    """
    def maxSubArray(self, nums: List[int]) -> int:
        # preNum = nums[0]
        preNum = 0
        maxSub = nums[0]
        
        for i in range(len(nums)):
            preNum = max(preNum + nums[i], nums[i])
            # preNum = preNum + nums[i] if preNum > 0 else nums[i]
            maxSub = max(preNum, maxSub)
        return maxSub