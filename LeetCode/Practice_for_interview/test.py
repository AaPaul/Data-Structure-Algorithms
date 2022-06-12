
# import time
# import random
# import pyautogui
 
# while 1:
#     # 5秒钟移动一次鼠标(移动鼠标时间可以根据自己需要设定)
#     time.sleep(30)
#     pyautogui.moveTo(x=1500,y=random.randint(100,900))

from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def check(l, h, x):
            while l < h:
                mid = l + (h - l) // 2
                if (x * potions[mid] < success):
                    l = mid + 1
                else:
                    h = mid
            return l
        n = len(potions)
        ans = []
        for i in spells:
            if i >= success:
                ans.append(n)
            else:
                pos = check(0, n-1, i)
                if pos == n-1 and i * potions[pos] < success:
                    ans.append(0)
                else:
                    ans.append(n - pos)
        return ans




spells=[3,1,2]
potions=[8,5,8]
success=16

s = Solution()
print(s.successfulPairs(spells, potions, success))