
# import time
# import random
# import pyautogui
 
# while 1:
#     # 5秒钟移动一次鼠标(移动鼠标时间可以根据自己需要设定)
#     time.sleep(30)
#     pyautogui.moveTo(x=1500,y=random.randint(100,900))

from typing import List
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        n = len(brackets)
        i = 0
        while income > 0 and i < n:
            t = brackets[i][0]
            p = brackets[i][1]
            if i == 0:
                if income < t:
                    t = income
                    income = 0
                prev = t
            else:
                if income > t:
                    t = t - prev
                    prev = t
                else:
                    t = income - prev
                    income = 0
                
            tax += (t * p / 100.0)
            i += 1
        return tax
            
                


brackets=[[3,50],[7,10],[12,25]]
income=10

s = Solution()
print(s.calculateTax(brackets, income))