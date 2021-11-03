class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return False
        
        f_n = len(flowerbed)
        # prevent boundry overflow
        flowerbed = flowerbed + [0]
        
        res = 0
        if flowerbed[0] == 0 and flowerbed[1] != 1:
            res += 1
            flowerbed[0] = 1

        for i in range(1, f_n):
            # if flowerbed[i] == 1:
            #     continue
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                res += 1
                flowerbed[i] = 1
        return res >= n
            


        