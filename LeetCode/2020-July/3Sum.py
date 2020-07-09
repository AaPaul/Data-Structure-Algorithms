from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            if (i == 0 or nums[i] != nums[i-1]):
                left = i + 1
                right = len(nums) - 1
                sum1 = 0 - nums[i]
                # temp = []
                while left < right:
                    if (nums[left] + nums[right] == sum1):
                        res.append([nums[i], nums[left], nums[right]])
                        # temp.append(nums[i])
                        # temp.append(nums[left])
                        # temp.append(nums[right])
                        # res.append(temp)
                        while (left < right and nums[left] == nums[left + 1]):
                            left += 1
                        while (left < right and nums[right] == nums[right - 1]):
                            right -= 1
                        left += 1
                        right -= 1
                    elif (nums[left] + nums[right] < sum1):
                        left += 1
                    else:
                        right -= 1

        return res

        # nums_hash = {}
        # for i in nums:
        #     if i not in nums_hash:
        #         nums_hash[i] = 1
        #     else:
        #         nums_hash[i] += 1
        # res = []
        # for i in nums_hash.keys():
        #     sum = i
        #     temp = [i]
        #     for j in nums_hash.keys():
        #         if i==j:
        #             continue
        #         if len(temp) < 2:
        #             temp.append(j)
        #         sum += j
        #         if
